"""Live test of the deep surface: IEC object model, symbol config, text lists, tasks,
project information/compiled library, code generation, forcing.

    python tests/live_deep.py
"""

import argparse
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from codesyskit import errors, protocol
from codesyskit.service import Service, DEFAULT_EXE

WORK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_runs", "deep")
RESULTS = []

DECL = "PROGRAM PLC_PRG\nVAR\n\tnCounter : INT;\nEND_VAR\n"
IMPL = "nCounter := nCounter + 1;\n"
FB_TEXT = ("FUNCTION_BLOCK FB_Motor\nVAR_INPUT\n\tbStart : BOOL;\nEND_VAR\n"
           "VAR_OUTPUT\n\tbRun : BOOL;\nEND_VAR\n")
GVL_TEXT = "VAR_GLOBAL\n\tnGlobal : INT;\nEND_VAR\n"
DUT_TEXT = "TYPE ST_Data :\nSTRUCT\n\tnX : INT;\nEND_STRUCT\nEND_TYPE\n"


def step(name, func):
    started = time.time()
    try:
        value = func()
        print("[PASS] %-52s %6.2fs  %s" % (name, time.time() - started, str(value)[:140]))
        RESULTS.append((name, True))
        return value
    except Exception as exc:  # noqa: BLE001
        print("[FAIL] %-52s %6.2fs  %s: %s" % (name, time.time() - started,
                                               type(exc).__name__, str(exc)[:240]))
        RESULTS.append((name, False))
        return None


def to_int(text):
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
        project_path = os.path.join(WORK, "deep.project")
        created = step("project.create(+device+task)",
                       lambda: client.create(project_path, device="CODESYS Control Win V3"))
        pou = (created or {}).get("program")
        application = (client.info() or {}).get("application", {}).get("path")
        client.write(pou, DECL, "declaration")
        client.write(pou, IMPL, "implementation")
        task_listing = client.tasks() or {}
        task_items = task_listing.get("items") or []
        task_path = task_items[0]["path"] if task_items else None
        print("      application=%r task=%r" % (application, task_path))

        # ---- save_as (the copy becomes the primary project) --------------
        copy_path = os.path.join(WORK, "deep_copy.project")
        saved = step("project.save_as (copy becomes primary)", lambda: client.save_as(copy_path))
        if saved:
            assert saved["size"] > 0 and saved["children"], saved
            assert saved["is_primary"] is True, saved

        # ---- IEC object model --------------------------------------------
        step("pou.create_typed gvl", lambda: client.create_typed("gvl", "GVL", text=GVL_TEXT))
        step("pou.create_typed dut", lambda: client.create_typed("dut", "ST_Data", text=DUT_TEXT))
        step("pou.create_typed interface",
             lambda: client.create_typed("interface", "I_Run"))
        fb = step("pou.create_typed function_block",
                  lambda: client.create_typed("function_block", "FB_Motor", text=FB_TEXT))
        step("pou.create_typed function (INT)",
             lambda: client.create_typed("function", "F_Add", return_type="INT"))
        fb_path = (fb or {}).get("path") or (application + "/FB_Motor")
        step("pou.member method",
             lambda: client.add_member(fb_path, "method", "Start", return_type="BOOL",
                                       text="bRun := bStart;\n"))
        step("pou.member property",
             lambda: client.add_member(fb_path, "property", "Speed", return_type="INT"))
        step("pou.member action", lambda: client.add_member(fb_path, "action", "Reset"))
        listed = step("pou.members", lambda: client.members(fb_path))
        if listed:
            print("      %d members: %s" % (listed["count"],
                                            [item["name"] for item in listed["items"]][:6]))

        compiled = step("compile after code generation", lambda: service.compile(client))
        if compiled:
            assert compiled["ok"], compiled["messages"][:4]

        # ---- tasks --------------------------------------------------------
        info = step("task.info", lambda: client.task_info(task_path))
        if info:
            print("      priority=%r interval=%r unit=%r" % (info["priority"], info["interval"],
                                                            info["interval_unit"]))
        updated = step("task.update(priority=20, interval=10)",
                       lambda: client.task_update(task_path, priority="20", interval="10"))
        if updated:
            assert updated["priority"] == "20", updated["priority"]
            assert to_int(updated["interval"]) == 10, updated["interval"]

        # ---- persistent variables / text content / permissions ------------
        step("pou.persistent",
             lambda: client.create_persistent("PersistentVars"))

        def permission_audit():
            result = client.project_permissions("仿真", group="Owner")
            return {"guid": result["command_guid"], "permitted": result.get("permitted"),
                    "groups": result["groups"]}

        audited = step("project.permissions(仿真, Owner)", permission_audit)
        if audited:
            assert audited["permitted"] is True, audited

        # ---- symbol configuration ----------------------------------------
        symbols = step("symbols.create", lambda: client.symbols_create(export_comments=True))
        symbols_path = (symbols or {}).get("path")
        s_info = step("symbols.info", lambda: client.symbols_info(symbols_path))
        if s_info:
            print("      datatypes=%d signatures=%d" % (len(s_info.get("datatypes") or []),
                                                        len(s_info.get("signatures") or [])))

        # ---- text lists ---------------------------------------------------
        texts = step("textlist.create(zh-CN, en)",
                     lambda: client.textlist_create("Texts", languages=["zh-CN", "en"]))
        text_path = (texts or {}).get("path")
        more = step("textlist.languages(add=fr)",
                    lambda: client.textlist_languages(text_path, add="fr"))
        if more:
            assert more["count"] == 3, more
        rows = step("textlist.rows", lambda: client.textlist_rows(text_path))
        if rows:
            print("      rows=%d ids=%s" % (rows["count"],
                                            [item["id"] for item in rows["items"]][:2]))
        if rows and rows["items"]:
            first_id = rows["items"][0]["id"]

            def write_texts():
                client.textlist_text(text_path, "Counter label", text_id=first_id)
                client.textlist_text(text_path, "计数器", text_id=first_id, language="zh-CN")
                after = client.textlist_rows(text_path)
                return {"default": after["items"][0]["default"]}

            written_texts = step("textlist.text (default + zh-CN)", write_texts)
            if written_texts:
                assert written_texts["default"] == "Counter label", written_texts

        exported = step("textlist.export",
                        lambda: client.textlist_export(text_path,
                                                       os.path.join(WORK, "texts.xml")))
        if exported:
            assert exported["exists"] and exported["size"] > 0, exported

        # ---- project information / compiled library -----------------------
        changed = step("project.meta(title/version/company)",
                       lambda: client.project_meta(title="DemoKit", version="1.0.0.0",
                                                   company="Winterwind"))
        if changed:
            assert changed["has_project_info"] is True, changed
            assert changed["changed"]["title"] == "DemoKit", changed
        library = step("export_library",
                       lambda: client.export_library(os.path.join(WORK, "DemoKit.compiled-library")))
        if library:
            assert library["size"] > 0, library

        # ---- io mapping ---------------------------------------------------
        io_csv = step("project.io_export (CSV)",
                      lambda: client.io_export(os.path.join(WORK, "io.csv")))
        if io_csv:
            assert io_csv["exists"] and io_csv["size"] > 0, io_csv

        # ---- library round trip: export -> install ------------------------
        def library_roundtrip():
            installed = client.install_library(library["path"])
            return {"before": installed["before"], "after": installed["after"]}

        step("library.install (our own compiled library)", library_roundtrip)

        # ---- user management / integrity ---------------------------------
        users = step("project.users (+ create user/group)",
                     lambda: client.project_users(add_user="tester", add_group="qa"))
        if users:
            assert users["users"], users
            if "refused" in users:
                print("      creation refused by the engine: %s" % users["refused"][0][:80])
            else:
                assert "tester" in users["users"], users
        integrity = step("project.integrity(enable=True)",
                         lambda: client.project_integrity(enable=True))
        if integrity:
            assert integrity["enabled"] is True, integrity

        # ---- code generation ---------------------------------------------
        cleaned = step("app.clean", lambda: client.app_clean())
        if cleaned:
            assert cleaned["is_uptodate"] is False, cleaned
        step("app.generate", lambda: client.app_generate())
        status = step("app.status", lambda: client.app_status())
        if status:
            assert status["is_active_application"] is True, status

        # ---- forcing in simulation ---------------------------------------
        step("online.simulation(True)", lambda: client.online_simulation(True))
        step("online.login(autostart=True)", lambda: client.online_login(autostart=True))

        def forced_stays():
            client.online_force("PLC_PRG.nCounter", "777")
            first = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            time.sleep(1.0)
            second = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            forced = client.online_forced()
            return {"first": first, "second": second, "pinned": first == second == 777,
                    "forced": forced["forced"]}

        pinned = step("online.force(777): value stays pinned while the task runs", forced_stays)
        if pinned:
            assert pinned["pinned"], pinned
            assert "PLC_PRG.nCounter" in pinned["forced"], pinned

        def unforce_releases():
            client.online_unforce()
            forced = client.online_forced()
            first = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            time.sleep(1.0)
            second = to_int(client.online_read("PLC_PRG.nCounter")["value"])
            return {"forced": forced["forced"], "first": first, "second": second,
                    "released": not forced["forced"] and second > first}

        released = step("online.unforce(): counter runs again", unforce_releases)
        if released:
            assert released["released"], released

        def files_are_unavailable():
            try:
                client.online_files("/")
            except protocol.ServiceError as exc:
                assert exc.code == errors.E_UNAVAILABLE, exc.code
                return exc.code
            raise AssertionError("simulated PLC exposed a file service")

        step("online.files -> E_UNAVAILABLE (simulated target)", files_are_unavailable)
        step("online.logout", lambda: client.online_logout())
        step("online.simulation(False)", lambda: client.online_simulation(False))

        # ---- compare is a measured wall ----------------------------------
        def compare_is_honest():
            try:
                client.compare(project_path)
            except protocol.ServiceError as exc:
                assert exc.code == errors.E_UNAVAILABLE, exc.code
                return exc.code
            raise AssertionError("project.compare claimed success")

        step("project.compare -> E_UNAVAILABLE (measured)", compare_is_honest)


    finally:
        client.close()
        if not args.keep:
            step("service.stop", service.stop)

    passed = sum(1 for _name, ok in RESULTS if ok)
    print("\n%d/%d passed" % (passed, len(RESULTS)))
    return 0 if passed == len(RESULTS) else 1


if __name__ == "__main__":
    sys.exit(main())
