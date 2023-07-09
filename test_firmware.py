from firmware.jsonrpc import RPC
from json import dumps, loads
import pytest


@pytest.fixture
def rpc(mocker):
    return RPC(methods={"foo": mocker.Mock(), "bar": mocker.Mock()})


def test_invalid_version_returns_error(rpc):
    request = dumps({"jsonrpc": "1.0", "method": "foo", "id": "1"})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32600, "message": "Missing or invalid version."},
        "id": "1",
    }


def test_missing_method_returns_error(rpc):
    request = dumps({"jsonrpc": "2.0", "method": "foobar", "id": "1"})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32601, "message": "Method not found"},
        "id": "1",
    }


def test_invalid_json_returns_error(rpc):
    request = '{"jsonrpc": "2.0", "method": "foobar, "params": "bar", "baz]'
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32700, "message": "Parse error"},
        "id": None,
    }


def test_invalid_request_returns_error(rpc):
    request = dumps({"jsonrpc": "2.0", "method": 1, "params": "bar"})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32600, "message": "Invalid Request"},
        "id": None,
    }


def test_batch_invalid_json_returns_error(rpc):
    request = """[
  {"jsonrpc": "2.0", "method": "sum", "params": [1,2,4], "id": "1"},
  {"jsonrpc": "2.0", "method"
]"""
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32700, "message": "Parse error"},
        "id": None,
    }


def test_batch_empty_array_returns_error(rpc):
    request = "[]"
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "error": {"code": -32600, "message": "Invalid Request"},
        "id": None,
    }


def test_non_rpc_array_returns_error(rpc):
    request = "[1,2,3]"
    assert loads(rpc.handle_packet(request)) == [
        {
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
            "id": None,
        },
        {
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
            "id": None,
        },
        {
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
            "id": None,
        },
    ]


def test_single_batch_invalid_returns_error(rpc):
    request = "[1]"
    assert loads(rpc.handle_packet(request)) == [
        {
            "jsonrpc": "2.0",
            "error": {"code": -32600, "message": "Invalid Request"},
            "id": None,
        },
    ]


def test_positional_params(rpc):
    rpc.methods["foo"].return_value = 17
    request = dumps({"jsonrpc": "2.0", "method": "foo", "params": [1, 2, 3], "id": 1})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "result": 17,
        "id": 1,
    }
    rpc.methods["foo"].assert_called_once_with(1, 2, 3)


def test_missing_params(rpc):
    rpc.methods["foo"].return_value = 17
    request = dumps({"jsonrpc": "2.0", "method": "foo", "id": 1})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "result": 17,
        "id": 1,
    }
    rpc.methods["foo"].assert_called_once_with()


def test_empty_positional_params(rpc):
    rpc.methods["foo"].return_value = 17
    request = dumps({"jsonrpc": "2.0", "method": "foo", "params": [], "id": 1})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "result": 17,
        "id": 1,
    }
    rpc.methods["foo"].assert_called_once_with()


def test_empty_named_params(rpc):
    rpc.methods["foo"].return_value = 17
    request = dumps({"jsonrpc": "2.0", "method": "foo", "params": {}, "id": 1})
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "result": 17,
        "id": 1,
    }
    rpc.methods["foo"].assert_called_once_with()


def test_named_params(rpc):
    rpc.methods["foo"].return_value = 19
    request = dumps(
        {"jsonrpc": "2.0", "method": "foo", "params": {"a": 1, "b": 2}, "id": 1}
    )
    assert loads(rpc.handle_packet(request)) == {
        "jsonrpc": "2.0",
        "result": 19,
        "id": 1,
    }
    rpc.methods["foo"].assert_called_once_with(a=1, b=2)


def test_notification(rpc):
    request = dumps({"jsonrpc": "2.0", "method": "foo", "params": [1, 2, 3]})
    assert not rpc.handle_packet(request)
    assert rpc.methods["foo"].called_once_with(1, 2, 3)


def test_batch_call(rpc):
    rpc.methods["foo"].return_value = "fooresult"
    rpc.methods["bar"].return_value = "barresult"
    request = dumps(
        [
            {"jsonrpc": "2.0", "method": "foo", "params": [1, 2, 3], "id": 1},
            {"jsonrpc": "2.0", "method": "bar", "params": {"a": "b"}, "id": 2},
        ]
    )
    assert loads(rpc.handle_packet(request)) == [
        {"jsonrpc": "2.0", "result": "fooresult", "id": 1},
        {"jsonrpc": "2.0", "result": "barresult", "id": 2},
    ]
    rpc.methods["foo"].assert_called_once_with(1, 2, 3)
    rpc.methods["bar"].assert_called_once_with(a="b")
