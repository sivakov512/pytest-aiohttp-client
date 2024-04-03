__all__ = ["AwesomeTestClient"]

import typing

import pytest
from aiohttp.client import ClientResponse
from aiohttp.test_utils import TestClient
from aiohttp.web import Application

_RetType = typing.Union[ClientResponse, typing.Any, bytes]


class AwesomeTestClient:
    def __init__(self, aiohttp_test_client: TestClient) -> None:
        self._inner = aiohttp_test_client

    async def get(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("POST", path, **kwargs)

    async def options(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("OPTIONS", path, **kwargs)

    async def head(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("HEAD", path, **kwargs)

    async def put(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("PUT", path, **kwargs)

    async def patch(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("PATCH", path, **kwargs)

    async def delete(self, path: str, **kwargs: typing.Any) -> _RetType:
        return await self.request("DELETE", path, **kwargs)

    async def request(
        self,
        method: str,
        path: str,
        expected_status: typing.Optional[int] = None,
        as_response: bool = False,
        **kwargs: typing.Any
    ) -> _RetType:
        response = await self._inner.request(method, path, **kwargs)

        if expected_status:
            assert response.status == expected_status

        result: _RetType
        if as_response:
            result = response
        elif response.content_type == "application/json":
            result = await response.json()
        else:
            result = await response.read()

        return result


@pytest.fixture
async def api(
    aiohttp_client: typing.Callable[[Application], typing.Awaitable[TestClient]],
    aiohttp_app: Application,
) -> AwesomeTestClient:
    client = await aiohttp_client(aiohttp_app)
    return AwesomeTestClient(client)
