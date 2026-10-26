"""Command line: ``codesyskit start|stop|status|call|ping|devices|batch|run|server-script``.

Every verb prints one JSON object and exits with a stable code (see :mod:`codesyskit.errors`):

    0 OK · 1 error · 2 unavailable (no CODESYS / feature off) · 3 timeout · 4 auth
"""

import argparse
import json
import os
import socket
import subprocess
import sys
import time

from . import errors, protocol
from .client import CodesysClient
from .service import Service, build_command_line, DEFAULT_EXE, DEFAULT_PROFILE


def emit(payload, code=errors.CLI_OK):
    print(json.dumps(payload, ensure_ascii=False, indent=1, default=str))
    return code


def exit_code_for(exc):
    mapping = {
        errors.E_TIMEOUT: errors.CLI_TIMEOUT,
        errors.E_TOKEN: errors.CLI_AUTH,
        errors.E_UNAVAILABLE: errors.CLI_UNAVAILABLE,
    }
    return mapping.get(getattr(exc, "code", ""), errors.CLI_ERROR)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="codesyskit",
                                     description="Resident CODESYS service for agents")
    parser.add_argument("--state-dir", default=None, help="where service.json lives")
    parser.add_argument("--exe", default=None, help="CODESYS.exe (default %s)" % DEFAULT_EXE)
    parser.add_argument("--profile", default=None, help="CODESYS profile name")
    sub = parser.add_subparsers(dest="verb", required=True)

    start = sub.add_parser("start", help="start the resident service")
    start.add_argument("--port", type=int, default=0, help="0 = let CODESYS pick a free port")
    start.add_argument("--allow-exec", action="store_true", help="enable the exec command")
    start.add_argument("--wait", type=float, default=180.0)

    sub.add_parser("stop", help="stop the service (quit, then kill if needed)")
    sub.add_parser("status", help="is a service running, and what does it report")

    call = sub.add_parser("call", help="run one command")
    call.add_argument("cmd")
    call.add_argument("--args", default="{}", help="json object with the command arguments")
    call.add_argument("--timeout", type=float, default=120.0)

    ping = sub.add_parser("ping", help="round trip check")
    ping.add_argument("--timeout", type=float, default=30.0)

    devices = sub.add_parser("devices", help="list device descriptions")
    devices.add_argument("--filter", default=None)
    devices.add_argument("--limit", type=int, default=20)

    cmds = sub.add_parser("commands", help="list IDE commands")
    cmds.add_argument("--filter", default=None)
    cmds.add_argument("--limit", type=int, default=20)

    execute = sub.add_parser("execute", help="run one IDE command and judge it from the engine log")
    execute.add_argument("name_or_guid")
    execute.add_argument("--timeout", type=float, default=600.0)

    find = sub.add_parser("find", help="search declarations and implementations")
    find.add_argument("pattern")
    find.add_argument("--case-sensitive", action="store_true")
    find.add_argument("--part", default="both", choices=["both", "declaration", "implementation"])
    find.add_argument("--limit", type=int, default=200)

    sub.add_parser("libs", help="list referenced and available libraries")
    lib_add = sub.add_parser("add-lib", help="reference a library by name")
    lib_add.add_argument("name")

    export_xml = sub.add_parser("export-xml", help="PLCopenXML export (default: active application)")
    export_xml.add_argument("path")
    export_xml.add_argument("--target", default=None)

    import_xml = sub.add_parser("import-xml", help="PLCopenXML import into the open project")
    import_xml.add_argument("path")

    archive = sub.add_parser("archive", help="save the whole project as an archive")
    archive.add_argument("path")

    sim = sub.add_parser("sim", help="enable/disable the device simulation mode (no gateway needed)")
    sim.add_argument("--off", action="store_true")
    sim.add_argument("--state", action="store_true")

    login = sub.add_parser("online-login", help="log in (simulation by default)")
    login.add_argument("--no-simulation", action="store_true")
    login.add_argument("--change-option", default="never", choices=["never", "update", "ask"])
    login.add_argument("--autostart", action="store_true")

    sub.add_parser("online-state", help="login-independent online snapshot")
    sub.add_parser("online-start", help="log in and start the application")
    sub.add_parser("online-stop", help="log in and stop the application")
    sub.add_parser("online-logout", help="log out")
    sub.add_parser("download", help="download (login with change_option=update) + boot application")

    read = sub.add_parser("online-read", help="read one or more expressions")
    read.add_argument("expressions", nargs="+")

    write = sub.add_parser("online-write", help="prepare, write and read back one expression")
    write.add_argument("expression")
    write.add_argument("value")

    monitor = sub.add_parser("online-monitor", help="sample expressions over time")
    monitor.add_argument("expressions", nargs="+")
    monitor.add_argument("--samples", type=int, default=5)
    monitor.add_argument("--interval-ms", type=int, default=500)

    sub.add_parser("clean", help="clean generated code")
    sub.add_parser("generate", help="generate code")
    sub.add_parser("app-status", help="application flags (active/uptodate/online-change)")

    save_as = sub.add_parser("save-as", help="save the project under a new path")
    save_as.add_argument("path")

    info = sub.add_parser("proj-info", help="read or write project information")
    info.add_argument("--title")
    info.add_argument("--company")
    info.add_argument("--version")
    info.add_argument("--author")

    library = sub.add_parser("export-library", help="save as a compiled library")
    library.add_argument("path")
    library.add_argument("--title")
    library.add_argument("--version")

    members = sub.add_parser("members", help="list members (methods/properties/actions)")
    members.add_argument("path")

    symbols = sub.add_parser("symbols", help="create or inspect a symbol configuration")
    symbols.add_argument("--create", action="store_true")
    symbols.add_argument("--path", default="")
    symbols.add_argument("--opc-ua", action="store_true")

    textlist = sub.add_parser("textlist", help="create a text list or manage its languages")
    textlist.add_argument("--create", action="store_true")
    textlist.add_argument("--path", default="")
    textlist.add_argument("--languages", nargs="*")
    textlist.add_argument("--add-language")
    textlist.add_argument("--out")

    task = sub.add_parser("task", help="read or update a task configuration")
    task.add_argument("path")
    task.add_argument("--priority")
    task.add_argument("--interval")
    task.add_argument("--interval-unit")
    task.add_argument("--watchdog-time")

    force = sub.add_parser("force", help="force an expression (simulation)")
    force.add_argument("expression")
    force.add_argument("value")
    sub.add_parser("unforce", help="release all forced expressions")
    sub.add_parser("forced", help="list forced and prepared expressions")

    io_export = sub.add_parser("io-export", help="export device I/O mappings as CSV")
    io_export.add_argument("path")
    io_export.add_argument("--device", default=None)

    batch = sub.add_parser("batch", help="run several commands in one request")
    batch.add_argument("--file", required=True, help="json file with [{\"cmd\":..,\"args\":{}}]")

    run = sub.add_parser("run", help="one-shot: run a script with --runscript and exit")
    run.add_argument("script")
    run.add_argument("--timeout", type=float, default=900.0)

    script = sub.add_parser("server-script", help="print the generated in-IDE server script")
    script.add_argument("--out", default=None)

    args = parser.parse_args(argv)

    if args.verb == "server-script":
        import secrets

        service = Service(exe=args.exe, profile=args.profile, directory=args.state_dir)
        source = __import__("codesyskit.agentscript", fromlist=["render"]).render(
            token=secrets.token_hex(16), port=0,
            state_file=service.state_path, log_file=service.log_path,
            allow_exec=getattr(args, "allow_exec", False))
        if args.out:
            with open(args.out, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(source)
            return emit({"written": args.out, "bytes": len(source)})
        sys.stdout.write(source)
        return errors.CLI_OK

    if args.verb == "run":
        exe = args.exe or os.environ.get("CODESYSKIT_EXE") or DEFAULT_EXE
        profile = args.profile or os.environ.get("CODESYSKIT_PROFILE") or DEFAULT_PROFILE
        if not os.path.exists(args.script):
            return emit({"error": "no such script: %s" % args.script}, errors.CLI_ERROR)
        started = time.time()
        result = subprocess.run(build_command_line(exe, profile, args.script),
                                shell=False, capture_output=True, text=True, encoding="utf-8",
                                errors="replace", timeout=args.timeout)
        return emit({"exit_code": result.returncode, "seconds": round(time.time() - started, 2),
                     "stdout": (result.stdout or "")[-4000:],
                     "stderr": (result.stderr or "")[-4000:]},
                    errors.CLI_OK if result.returncode == 0 else errors.CLI_ERROR)

    service = Service(exe=args.exe, profile=args.profile, directory=args.state_dir)

    try:
        if args.verb == "start":
            state = service.start(wait=args.wait, token=None)
            if args.allow_exec:
                # restart with exec enabled: the flag is baked into the script
                service.stop()
                service = Service(exe=args.exe, profile=args.profile,
                                  directory=args.state_dir, allow_exec=True)
                state = service.start(wait=args.wait)
            return emit(state)
        if args.verb == "stop":
            return emit(service.stop())
        if args.verb == "status":
            if not service.is_alive():
                return emit({"running": False, "state_path": service.state_path},
                            errors.CLI_UNAVAILABLE)
            state = service.state()
            client = service.client(timeout=15.0)
            try:
                state["ping"] = client.ping()
            finally:
                client.close()
            state["running"] = True
            return emit(state)
        if args.verb == "ping":
            client = service.client(timeout=args.timeout)
            try:
                return emit(client.ping())
            finally:
                client.close()
        if args.verb == "devices":
            client = service.client()
            try:
                return emit(client.devices(filter=args.filter, limit=args.limit))
            finally:
                client.close()
        if args.verb == "call":
            payload = json.loads(args.args)
            client = service.client(timeout=args.timeout)
            try:
                return emit(client.call(args.cmd, **payload))
            finally:
                client.close()
        if args.verb == "commands":
            client = service.client()
            try:
                return emit(client.commands(filter=args.filter, limit=args.limit))
            finally:
                client.close()
        if args.verb == "execute":
            result = service.run_command(client=service.client(timeout=args.timeout),
                                         name_or_guid=args.name_or_guid,
                                         timeout_ms=int(args.timeout * 1000))
            return emit(result, errors.CLI_OK if result["ok"] else errors.CLI_ERROR)
        if args.verb == "find":
            client = service.client()
            try:
                return emit(client.find(args.pattern, case_sensitive=args.case_sensitive,
                                        part=args.part, limit=args.limit))
            finally:
                client.close()
        if args.verb == "libs":
            client = service.client()
            try:
                return emit(client.libraries())
            finally:
                client.close()
        if args.verb == "add-lib":
            client = service.client()
            try:
                return emit(client.add_library(args.name))
            finally:
                client.close()
        if args.verb == "export-xml":
            client = service.client()
            try:
                return emit(client.export_xml(args.path, target=args.target))
            finally:
                client.close()
        if args.verb == "import-xml":
            client = service.client()
            try:
                return emit(client.import_xml(args.path))
            finally:
                client.close()
        if args.verb == "archive":
            client = service.client()
            try:
                return emit(client.archive(args.path))
            finally:
                client.close()
        if args.verb == "sim":
            client = service.client()
            try:
                if args.state:
                    return emit({"simulation": client.online_state().get("simulation")})
                return emit(client.online_simulation(None if not args.off else False))
            finally:
                client.close()
        if args.verb == "online-login":
            client = service.client()
            try:
                return emit(client.online_login(
                    simulation=not args.no_simulation, change_option=args.change_option,
                    autostart=args.autostart))
            finally:
                client.close()
        if args.verb == "online-state":
            client = service.client()
            try:
                return emit(client.online_state())
            finally:
                client.close()
        if args.verb == "online-start":
            client = service.client()
            try:
                return emit(client.online_start())
            finally:
                client.close()
        if args.verb == "online-stop":
            client = service.client()
            try:
                return emit(client.online_stop())
            finally:
                client.close()
        if args.verb == "online-logout":
            client = service.client()
            try:
                return emit(client.online_logout())
            finally:
                client.close()
        if args.verb == "download":
            client = service.client(timeout=600.0)
            try:
                return emit(client.online_download())
            finally:
                client.close()
        if args.verb == "online-read":
            client = service.client()
            try:
                return emit(client.online_read(expressions=args.expressions))
            finally:
                client.close()
        if args.verb == "online-write":
            client = service.client()
            try:
                return emit(client.online_write(args.expression, args.value))
            finally:
                client.close()
        if args.verb == "online-monitor":
            client = service.client(timeout=600.0)
            try:
                return emit(client.online_monitor(expressions=args.expressions,
                                                 samples=args.samples,
                                                 interval_ms=args.interval_ms))
            finally:
                client.close()
        if args.verb in ("clean", "generate", "app-status", "forced", "unforce"):
            client = service.client()
            try:
                if args.verb == "clean":
                    return emit(client.app_clean())
                if args.verb == "generate":
                    return emit(client.app_generate())
                if args.verb == "app-status":
                    return emit(client.app_status())
                if args.verb == "forced":
                    return emit(client.online_forced())
                return emit(client.online_unforce())
            finally:
                client.close()
        if args.verb == "save-as":
            client = service.client(timeout=600.0)
            try:
                return emit(client.save_as(args.path))
            finally:
                client.close()
        if args.verb == "proj-info":
            client = service.client()
            try:
                return emit(client.project_meta(title=args.title, company=args.company,
                                                version=args.version, author=args.author))
            finally:
                client.close()
        if args.verb == "export-library":
            client = service.client(timeout=600.0)
            try:
                return emit(client.export_library(args.path, title=args.title,
                                                  version=args.version))
            finally:
                client.close()
        if args.verb == "members":
            client = service.client()
            try:
                return emit(client.members(args.path))
            finally:
                client.close()
        if args.verb == "symbols":
            client = service.client()
            try:
                if args.create:
                    return emit(client.symbols_create(opc_ua=args.opc_ua))
                return emit(client.symbols_info(args.path))
            finally:
                client.close()
        if args.verb == "textlist":
            client = service.client()
            try:
                if args.create:
                    return emit(client.textlist_create(languages=args.languages))
                if args.out:
                    return emit(client.textlist_export(args.path, args.out))
                return emit(client.textlist_languages(args.path, add=args.add_language))
            finally:
                client.close()
        if args.verb == "task":
            client = service.client()
            try:
                if any([args.priority, args.interval, args.interval_unit, args.watchdog_time]):
                    return emit(client.task_update(args.path, priority=args.priority,
                                                   interval=args.interval,
                                                   interval_unit=args.interval_unit,
                                                   watchdog_time=args.watchdog_time))
                return emit(client.task_info(args.path))
            finally:
                client.close()
        if args.verb == "force":
            client = service.client()
            try:
                return emit(client.online_force(args.expression, args.value))
            finally:
                client.close()
        if args.verb == "io-export":
            client = service.client()
            try:
                return emit(client.io_export(args.path, device=args.device))
            finally:
                client.close()
        if args.verb == "batch":
            with open(args.file, "r", encoding="utf-8") as handle:
                calls = json.load(handle)
            client = service.client()
            try:
                return emit(client.batch(calls))
            finally:
                client.close()
    except protocol.ServiceError as exc:
        return emit({"ok": False, "code": exc.code, "message": exc.message,
                     "detail": exc.detail}, exit_code_for(exc))
    except (socket.timeout, ConnectionError, OSError):
        return emit({"ok": False, "code": errors.E_PROTOCOL,
                     "message": "no service on the recorded port"}, errors.CLI_ERROR)
    return emit({"error": "unhandled verb"}, errors.CLI_INTERNAL)


if __name__ == "__main__":
    sys.exit(main())
