import json


class ParseError(Exception):
    ...


class InvalidRequest(Exception):
    ...


class MethodNotFound(Exception):
    ...


class InvalidParams(Exception):
    ...


class RPC:
    PARSE_ERROR = -32700
    INVALID_REQUEST = -32600
    METHOD_NOT_FOUND = -32601
    INVALID_PARAMS = -32602
    INTERNAL_ERROR = -32603
    SERVER_ERROR = -32000

    def __init__(self, methods: "dict | None" = None):
        self.methods = {}
        if methods:
            for name, method in methods.items():
                self.register(name, method)

    def register(self, name, method):
        self.methods[name] = method

    def parse(self, raw_data: str) -> dict:
        try:
            data = {"kwargs": {}, "args": ()}
            data.update(json.loads(raw_data))
        except Exception as e:
            raise ParseError() from e
        return data

    def extract_params(self, data: dict) -> None:
        params = data.get("params")
        if params:
            if type(params) not in {dict, list}:
                raise InvalidRequest()
            data["kwargs"] = params if isinstance(params, dict) else {}
            data["args"] = params if isinstance(params, list) else []
            del data["params"]

    def validate(self, data):
        if not all(data.get(x) for x in ("jsonrpc", "method")):
            raise InvalidRequest()

        if data.get("jsonrpc", None) != "2.0":
            raise InvalidRequest("Missing or invalid version.")

    def error(self, e: Exception, id: "str | None" = None) -> dict:
        code, default_msg = {
            ParseError: (self.PARSE_ERROR, "Parse error"),
            InvalidRequest: (self.INVALID_REQUEST, "Invalid Request"),
            MethodNotFound: (self.METHOD_NOT_FOUND, "Method not found"),
            InvalidParams: (self.INVALID_PARAMS, "Invalid params"),
        }.get(type(e), (self.INTERNAL_ERROR, "Internal error"))
        return {
            "jsonrpc": "2.0",
            "id": id,
            "error": {"code": code, "message": str(e) or default_msg},
        }

    def call_method(self, data: dict) -> "dict | str | int":
        try:
            method = self.methods[data["method"]]
        except KeyError as e:
            raise MethodNotFound("Method not found") from e
        return method(*data["args"], **data["kwargs"])

    def _handle_entry(self, data: dict):
        if not isinstance(data, dict):
            return self.error(InvalidRequest())
        id = None
        try:
            self.extract_params(data)
            id = data.get("id")
            self.validate(data)
            result = self.call_method(data)
            if id:
                return {"jsonrpc": "2.0", "result": result, "id": id}
            else:
                return None
        except Exception as e:
            return self.error(e, id)

    def _handle_packet(self, packet: str) -> "str | None":
        try:
            data = self.parse(packet)
            if isinstance(data, list):
                if not data:
                    raise InvalidRequest()
                return [self._handle_entry(x) for x in data]
            else:
                return self._handle_entry(data)
        except Exception as e:
            return self.error(e)

    def handle_packet(self, packet: str) -> str:
        resp = self._handle_packet(packet)
        return json.dumps(resp) if resp else None
