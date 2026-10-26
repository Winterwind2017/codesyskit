"""A Python 3 stand-in for the in-IDE service, so the client can be tested without CODESYS.

It speaks the same wire protocol and implements the commands the tests need.
"""

import json
import socket
import threading
import time

from codesyskit import errors, protocol


class FakeService:
    def __init__(self, token="t" * 32, port=0):
        self.token = token
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind(("127.0.0.1", port))
        self.port = self._server.getsockname()[1]
        self._server.listen(8)
        self._stop = threading.Event()
        self._thread = None
        self.calls = []

    # -- lifecycle ---------------------------------------------------------
    def start(self):
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()
        return self

    def stop(self):
        self._stop.set()
        try:
            self._server.close()
        except OSError:
            pass
        if self._thread:
            self._thread.join(timeout=2)

    # -- protocol ----------------------------------------------------------
    def _serve(self):
        while not self._stop.is_set():
            try:
                client, _ = self._server.accept()
            except OSError:
                return
            threading.Thread(target=self._handle, args=(client,), daemon=True).start()

    def _handle(self, client):
        reader = client.makefile("rb")
        try:
            for line in reader:
                if not line.strip():
                    continue
                payload = self.dispatch(line)
                client.sendall((json.dumps(payload) + "\n").encode("utf-8"))
        finally:
            try:
                client.close()
            except OSError:
                pass

    def dispatch(self, line):
        started = time.time()
        try:
            request = protocol.decode_request(line)
        except protocol.ProtocolError as exc:
            return protocol.error_response(None, exc.code, exc.message)
        self.calls.append(request.get("cmd"))
        request_id = request.get("id")
        if request.get("token") != self.token:
            return protocol.error_response(request_id, errors.E_TOKEN, "bad or missing token")
        cmd = request.get("cmd")
        args = request.get("args") or {}
        try:
            result = self._run(cmd, args)
        except KeyError:
            return protocol.error_response(request_id, errors.E_UNKNOWN_CMD,
                                           "unknown command %r" % (cmd,))
        except ValueError as exc:
            return protocol.error_response(request_id, errors.E_ARGS, str(exc))
        except _Slow as exc:
            time.sleep(exc.seconds)
            result = {"slept": exc.seconds}
        except RuntimeError as exc:
            return protocol.error_response(request_id, errors.E_SCRIPT, str(exc), "trace")
        elapsed = int((time.time() - started) * 1000)
        return protocol.ok_response(request_id, result, elapsed)

    def _run(self, cmd, args):
        if cmd == "ping":
            return {"protocol": protocol.PROTOCOL_VERSION, "banner": "fake", "ui_present": False,
                    "pid": 1, "uptime_s": 1.0}
        if cmd == "echo":
            return {"echo": args}
        if cmd == "slow":
            raise _Slow(float(args.get("seconds", 1.0)))
        if cmd == "fail":
            raise RuntimeError("boom")
        if cmd == "needs_arg":
            if "value" not in args:
                raise ValueError("needs_arg needs 'value'")
            return {"value": args["value"]}
        if cmd == "batch":
            calls = args.get("calls") or []
            results = []
            for index, call in enumerate(calls):
                entry = {"index": index, "cmd": call.get("cmd")}
                try:
                    entry.update({"ok": True, "code": "OK",
                                  "result": self._run(call.get("cmd"), call.get("args") or {})})
                except Exception as exc:  # noqa: BLE001
                    entry.update({"ok": False, "code": errors.E_SCRIPT, "error": str(exc)})
                results.append(entry)
            return {"results": results, "executed": len(results)}
        if cmd == "quit":
            return {"bye": True}
        raise KeyError(cmd)


class _Slow(Exception):
    def __init__(self, seconds):
        Exception.__init__(self, "slow")
        self.seconds = seconds
