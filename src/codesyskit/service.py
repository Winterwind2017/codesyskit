"""Start / stop / inspect the resident CODESYS service.

The service is one CODESYS process running the generated IronPython server:

    CODESYS.exe --profile="<profile>" --noUI --runscript="<state>/server.py"

It publishes ``service.json`` (port, token, pid, banner) as soon as the socket is bound, which
is what the client and the CLI read.  Port ``0`` asks the engine to pick a free port, so several
services can coexist and nothing has to guess 5601.
"""

import json
import os
import re
import secrets
import subprocess
import time

from . import agentscript, errors, protocol
from .client import CodesysClient, DEFAULT_STATE

DEFAULT_EXE = r"D:\Program Files\CODESYS 3.5.22.20\CODESYS\Common\CODESYS.exe"
DEFAULT_PROFILE = "CODESYS V3.5 SP22 Patch 2"


def build_command_line(exe, profile, script_path):
    """CODESYS needs the profile name wrapped in literal quotes in --noUI mode.

    Measured: passing the profile through ``subprocess`` list form makes the engine print
    ``启动参数 --noUI 模式, 请使用 --profile="profile name" 指定配置文件`` and exit 1.
    """
    return '"%s" --profile="%s" --noUI --runscript="%s"' % (exe, profile, script_path)


def state_dir(explicit=None):
    directory = explicit or os.path.dirname(DEFAULT_STATE)
    os.makedirs(directory, exist_ok=True)
    return directory


class Service:
    def __init__(self, exe=None, profile=None, directory=None, port=0, allow_exec=False,
                 state_path=None):
        self.exe = exe or os.environ.get("CODESYSKIT_EXE") or DEFAULT_EXE
        self.profile = (profile or os.environ.get("CODESYSKIT_PROFILE") or DEFAULT_PROFILE)
        self.directory = state_dir(directory)
        self.port = int(port)
        self.allow_exec = allow_exec
        self.state_path = state_path or os.path.join(self.directory, "service.json")
        self.script_path = os.path.join(self.directory, "server.py")
        self.log_path = os.path.join(self.directory, "service.log")
        self.stderr_path = os.path.join(self.directory, "engine.stderr.log")
        self.process = None
        self._stderr_handle = None

    # -- deployment --------------------------------------------------------
    def write_script(self, token, port):
        source = agentscript.render(token=token, port=port, state_file=self.state_path,
                                    log_file=self.log_path, allow_exec=self.allow_exec)
        with open(self.script_path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(source)
        return self.script_path

    def command_line(self):
        """One command-line *string*, because CODESYS demands literal quotes around the profile.

        Measured: passing ``--profile=<name with spaces>`` through ``subprocess`` list form makes
        the engine print ``启动参数 --noUI 模式, 请使用 --profile="profile name" 指定配置文件`` and
        exit 1 — the engine wants the quotes to survive into its own argv.
        """
        return build_command_line(self.exe, self.profile, self.script_path)

    def argv(self):
        """Readable form for logs and error messages."""
        return [self.exe, '--profile="%s"' % self.profile, "--noUI",
                '--runscript="%s"' % self.script_path]

    # -- lifecycle ---------------------------------------------------------
    def start(self, wait=180.0, token=None, poll=0.4):
        if not os.path.exists(self.exe):
            raise protocol.ServiceError(errors.E_UNAVAILABLE, "CODESYS.exe not found: %s" % self.exe)
        if self.is_alive():
            raise protocol.ServiceError(errors.E_STATE,
                                        "a service is already running (pid %s)"
                                        % self.state().get("pid"))
        if os.path.exists(self.state_path):
            os.remove(self.state_path)
        token = token or secrets.token_hex(16)
        self.write_script(token, self.port)
        started = time.time()
        # The engine writes compiler diagnostics to stderr, not to the message storage
        # (measured: system.get_messages() stays empty while stderr shows C189/C9/C190).
        # Keep them in a file so build results can be judged.
        self._stderr_handle = open(self.stderr_path, "ab")
        self.process = subprocess.Popen(self.command_line(),
                                        stdout=subprocess.DEVNULL,
                                        stderr=self._stderr_handle,
                                        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        deadline = started + wait
        last_error = None
        while time.time() < deadline:
            if os.path.exists(self.state_path):
                try:
                    state = self.state()
                except ValueError:
                    time.sleep(poll)
                    continue
                try:
                    client = CodesysClient(port=state["port"], token=state["token"],
                                           timeout=10.0, state_path=self.state_path)
                    ping = client.ping()
                    client.close()
                    state["ping"] = ping
                    state["boot_s"] = round(time.time() - started, 2)
                    return state
                except protocol.ServiceError as exc:
                    last_error = exc
            if self.process.poll() is not None:
                raise protocol.ServiceError(
                    errors.E_UNAVAILABLE,
                    "CODESYS exited during startup (code %s); see %s"
                    % (self.process.returncode, self.log_path))
            time.sleep(poll)
        raise protocol.ServiceError(errors.E_TIMEOUT,
                                    "service did not answer within %.0fs (%s)"
                                    % (wait, last_error or "no state file"), )

    # -- compiler output ---------------------------------------------------
    MESSAGE_RE = re.compile(r"^(?P<category>[^:]+): (?P<severity>Error|Warning|Text|Fatal)"
                            r": (?P<code>[A-Za-z]*\d*):?\s*(?P<text>.*)$")
    SUMMARY_RE = re.compile(r"编译完成\s*[-—]*\s*(?P<errors>\d+)\s*错误\s*[,，]\s*"
                            r"(?P<warnings>\d+)\s*警告")

    def engine_log_offset(self):
        try:
            return os.path.getsize(self.stderr_path)
        except OSError:
            return 0

    def engine_log_since(self, offset):
        try:
            with open(self.stderr_path, "rb") as handle:
                handle.seek(offset)
                return handle.read().decode("utf-8", "replace")
        except OSError:
            return ""

    @classmethod
    def parse_engine_log(cls, text):
        messages = []
        summary = None
        for line in text.splitlines():
            match = cls.SUMMARY_RE.search(line)
            if match:
                summary = {"errors": int(match.group("errors")),
                           "warnings": int(match.group("warnings"))}
                continue
            match = cls.MESSAGE_RE.match(line.strip())
            if match:
                severity = match.group("severity")
                if severity == "Text":
                    # progress chatter ("开始构建...", "代码典型化..."), not a diagnostic
                    continue
                messages.append({"category": match.group("category").strip(),
                                 "severity": severity,
                                 "code": match.group("code") or None,
                                 "text": match.group("text")})
        errors = sum(1 for item in messages if item["severity"] in ("Error", "Fatal"))
        warnings = sum(1 for item in messages if item["severity"] == "Warning")
        if summary is not None:
            errors = max(errors, summary["errors"])
            warnings = max(warnings, summary["warnings"])
        return {"ok": errors == 0, "errors": errors, "warnings": warnings,
                "summary": summary, "messages": messages}

    def compile(self, client, timeout_ms=600000):
        """Build through the service and judge the result from the engine's own stderr."""
        offset = self.engine_log_offset()
        server_side = client.build(timeout_ms=timeout_ms)
        text = self.engine_log_since(offset)
        parsed = self.parse_engine_log(text)
        parsed.update({"server": server_side, "log_tail": text[-4000:]})
        return parsed

    def state(self):
        with open(self.state_path, "r", encoding="utf-8") as handle:
            return json.load(handle)

    def is_alive(self):
        if not os.path.exists(self.state_path):
            return False
        try:
            state = self.state()
        except (OSError, ValueError):
            return False
        pid = state.get("pid")
        if not pid:
            return False
        return _pid_alive(pid)

    def client(self, timeout=120.0):
        state = self.state()
        return CodesysClient(port=state["port"], token=state["token"], timeout=timeout,
                             state_path=self.state_path)

    def stop(self, kill_after=20.0):
        state = None
        if os.path.exists(self.state_path):
            try:
                state = self.state()
            except (OSError, ValueError):
                state = None
        if state:
            try:
                client = CodesysClient(port=state["port"], token=state["token"], timeout=15.0,
                                       state_path=self.state_path)
                client.quit()
                client.close()
            except protocol.ServiceError:
                pass
        pid = (state or {}).get("pid")
        deadline = time.time() + kill_after
        while time.time() < deadline:
            if not pid or not _pid_alive(pid):
                break
            time.sleep(0.4)
        if pid and _pid_alive(pid):
            _taskkill(pid)
        if self._stderr_handle is not None:
            try:
                self._stderr_handle.close()
            except OSError:
                pass
            self._stderr_handle = None
        if os.path.exists(self.state_path):
            os.remove(self.state_path)
        return {"stopped": True, "pid": pid}


def _pid_alive(pid):
    if os.name == "nt":
        result = subprocess.run(["tasklist", "/FI", "PID eq %s" % pid, "/NH"],
                                capture_output=True, text=True)
        return str(pid) in (result.stdout or "")
    try:
        os.kill(int(pid), 0)
        return True
    except OSError:
        return False


def _taskkill(pid):
    subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"],
                   capture_output=True, text=True)
