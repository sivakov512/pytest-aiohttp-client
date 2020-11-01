from typing import Dict, Tuple

import pytest
from aiohttp import web
from aiohttp.web import Application, Request, Response, json_response

pytest_plugins = ["aiohttp.pytest_plugin"]

_T = Tuple[Application, Dict[str, str]]


@pytest.fixture
def setup() -> _T:
    state: Dict[str, str] = {}

    async def reg(request: Request) -> None:
        nonlocal state
        state["method"] = request.method
        state["body"] = await request.read()

    async def handler(request: Request) -> Response:
        await reg(request)
        return Response(text="Some text")

    async def json_handler(request: Request) -> Response:
        await reg(request)
        return json_response({"key": "value"})

    app = Application()
    app.add_routes(
        [
            web.get("/url/", handler),
            web.post("/url/", handler),
            web.options("/url/", handler),
            web.put("/url/", handler),
            web.patch("/url/", handler),
            web.delete("/url/", handler),
            web.get("/json_url/", json_handler),
        ]
    )

    return app, state


@pytest.fixture
def aiohttp_app(setup: _T) -> Application:
    return setup[0]


@pytest.fixture
def req(setup: _T) -> Dict[str, str]:
    return setup[1]
