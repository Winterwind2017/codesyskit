"""Wire protocol tests -- no CODESYS needed."""

import json

import pytest

from codesyskit import errors, protocol


def test_encode_is_one_json_line():
    raw = protocol.encode({"v": 1, "id": "a", "token": "t", "cmd": "ping", "args": {}})
    assert raw.endswith(b"\n")
    assert raw.count(b"\n") == 1
    assert json.loads(raw.decode("utf-8"))["cmd"] == "ping"


def test_decode_request_accepts_bytes_and_str():
    assert protocol.decode_request(b'{"cmd":"ping"}')["cmd"] == "ping"
    assert protocol.decode_request('{"cmd":"ping"}')["cmd"] == "ping"


def test_decode_request_rejects_garbage():
    for line in ("", "   ", "not json", "[1,2]", '{"args":{}}'):
        with pytest.raises(protocol.ProtocolError) as info:
            protocol.decode_request(line)
        assert info.value.code in (errors.E_PROTOCOL, errors.E_ARGS)


def test_decode_request_rejects_wrong_version():
    with pytest.raises(protocol.ProtocolError) as info:
        protocol.decode_request('{"v":99,"cmd":"ping"}')
    assert info.value.code == errors.E_PROTOCOL


def test_decode_request_rejects_oversize():
    big = '{"cmd":"ping","pad":"%s"}' % ("x" * (protocol.MAX_LINE + 10))
    with pytest.raises(protocol.ProtocolError) as info:
        protocol.decode_request(big)
    assert info.value.code == errors.E_PROTOCOL


def test_ok_and_error_shapes():
    ok = protocol.ok_response("id1", {"a": 1}, 3)
    assert ok["ok"] is True and ok["code"] == errors.OK and ok["result"] == {"a": 1}
    bad = protocol.error_response("id2", errors.E_STATE, "no project", "detail", 5)
    assert bad["ok"] is False and bad["code"] == errors.E_STATE
    assert bad["error"]["message"] == "no project"
    assert bad["error"]["detail"] == "detail"


def test_new_id_is_unique():
    ids = {protocol.new_id() for _ in range(50)}
    assert len(ids) == 50


def test_error_codes_are_closed_set():
    assert errors.OK in errors.ALL
    assert len(set(errors.ALL)) == len(errors.ALL)
    for code in errors.ALL:
        assert code.startswith("OK") or code.startswith("E_")
