"""Client behaviour against the fake service: token, error codes, timeout, batch, keep-alive."""

import time

import pytest

from codesyskit import errors, protocol
from codesyskit.client import CodesysClient
from fake_server import FakeService


@pytest.fixture()
def service():
    fake = FakeService().start()
    yield fake
    fake.stop()


def client_for(service, **kwargs):
    return CodesysClient(port=service.port, token=service.token, timeout=kwargs.pop("timeout", 20.0),
                         **kwargs)


def test_ping_round_trip(service):
    with client_for(service) as client:
        result = client.ping()
    assert result["banner"] == "fake"
    assert result["protocol"] == protocol.PROTOCOL_VERSION


def test_bad_token_raises_auth_error(service):
    client = CodesysClient(port=service.port, token="wrong", timeout=10.0)
    with pytest.raises(protocol.ServiceError) as info:
        client.ping()
    assert info.value.code == errors.E_TOKEN
    client.close()


def test_unknown_command_raises(service):
    with client_for(service) as client:
        with pytest.raises(protocol.ServiceError) as info:
            client.call("nope")
    assert info.value.code == errors.E_UNKNOWN_CMD


def test_missing_argument_maps_to_e_args(service):
    with client_for(service) as client:
        with pytest.raises(protocol.ServiceError) as info:
            client.call("needs_arg")
    assert info.value.code == errors.E_ARGS


def test_command_exception_maps_to_e_script(service):
    with client_for(service) as client:
        with pytest.raises(protocol.ServiceError) as info:
            client.call("fail")
    assert info.value.code == errors.E_SCRIPT
    assert info.value.detail == "trace"


def test_client_timeout(service):
    client = CodesysClient(port=service.port, token=service.token, timeout=0.5)
    started = time.perf_counter()
    with pytest.raises(protocol.ServiceError) as info:
        client.call("slow", seconds=3)
    assert info.value.code == errors.E_TIMEOUT
    assert time.perf_counter() - started < 3.0
    client.close()


def test_keep_alive_reuses_one_connection(service):
    with client_for(service) as client:
        for _ in range(5):
            client.ping()
    assert service.calls.count("ping") == 5


def test_batch_runs_several_commands(service):
    with client_for(service) as client:
        result = client.batch([{"cmd": "ping"}, {"cmd": "echo", "args": {"a": 1}}])
    assert result["executed"] == 2
    assert all(entry["ok"] for entry in result["results"])
    assert result["results"][1]["result"] == {"echo": {"a": 1}}


def test_batch_reports_partial_failures(service):
    with client_for(service) as client:
        result = client.batch([{"cmd": "ping"}, {"cmd": "fail"}, {"cmd": "echo"}])
    assert [entry["ok"] for entry in result["results"]] == [True, False, True]


def test_reconnect_after_transport_error(service):
    client = client_for(service)
    client.ping()
    client._disconnect()
    assert client.ping()["banner"] == "fake"
    client.close()
