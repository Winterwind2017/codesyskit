"""Live online test: simulation mode, login, download, run/stop, read/write, monitoring.

Needs CODESYS 3.5 (no gateway, no PLC, no admin: the device's simulation mode hosts the runtime).

    python tests/live_online.py
"""

import argparse
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from codesyskit import errors, protocol
from codesyskit.service import Service, DEFAULT_EXE

WORK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_runs", "online")
RESULTS = []

DECL = "PROGRAM PLC_PRG\nVAR\n\tnCounter : INT;\n\tnFlag : BOOL;\nEND_VAR\n"
IMPL = "nCounter := nCounter + 1;\n"


def step(name, func):
    started = time.time()
    try:
        value = func()
        print("[PASS] %-50s %6.2fs  %s" % (name, time.time() - started, str(value)[:140]))
        RESULTS.append((name, True))
        return value
    except Exception as exc:  # noqa: BLE001
        print("[FAIL] %-50s %6.2fs  %s: %s" % (name, time.time() - started,
                                               type(exc).__name__, str(exc)[:240]))
        RESULTS.append((name, False))
        return None


def to_int(text):
    """'INT#9' -> 9 (the engine renders typed values)."""
    if text is None:
        return None
    digits = "".join(ch for ch in str(text) if ch.isdigit() or ch == "-")
    return int(digits) if digits not in ("", "-") else None


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
    if not step("service.start", lambda: service.start(wait=240)):
        return 1
    client = service.client(timeout=600.0)
    try:
        project_path = os.path.join(WORK, "online.project")
        created = step("project.create(+device+task)",
                       lambda: client.create(project_path, device="CODESYS Control Win V3"))
        pou = (created or {}).get("program")
        client.write(pou, DECL, "declaration")
        client.write(pou, IMPL, "implementation")
        compiled = step("compile", lambda: service.compile(client))
        if compiled:
            assert compiled["ok"], compiled["messages"][:3]

        step("online.simulation(True)", lambda: client.online_simulation(True))
        state = step("online.state after enabling simulation", lambda: client.online_state())
        if state:
            assert state["simulation"] is True, state

        login = step("online.login(autostart=True)",
                     lambda: client.online_login(autostart=True))
        if login:
            print("      %s" % {k: login.get(k) for k in
                                ("logged_in", "application_state", "operation_state",
                                 "gateway", "address")})
            assert login["logged_in"] is True, login
            assert login["application_state"] == "run", login

        # the counter is incremented by the cyclic task: two samples must differ
        def counter_grows():
            first = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            time.sleep(1.2)
            second = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            return {"first": first, "second": second, "grew": second > first}

        growth = step("monitor: the task really runs (counter grows)", counter_grows)
        if growth:
            assert growth["grew"], growth

        def write_and_read():
            client.online_write("PLC_PRG.nCounter", "1000")
            value = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            return {"value": value, "accepted": value is not None and value >= 1000}

        written = step("online.write(1000) + readback", write_and_read)
        if written:
            assert written["accepted"], written

        series = step("online.monitor(5 samples / 300 ms)",
                      lambda: client.online_monitor(expressions=["PLC_PRG.nCounter"],
                                                    samples=5, interval_ms=300))
        if series:
            values = [to_int(row["PLC_PRG.nCounter"]) for row in series["samples"]]
            print("      samples: %s" % values)
            assert len(values) == 5 and all(v is not None for v in values)

        stepped = step("online.stop()", lambda: client.online_stop())
        if stepped:
            assert stepped["application_state"] == "stop", stepped
        step("online.start()", lambda: client.online_start())

        download = step("online.download() (change option update + boot application)",
                        lambda: client.online_download())
        if download:
            print("      boot_application=%r state=%s" % (download.get("boot_application"),
                                                          download.get("application_state")))

        step("online.logout()", lambda: client.online_logout())
        step("online.simulation(False)", lambda: client.online_simulation(False))

        # the failure path must stay honest: without simulation and without a gateway it fails
        def login_without_gateway():
            client.online_simulation(False)
            try:
                client.online_login(simulation=False)
            except protocol.ServiceError as exc:
                return exc.code
            finally:
                client.online_simulation(True)
            raise AssertionError("a gateway-less login succeeded")

        step("online.login without gateway -> E_CODESYS", login_without_gateway)
    finally:
        client.close()
        if not args.keep:
            step("service.stop", service.stop)

    passed = sum(1 for _name, ok in RESULTS if ok)
    print("\n%d/%d passed" % (passed, len(RESULTS)))
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
