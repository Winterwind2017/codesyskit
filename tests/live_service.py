"""Live end-to-end test: needs CODESYS 3.5 installed.  Skips cleanly when it is not.

    python tests/live_service.py            # start -> drive -> stop
    python tests/live_service.py --keep     # leave the service running

Judged by read-backs and by the engine's own compiler log, not by return values.
"""

import argparse
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from codesyskit import errors, protocol
from codesyskit.client import CodesysClient
from codesyskit.service import Service, DEFAULT_EXE

WORK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_runs", "live")
RESULTS = []

DECL = "PROGRAM PLC_PRG\nVAR\n\tnCounter : INT;\nEND_VAR\n"
IMPL = "nCounter := nCounter + 1;\n"
BROKEN = "THIS IS NOT ST !!!\n"


def step(name, func):
    started = time.time()
    try:
        value = func()
        print("[PASS] %-46s %6.2fs  %s" % (name, time.time() - started, str(value)[:130]))
        RESULTS.append((name, True))
        return value
    except Exception as exc:  # noqa: BLE001
        print("[FAIL] %-46s %6.2fs  %s: %s" % (name, time.time() - started,
                                               type(exc).__name__, str(exc)[:240]))
        RESULTS.append((name, False))
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--keep", action="store_true")
    parser.add_argument("--exe", default=None)
    args = parser.parse_args()
    if not os.path.exists(args.exe or DEFAULT_EXE):
        print("[SKIP] CODESYS 3.5 not installed (%s)" % (args.exe or DEFAULT_EXE))
        return 0

    if os.path.isdir(WORK):
        shutil.rmtree(WORK)
    os.makedirs(WORK)

    service = Service(exe=args.exe, directory=WORK, port=0)
    state = step("service.start", lambda: service.start(wait=240))
    if not state:
        return 1
    print("      port=%s pid=%s boot=%ss" % (state.get("port"), state.get("pid"),
                                             state.get("boot_s")))

    client = service.client(timeout=300.0)
    try:
        step("ping", lambda: client.ping()["protocol"])
        step("devices", lambda: client.devices(filter="CODESYS Control Win V3", limit=3)["count"])

        project_path = os.path.join(WORK, "live.project")
        created = step("project.create(+device+task)",
                       lambda: client.create(project_path, device="CODESYS Control Win V3"))
        pou_path = (created or {}).get("program")
        if created:
            print("      program=%s task=%s" % (created.get("program"), created.get("task")))

        tasks = step("tasks", lambda: client.call("tasks"))
        if tasks:
            print("      tasks:", [(item["name"], item["pous"]) for item in tasks["items"]])

        step("pou.write(declaration)", lambda: client.write(pou_path, DECL, "declaration"))
        step("pou.write(implementation)", lambda: client.write(pou_path, IMPL, "implementation"))

        clean = step("compile(valid code) -> 0 errors", lambda: service.compile(client))
        if clean:
            print("      errors=%s warnings=%s summary=%s" % (clean["errors"], clean["warnings"],
                                                              clean["summary"]))

        def compile_broken():
            client.write(pou_path, BROKEN, "implementation")
            parsed = service.compile(client)
            client.write(pou_path, IMPL, "implementation")
            return {"errors": parsed["errors"], "warnings": parsed["warnings"],
                    "codes": [item["code"] for item in parsed["messages"]][:5],
                    "first": (parsed["messages"][0]["text"][:60] if parsed["messages"] else None)}

        broken = step("compile(garbage) -> errors > 0", compile_broken)
        if broken:
            print("      errors=%s codes=%s" % (broken["errors"], broken["codes"]))
            assert broken["errors"] > 0, "the compiler accepted garbage code"
            assert broken["codes"], "no diagnostic codes were parsed"

        restored = step("compile(restored) -> 0 errors", lambda: service.compile(client))
        if restored:
            assert restored["ok"], restored["messages"][:3]

        step("project.save", client.save)

        def reopen_and_check():
            client.call("project.close")
            client.open(project_path)
            readback = client.read(pou_path, "implementation")
            client.call("project.close")
            return {"matches": readback["text"] == IMPL, "text": readback["text"]}

        step("reopen + read back", reopen_and_check)

        # the trap this kit exists to avoid: no task configuration => build compiles nothing
        def bare_project():
            bare_path = os.path.join(WORK, "bare.project")
            client.create(bare_path, device="CODESYS Control Win V3", bare=True)
            application = client.info()["application"]["path"]
            client.create_pou("PLC_PRG", "program", parent=application)
            client.write(application + "/PLC_PRG", BROKEN, "implementation")
            silent = service.compile(client)
            client.call("project.close")
            return {"errors": silent["errors"], "summary": silent["summary"],
                    "messages": len(silent["messages"])}

        bare = step("bare project compiles nothing (documented trap)", bare_project)
        if bare:
            print("      bare build: errors=%s summary=%s" % (bare["errors"], bare["summary"]))

        def bad_token():
            state_now = service.state()
            probe = CodesysClient(port=state_now["port"], token="deadbeef" * 4, timeout=10.0)
            try:
                probe.ping()
            except protocol.ServiceError as exc:
                assert exc.code == errors.E_TOKEN, exc.code
                return exc.code
            finally:
                probe.close()
            raise AssertionError("a bad token was accepted")

        step("bad token -> E_TOKEN", bad_token)

        def unknown():
            try:
                client.call("does.not.exist")
            except protocol.ServiceError as exc:
                assert exc.code == errors.E_UNKNOWN_CMD, exc.code
                return exc.code
            raise AssertionError("an unknown command was accepted")

        step("unknown command -> E_UNKNOWN_CMD", unknown)
    finally:
        client.close()
        if not args.keep:
            step("service.stop", service.stop)

    passed = sum(1 for _name, ok in RESULTS if ok)
    print("\n%d/%d passed" % (passed, len(RESULTS)))
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
