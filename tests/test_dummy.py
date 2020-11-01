import pytest

from pytest_aiohttp_client import dummy

pytestmark = [pytest.mark.asyncio]


async def test_dummy() -> None:
    assert await dummy() == "DUMMY"
