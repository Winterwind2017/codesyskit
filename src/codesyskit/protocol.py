"""Wire format of the resident service: one JSON object per line, both directions.

Request::

    {"v":1,"id":"<client id>","token":"<hex>","cmd":"ping","args":{},"timeout_ms":30000}

Response::

    {"v":1,"id":"<same id>","ok":true,"code":"OK","result":{...},"elapsed_ms":3}
    {"v":1,"id":"<same id>","ok":false,"code":"E_STATE",
     "error":{"code":"E_STATE","message":"no project open","detail":null},"elapsed_ms":1}

The framing is deliberately plain (newline delimited): the in-IDE side is IronPython 2.7 and
must stay dependency free, and a human can drive the port with ``telnet``/``nc`` when debugging.
"""

import json
import uuid

from . import errors

PROTOCOL_VERSION = 1
MAX_LINE = 1 << 20          # 1 MiB per request, guards the IronPython side


def new_id():
    return uuid.uuid4().hex[:16]


def encode(request):
    payload = json.dumps(request, ensure_ascii=False, separators=(",", ":"))
    return (payload + "\n").encode("utf-8")


def decode_request(line):
    """Parse one request line.  Raises :class:`ProtocolError` with a code."""
    if isinstance(line, bytes):
        try:
            line = line.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ProtocolError(errors.E_PROTOCOL, "request is not utf-8: %s" % exc)
    line = line.strip()
    if not line:
        raise ProtocolError(errors.E_PROTOCOL, "empty request")
    if len(line.encode("utf-8")) > MAX_LINE:
        raise ProtocolError(errors.E_PROTOCOL, "request larger than %d bytes" % MAX_LINE)
    try:
        request = json.loads(line)
    except ValueError as exc:
        raise ProtocolError(errors.E_PROTOCOL, "request is not json: %s" % exc)
    if not isinstance(request, dict):
        raise ProtocolError(errors.E_PROTOCOL, "request must be a json object")
    version = request.get("v", PROTOCOL_VERSION)
    if version != PROTOCOL_VERSION:
        raise ProtocolError(errors.E_PROTOCOL,
                            "protocol version %r not supported" % (version,))
    if not request.get("cmd"):
        raise ProtocolError(errors.E_ARGS, "request has no cmd")
    return request


def decode_response(line):
    if isinstance(line, bytes):
        line = line.decode("utf-8", "replace")
    return json.loads(line)


def ok_response(request_id, result, elapsed_ms):
    return {"v": PROTOCOL_VERSION, "id": request_id, "ok": True, "code": errors.OK,
            "result": result, "elapsed_ms": int(elapsed_ms)}


def error_response(request_id, code, message, detail=None, elapsed_ms=0):
    return {"v": PROTOCOL_VERSION, "id": request_id, "ok": False, "code": code,
            "error": {"code": code, "message": str(message)[:2000],
                      "detail": None if detail is None else str(detail)[:4000]},
            "elapsed_ms": int(elapsed_ms)}


class ProtocolError(Exception):
    def __init__(self, code, message):
        Exception.__init__(self, message)
        self.code = code
        self.message = message


class ServiceError(Exception):
    """A failed response surfaced to the client as an exception."""

    def __init__(self, code, message, detail=None, request_id=None):
        Exception.__init__(self, "%s: %s" % (code, message))
        self.code = code
        self.message = message
        self.detail = detail
        self.request_id = request_id

    def as_dict(self):
        return {"code": self.code, "message": self.message, "detail": self.detail,
                "request_id": self.request_id}
