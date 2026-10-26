"""Live test of the extended surface: IDE commands, structure edits, libraries, exchange, online.

Needs CODESYS 3.5; skips cleanly when it is not installed.

    python tests/live_surface.py
"""

import argparse
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from codesyskit import errors, protocol
from codesyskit.service import Service, DEFAULT_EXE

WORK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_runs", "surface")
RESULTS = []

DECL = "PROGRAM PLC_PRG\nVAR\n\tnCounter : INT;\nEND_VAR\n"
IMPL = "nCounter := nCounter + 1;\n"


def step(name, func):
    started = time.time()
    try:
        value = func()
        print("[PASS] %-48s %6.2fs  %s" % (name, time.time() - started, str(value)[:130]))
        RESULTS.append((name, True))
        return value
    except Exception as exc:  # noqa: BLE001
        print("[FAIL] %-48s %6.2fs  %s: %s" % (name, time.time() - started,
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
    client = service.client(timeout=600.0)
    try:
        project_path = os.path.join(WORK, "surface.project")
        created = step("project.create(+device+task)",
                       lambda: client.create(project_path, device="CODESYS Control Win V3"))
        pou = (created or {}).get("program")
        application = (client.info() or {}).get("application", {}).get("path")
        client.write(pou, DECL, "declaration")
        client.write(pou, IMPL, "implementation")

        # ---- IDE commands -------------------------------------------------
        listing = step("commands (all)", lambda: client.commands())
        if listing:
            print("      %d commands" % listing["count"])
        filtered = step("commands --filter 编译", lambda: client.commands(filter="编译", limit=10))
        if filtered:
            print("      %s" % [item["name"] for item in filtered["items"]][:6])

        rebuilt = step("execute 重新编译 (judged from engine log)",
                       lambda: service.run_command(client, "重新编译"))
        if rebuilt:
            print("      errors=%s warnings=%s" % (rebuilt["errors"], rebuilt["warnings"]))
            assert rebuilt["errors"] == 0, rebuilt["messages"][:3]

        # ---- structure ----------------------------------------------------
        step("object.info", lambda: client.object_info(pou)["name"])
        step("folder.create Records", lambda: client.mkdir("Records", application)["name"])

        def move_rename_delete():
            folder = client.mkdir("Temp", application)["path"]
            moved = client.move(pou, folder, -1)["path"]
            renamed = client.rename(moved, "PLC_MAIN")["path"]
            info = client.object_info(renamed)
            back = client.move(renamed, application, -1)["path"]
            client.rename(back, "PLC_PRG")
            client.delete(folder)
            return {"moved_ok": info["name"] == "PLC_MAIN",
                    "restored": client.object_info(pou)["name"]}

        step("move/rename/delete round trip", move_rename_delete)

        def unicode_text():
            text = "(* 中文注释：计数器 *)\nnCounter := nCounter + 1;\n"
            client.write(pou, text, "implementation")
            readback = client.read(pou, "implementation")["text"]
            client.write(pou, IMPL, "implementation")
            return {"match": readback == text, "text": readback[:30]}

        step("utf-8 text round trip (Chinese)", unicode_text)

        # ---- search -------------------------------------------------------
        found = step("find.text", lambda: client.find("nCounter", limit=10))
        if found:
            print("      %d hits: %s" % (found["count"],
                                         [(item["path"], item["line"]) for item in found["items"]][:3]))

        # ---- libraries ----------------------------------------------------
        libs = step("libraries", lambda: client.libraries())
        if libs:
            print("      referenced=%s available=%s" % (libs["referenced_count"],
                                                        libs["available_count"]))
        added = step("library.add(Standard)", lambda: client.add_library("Standard"))
        if added:
            assert "Standard" in added["referenced"], added["referenced"]

        # ---- exchange -----------------------------------------------------
        xml_path = os.path.join(WORK, "export.xml")
        exported = step("export.xml", lambda: client.export_xml(xml_path))
        if exported:
            assert exported["size"] > 0
        device_xml = os.path.join(WORK, "export_device.xml")
        step("export.xml (device subtree)",
             lambda: client.export_xml(device_xml, target="/PLC"))
        native_path = os.path.join(WORK, "export.plcopen")
        step("export.native", lambda: client.export_native(native_path, application))
        archive_path = os.path.join(WORK, "surface.projectarchive")
        archived = step("project.archive", lambda: client.archive(archive_path))
        if archived:
            assert archived["size"] > 0
        def doc_export_is_honest():
            try:
                client.export_doc(os.path.join(WORK, "doc.txt"))
            except protocol.ServiceError as exc:
                assert exc.code == errors.E_UNAVAILABLE, exc.code
                return exc.code
            raise AssertionError("export_doc reported success but wrote nothing")

        step("project.doc -> E_UNAVAILABLE (measured)", doc_export_is_honest)
        runtime_dir = os.path.join(WORK, "rtsys")
        runtime = step("generate.runtime", lambda: client.generate_runtime(runtime_dir))
        if runtime:
            print("      runtime files: %s" % runtime["files"][:5])

        def import_roundtrip():
            target = os.path.join(WORK, "imported.project")
            client.create(target)                      # empty project: no device at all
            before = len(client.info()["children"])
            imported = client.import_xml(device_xml)
            after = len(client.info()["children"])
            client.call("project.close")
            client.open(project_path)
            return {"children_before": before, "children_after": after,
                    "imported": imported}

        step("import.xml (device subtree into an empty project)", import_roundtrip)

        # ---- online (no gateway/PLC on this machine) ----------------------
        online_state = step("online.state", lambda: client.online_state())
        if online_state:
            print("      %s" % online_state)

        def login_should_fail():
            try:
                client.online_login()
            except protocol.ServiceError as exc:
                assert exc.code in (errors.E_CODESYS, errors.E_SCRIPT), exc.code
                return exc.code
            raise AssertionError("login succeeded without a gateway")

        step("online.login -> engine error (no gateway)", login_should_fail)
    finally:
        client.close()
        if not args.keep:
            step("service.stop", service.stop)

    passed = sum(1 for _name, ok in RESULTS if ok)
    print("\n%d/%d passed" % (passed, len(RESULTS)))
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
