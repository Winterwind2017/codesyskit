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
