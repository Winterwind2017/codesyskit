"""Self-check: the kit is importable, documented, and internally consistent.

    python tools/selfcheck.py

Exits non-zero on the first inconsistency.  No CODESYS needed.
"""

import ast
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
FAILURES = []


def check(name, condition, detail=""):
    if condition:
        print("[ok]   %s" % name)
    else:
        print("[FAIL] %s %s" % (name, detail))
        FAILURES.append(name)


def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def main():
    sys.path.insert(0, SRC)

    # 1. importable and versioned
    import codesyskit
    from codesyskit import agentscript, client, cli, errors, protocol, service

    check("package imports", True)
    check("version present", bool(codesyskit.__version__), codesyskit.__version__)
    check("protocol version is 1", protocol.PROTOCOL_VERSION == 1)

    # 2. error code table is closed and unique
    check("error codes unique", len(set(errors.ALL)) == len(errors.ALL))
    check("OK is in ALL", errors.OK in errors.ALL)
    check("no legacy code names", all(code.startswith(("OK", "E_")) for code in errors.ALL))

    # 3. every command the server dispatches is documented
    source = agentscript.render(token="0" * 32, port=0, state_file="s", log_file="l")
    table = source.split("COMMANDS = {", 1)[1].split("}", 1)[0]
    commands = set(re.findall(r'"([a-z][a-z0-9._]*)"\s*:', table))
    protocol_doc = read(os.path.join(ROOT, "docs", "PROTOCOL.md"))
    documented = set(re.findall(r"^\| `([a-z][a-z0-9._]*)`", protocol_doc, re.M))
    missing = sorted(commands - documented)
    check("all server commands documented", not missing, ",".join(missing))

    # 4. client convenience methods only use documented commands
    client_source = read(os.path.join(SRC, "codesyskit", "client.py"))
    used = set(re.findall(r'self\.call\("([a-z][a-z0-9._]*)"', client_source))
    check("client uses known commands", used <= commands, ",".join(sorted(used - commands)))

    # 5. the generated script keeps the invariants the docs claim
    check("script exits by itself", "SYSTEM.exit(0)" in source)
    check("script never prints (would pollute IDE messages)",
          not re.search(r"^\s*print\(", source, re.M))
    check("write path uses replace(offset, length, text)",
          "document.replace(0, document.length, text)" in source)
    check("one request per connection", "One request per connection" in source)
    check("task configuration is created for compilable projects",
          "create_task_configuration" in source)

    # 6. quoting helper is used everywhere a process is launched
    check("service uses build_command_line", "build_command_line(" in read(
        os.path.join(SRC, "codesyskit", "service.py")))
    check("cli uses build_command_line", "build_command_line(" in read(
        os.path.join(SRC, "codesyskit", "cli.py")))

    # 7. docs mentioned by README exist
    readme = read(os.path.join(ROOT, "README.md"))
    for name in re.findall(r"(docs/[A-Z\-]+\.md)", readme):
        check("README link %s" % name, os.path.exists(os.path.join(ROOT, name)))

    # 8. no customer identifiers from other projects leaked in
    banned = ["1号机", "申万", "Inovance", "AutoShop", "汇川", "H5U"]
    leaks = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in {".git", "__pycache__", "_runs", ".pytest_cache"}]
        for name in files:
            if not name.endswith((".py", ".md", ".toml", ".json", ".cfg")):
                continue
            path = os.path.join(base, name)
            if os.path.abspath(path) == os.path.abspath(__file__):
                continue
            text = read(path)
            for word in banned:
                if word in text:
                    leaks.append("%s:%s" % (os.path.relpath(path, ROOT), word))
    check("no foreign project identifiers", not leaks, "; ".join(leaks[:3]))

    # 9. tests exist and the live test skips without CODESYS
    tests = sorted(name for name in os.listdir(os.path.join(ROOT, "tests"))
                   if name.startswith("test_") and name.endswith(".py"))
    check("unit tests present", len(tests) >= 4, ",".join(tests))
    live = read(os.path.join(ROOT, "tests", "live_service.py"))
    check("live test skips without CODESYS", "[SKIP]" in live)

    # 10. every python file parses
    bad = []
    for base, dirs, files in os.walk(os.path.join(ROOT, "src")):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        for name in files:
            if name.endswith(".py"):
                path = os.path.join(base, name)
                try:
                    ast.parse(read(path))
                except SyntaxError as exc:
                    bad.append("%s:%s" % (os.path.relpath(path, ROOT), exc))
    check("source parses", not bad, "; ".join(bad[:3]))

    print("")
    if FAILURES:
        print("selfcheck: %d failure(s)" % len(FAILURES))
        return 1
    print("selfcheck: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
