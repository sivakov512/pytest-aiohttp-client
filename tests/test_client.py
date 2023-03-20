import typing

import pytest
from aiohttp.client import ClientResponse

from pytest_aiohttp_client import AwesomeTestClient

_STATE_T = dict[str, typing.Union[str, bytes]]


@pytest.mark.parametrize("method", ["get", "post", "options", "head", "put", "patch", "delete"])
async def test_will_send_request_with_expected_method(
    method: str, api: AwesomeTestClient, req: _STATE_T
) -> None:
    await getattr(api, method)("/url/")

    assert req["method"] == method.upper()


@pytest.mark.parametrize(
    ("url", "expected"),
    [
        ("/json_url/", {"key": "value"}),  # parse as json because of content-type
        ("/url/", b"Some text"),  # returns bytes by default
    ],
)
async def test_returns_payload_by_default(
    url: str, expected: typing.Union[dict[str, str], bytes], api: AwesomeTestClient
) -> None:
    got = await api.get(url)

    assert got == expected


async def test_returns_response_if_requested(api: AwesomeTestClient) -> None:
    got = await api.get("/url/", as_response=True)

    assert isinstance(got, ClientResponse)


async def test_asserts_for_status_code(api: AwesomeTestClient) -> None:
    with pytest.raises(AssertionError):
        await api.get("/url/", expected_status=400)

    await api.get("/url/", expected_status=200)


@pytest.mark.parametrize("kw", [dict(data='{"k": "v"}'), dict(json={"k": "v"})])
async def test_passed_payload(
    kw: dict[str, typing.Any], api: AwesomeTestClient, req: _STATE_T
) -> None:
    await api.get("/url/", **kw)

    assert req["body"] == b'{"k": "v"}'
