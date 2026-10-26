"""The generated in-IDE script: placeholders, baked values, command coverage."""

import re

import pytest

from codesyskit import agentscript, errors


TOKEN = "0123456789abcdef0123456789abcdef"


def render(**kwargs):
    return agentscript.render(token=kwargs.pop("token", TOKEN), port=kwargs.pop("port", 0),
                              state_file=r"D:\tmp\state.json", log_file=r"D:\tmp\service.log",
                              **kwargs)


def test_no_placeholders_left():
    source = render()
    assert "@@" not in source


def test_values_are_baked_in():
    source = render(port=5599, allow_exec=True)
    assert TOKEN in source
    assert "PORT = 5599" in source
    assert "ALLOW_EXEC = True" in source
    assert 'STATE_FILE = "D:\\\\tmp\\\\state.json"' in source


def test_allow_exec_defaults_off():
    assert "ALLOW_EXEC = False" in render()


def test_script_exits_by_itself():
    source = render()
    assert "SYSTEM.exit(0)" in source


def test_every_error_code_is_used_by_the_server():
    source = render()
    for code in ("E_TOKEN", "E_PROTOCOL", "E_TIMEOUT", "E_UNKNOWN_CMD", "E_ARGS",
                 "E_STATE", "E_UNAVAILABLE", "E_SCRIPT"):
        assert code in source, code


def test_every_command_is_dispatched():
    source = render()
    table = source.split("COMMANDS = {", 1)[1].split("}", 1)[0]
    commands = re.findall(r'"([a-z][a-z0-9._]*)"\s*:', table)
    assert "ping" in commands and "build" in commands and "quit" in commands
    assert len(commands) >= 15


def test_short_token_rejected():
    with pytest.raises(ValueError):
        agentscript.render(token="short", port=0, state_file="a", log_file="b")


def test_write_path_uses_replace_not_text_assignment():
    """The measured gotcha: doc.text is read-only, replace(offset, length, text) is the way."""
    source = render()
    assert "document.replace(0, document.length, text)" in source
    assert not re.search(r"document\.text\s*=", source)


# --- extended surface invariants ------------------------------------------------

NEW_COMMANDS = (
    "commands", "execute", "object.info", "object.rename", "object.delete", "object.move",
    "folder.create", "find.text", "libraries", "library.add", "export.xml", "import.xml",
    "export.native", "project.archive", "generate.runtime", "project.doc",
    "online.login", "online.logout", "online.state", "online.start", "online.stop",
    "online.read", "online.write", "online.download",
)


def test_extended_commands_are_registered():
    source = render()
    table = source.split("COMMANDS = {", 1)[1].split("}", 1)[0]
    for name in NEW_COMMANDS:
        assert '"%s":' % name in table, name


def test_replies_are_utf8_and_sent_completely():
    """Measured bug: raw char codes raised 'Cannot convert int(36333) to Byte' on Chinese."""
    source = render()
    assert "Encoding.UTF8.GetBytes(text)" in source
    assert "while sent < total" in source
    assert "SocketFlags.None" in source


def test_requests_are_decoded_as_utf8():
    source = render()
    assert '.decode("utf-8", "replace")' in source


def test_mutating_commands_refuse_the_project_root():
    source = render()
    for command in ("cmd_object_rename", "cmd_object_delete", "cmd_object_move"):
        body = source.split("def %s(" % command, 1)[1].split("\ndef ", 1)[0]
        assert "mutable_node(" in body, command
    assert "refusing to modify the project root" in source


def test_folder_create_computes_the_path_from_the_parent():
    """The object returned by create_folder has no name yet, so path_of() yields '/'."""
    source = render()
    body = source.split("def cmd_folder_create(", 1)[1].split("\ndef ", 1)[0]
    assert 'parent_path.rstrip("/") + "/" + name' in body
    assert "walk(project, path)" in body


def test_online_login_maps_engine_failure_to_e_codesys():
    source = render()
    body = source.split("def online_login_now(", 1)[1].split("\ndef ", 1)[0]
    assert 'CmdError("E_CODESYS"' in body


def test_online_uses_the_device_simulation_flag():
    """The working headless path is device.set_simulation_mode(True) -- no gateway service."""
    source = render()
    assert "node.set_simulation_mode(bool(enabled))" in source
    assert "def device_node(" in source
    assert "def cmd_online_monitor(" in source


def test_path_walk_skips_a_leading_project_name():
    source = render()
    body = source.split("def walk(", 1)[1].split("\ndef ", 1)[0]
    assert "segments[0] == root_name" in body
