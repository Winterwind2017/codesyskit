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
