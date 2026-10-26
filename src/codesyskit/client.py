"""Client for the CODESYS resident service (standard library only)."""

import json
import os
import socket

from . import errors, protocol

DEFAULT_STATE = os.path.join(
    os.environ.get("LOCALAPPDATA") or os.path.expanduser("~"), "codesyskit", "service.json")


def load_state(path=None):
    path = path or DEFAULT_STATE
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


class CodesysClient:
    """Talks to the in-IDE service.  One connection, keep-alive, one response per request."""

    def __init__(self, port=None, token=None, host="127.0.0.1", timeout=60.0,
                 state_path=None, connect_timeout=10.0):
        self.host = host
        self.timeout = timeout
        self.connect_timeout = connect_timeout
        self.state_path = state_path or DEFAULT_STATE
        if port is None or token is None:
            state = load_state(self.state_path)
            port = port if port is not None else state["port"]
            token = token if token is not None else state["token"]
        self.port = int(port)
        self.token = token
        self._sock = None
        self._reader = None

    # -- transport ---------------------------------------------------------
    def _connect(self):
        self._disconnect()
        sock = socket.create_connection((self.host, self.port), timeout=self.connect_timeout)
        sock.settimeout(self.timeout)
        self._sock = sock
        self._reader = sock.makefile("rb")

    def _disconnect(self):
        for resource in (self._reader, self._sock):
            try:
                if resource is not None:
                    resource.close()
            except OSError:
                pass
        self._reader = None
        self._sock = None

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        try:
            self.quit()
        except Exception:  # noqa: BLE001 - closing is best effort
            pass
        self._disconnect()
        return False

    # -- request/response --------------------------------------------------
    def call(self, cmd, timeout_ms=None, **args):
        request = {"v": protocol.PROTOCOL_VERSION, "id": protocol.new_id(), "token": self.token,
                   "cmd": cmd, "args": args}
        if timeout_ms is not None:
            request["timeout_ms"] = int(timeout_ms)
        try:
            self._connect()
            self._sock.sendall(protocol.encode(request))
            line = self._reader.readline()
            self._disconnect()
        except socket.timeout:
            self._disconnect()
            raise protocol.ServiceError(errors.E_TIMEOUT,
                                        "no reply for %r within %.1fs" % (cmd, self.timeout),
                                        request_id=request["id"])
        except OSError as exc:
            self._disconnect()
            raise protocol.ServiceError(errors.E_PROTOCOL, "transport error: %s" % exc,
                                        request_id=request["id"])
        if not line:
            self._disconnect()
            raise protocol.ServiceError(errors.E_PROTOCOL, "service closed the connection",
                                        request_id=request["id"])
        response = protocol.decode_response(line)
        if not response.get("ok"):
            error = response.get("error") or {}
            raise protocol.ServiceError(error.get("code") or response.get("code") or errors.E_INTERNAL,
                                        error.get("message") or "request failed",
                                        error.get("detail"), request["id"])
        return response.get("result")

    # -- convenience -------------------------------------------------------
    def ping(self):
        return self.call("ping")

    def version(self):
        return self.call("version")

    def devices(self, filter=None, limit=20):
        args = {"limit": limit}
        if filter:
            args["filter"] = filter
        return self.call("devices", **args)

    def projects(self):
        return self.call("projects")

    def create(self, path, device=None, **options):
        """Create a project.  With ``device`` the kit also builds POU+task (pass bare=True to skip)."""
        args = {"path": path}
        if device:
            args["device"] = device
        args.update(options)
        return self.call("project.create", **args)

    def open(self, path):
        return self.call("project.open", path=path)

    def save(self, path=None):
        return self.call("project.save", path=path) if path else self.call("project.save")

    def info(self):
        return self.call("project.info")

    def tree(self, path="", depth=2):
        return self.call("tree", path=path, depth=depth)

    def read(self, path, part="declaration"):
        return self.call("pou.read", path=path, part=part)

    def write(self, path, text, part="declaration"):
        return self.call("pou.write", path=path, part=part, text=text)

    def create_pou(self, name, kind="program", parent=None, language=None):
        args = {"name": name, "kind": kind}
        if parent:
            args["parent"] = parent
        if language:
            args["language"] = language
        return self.call("pou.create", **args)

    def create_task(self, name="MainTask", pous=None, interval=None, unit=None, priority=None):
        args = {"name": name}
        if pous:
            args["pous"] = pous
        if interval is not None:
            args["interval"] = interval
        if unit:
            args["unit"] = unit
        if priority is not None:
            args["priority"] = priority
        return self.call("task.create", **args)

    def tasks(self):
        return self.call("tasks")

    def build(self, timeout_ms=600000):
        return self.call("build", timeout_ms=timeout_ms)

    def messages(self, clear=False):
        return self.call("messages", clear=clear)

    def batch(self, calls, stop_on_error=False, timeout_ms=None):
        return self.call("batch", calls=calls, stop_on_error=stop_on_error,
                         timeout_ms=timeout_ms)

    # -- IDE commands ------------------------------------------------------
    def commands(self, filter=None, limit=0):
        args = {"limit": limit}
        if filter:
            args["filter"] = filter
        return self.call("commands", **args)

    def execute(self, name=None, guid=None, index=None, timeout_ms=600000):
        args = {}
        for key, value in (("name", name), ("guid", guid), ("index", index)):
            if value is not None:
                args[key] = value
        if not args:
            raise ValueError("execute needs a name, a guid or an index")
        return self.call("execute", timeout_ms=timeout_ms, **args)

    # -- object structure --------------------------------------------------
    def object_info(self, path):
        return self.call("object.info", path=path)

    def rename(self, path, name):
        return self.call("object.rename", path=path, name=name)

    def delete(self, path):
        return self.call("object.delete", path=path)

    def move(self, path, parent, index=-1):
        return self.call("object.move", path=path, parent=parent, index=index)

    def mkdir(self, name, parent=None):
        args = {"name": name}
        if parent:
            args["parent"] = parent
        return self.call("folder.create", **args)

    # -- search ------------------------------------------------------------
    def find(self, pattern, case_sensitive=False, part="both", limit=200, path=None):
        args = {"pattern": pattern, "case_sensitive": case_sensitive, "part": part,
                "limit": limit}
        if path:
            args["path"] = path
        return self.call("find.text", **args)

    # -- libraries ---------------------------------------------------------
    def libraries(self):
        return self.call("libraries")

    def add_library(self, name):
        return self.call("library.add", name=name)

    def install_library(self, path):
        """Install a .compiled-library / .library file into the local repository."""
        return self.call("library.install", path=path)

    # -- exchange ----------------------------------------------------------
    def export_xml(self, path, target=None):
        args = {"path": path}
        if target:
            args["target"] = target
        return self.call("export.xml", **args)

    def import_xml(self, path):
        return self.call("import.xml", path=path)

    def export_native(self, path, target=None):
        args = {"path": path}
        if target:
            args["target"] = target
        return self.call("export.native", **args)

    def archive(self, path):
        return self.call("project.archive", path=path)

    def generate_runtime(self, directory):
        return self.call("generate.runtime", directory=directory)

    def export_doc(self, path):
        return self.call("project.doc", path=path)

    # -- IEC object model ---------------------------------------------------
    def create_typed(self, kind, name, return_type=None, text=None, language=None):
        args = {"kind": kind, "name": name}
        for key, value in (("return_type", return_type), ("text", text),
                           ("language", language)):
            if value is not None:
                args[key] = value
        return self.call("pou.create_typed", **args)

    def add_member(self, parent, kind, name, return_type=None, text=None):
        args = {"parent": parent, "kind": kind, "name": name}
        if return_type is not None:
            args["return_type"] = return_type
        if text is not None:
            args["text"] = text
        return self.call("pou.member", **args)

    def members(self, path):
        return self.call("pou.members", path=path)

    def symbols_create(self, export_comments=True, opc_ua=False, layout_calculator=None):
        args = {"export_comments": export_comments, "opc_ua": opc_ua}
        if layout_calculator is not None:
            args["layout_calculator"] = layout_calculator
        return self.call("symbols.create", **args)

    def symbols_info(self, path):
        return self.call("symbols.info", path=path)

    def textlist_create(self, name=None, languages=None):
        args = {}
        if name:
            args["name"] = name
        if languages:
            args["languages"] = languages
        return self.call("textlist.create", **args)

    def textlist_languages(self, path, add=None):
        args = {"path": path}
        if add:
            args["add"] = add
        return self.call("textlist.languages", **args)

    def create_persistent(self, name="PersistentVars"):
        return self.call("pou.persistent", name=name)

    def textlist_rows(self, path, limit=50):
        return self.call("textlist.rows", path=path, limit=limit)

    def textlist_text(self, path, text, text_id=None, language=None):
        args = {"path": path, "text": text}
        if text_id:
            args["id"] = text_id
        if language:
            args["language"] = language
        return self.call("textlist.text", **args)

    def project_permissions(self, command, group=None):
        args = {"command": command}
        if group:
            args["group"] = group
        return self.call("project.permissions", **args)

    def online_files(self, directory="/", simulation=None):
        args = {"directory": directory}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.files", **args)

    def textlist_export(self, path, out):
        return self.call("textlist.export", path=path, out=out)

    # -- application / project lifecycle -----------------------------------
    def app_clean(self):
        return self.call("app.clean")

    def app_generate(self):
        return self.call("app.generate")

    def app_status(self):
        return self.call("app.status")

    def save_as(self, path):
        return self.call("project.save_as", path=path, timeout_ms=600000)

    def project_meta(self, **fields):
        """Read (and optionally write) title/company/version/author/released/default_namespace."""
        return self.call("project.meta", **fields)

    def export_library(self, path, title=None, version=None, company=None):
        args = {"path": path}
        for key, value in (("title", title), ("version", version), ("company", company)):
            if value is not None:
                args[key] = value
        return self.call("project.export_library", **args, timeout_ms=600000)

    def project_clean(self):
        return self.call("project.clean")

    def compare(self, path):
        return self.call("project.compare", path=path, timeout_ms=600000)

    def project_users(self, add_user=None, add_group=None):
        args = {}
        if add_user:
            args["add_user"] = add_user
        if add_group:
            args["add_group"] = add_group
        return self.call("project.users", **args)

    def project_integrity(self, enable=False):
        return self.call("project.integrity", enable=enable)

    def io_export(self, path, device=None):
        args = {"path": path}
        if device:
            args["device"] = device
        return self.call("project.io_export", **args)

    def io_import(self, path, device=None):
        args = {"path": path}
        if device:
            args["device"] = device
        return self.call("project.io_import", **args)

    # -- tasks -------------------------------------------------------------
    def task_info(self, path):
        return self.call("task.info", path=path)

    def task_update(self, path, priority=None, interval=None, interval_unit=None,
                    watchdog_time=None, watchdog_enabled=None):
        args = {"path": path}
        for key, value in (("priority", priority), ("interval", interval),
                           ("interval_unit", interval_unit),
                           ("watchdog_time", watchdog_time),
                           ("watchdog_enabled", watchdog_enabled)):
            if value is not None:
                args[key] = value
        return self.call("task.update", **args)

    # -- online (simulation works headless; a real PLC needs a gateway) -----
    def online_force(self, expression, value, simulation=None):
        args = {"expression": expression, "value": value}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.force", **args)

    def online_unforce(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.unforce", **args)

    def online_forced(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.forced", **args)

    def online_simulation(self, enabled=None):
        args = {}
        if enabled is not None:
            args["enabled"] = bool(enabled)
        return self.call("online.simulation", **args)

    def online_state(self):
        return self.call("online.state")

    def online_login(self, simulation=None, change_option="never", delete_foreign=False,
                     autostart=False):
        args = {"change_option": change_option, "delete_foreign": delete_foreign,
                "autostart": autostart}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.login", **args)

    def online_logout(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.logout", **args)

    def online_start(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.start", **args)

    def online_stop(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.stop", **args)

    def online_read(self, expression=None, expressions=None, simulation=None):
        args = {}
        if expression:
            args["expression"] = expression
        if expressions:
            args["expressions"] = expressions
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.read", **args)

    def online_write(self, expression, value, simulation=None):
        args = {"expression": expression, "value": value}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.write", **args)

    def online_monitor(self, expressions=None, expression=None, samples=5, interval_ms=500,
                       simulation=None):
        args = {"samples": samples, "interval_ms": interval_ms}
        if expression:
            args["expression"] = expression
        if expressions:
            args["expressions"] = expressions
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.monitor", timeout_ms=600000, **args)

    def online_download(self, simulation=None):
        args = {}
        if simulation is not None:
            args["simulation"] = bool(simulation)
        return self.call("online.download", timeout_ms=600000, **args)

    def quit(self):
        return self.call("quit")

    def close(self):
        self._disconnect()
