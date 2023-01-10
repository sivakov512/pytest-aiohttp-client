# pytest-aiohttp-client

Awesome pytest fixture for awesome [aiohttp](https://docs.aiohttp.org/en/stable/)!

[![Build status](https://github.com/sivakov512/pytest-aiohttp-client/workflows/test/badge.svg)](https://github.com/sivakov512/pytest-aiohttp-client/actions?query=workflow%3Atest)
[![Coverage Status](https://coveralls.io/repos/github/sivakov512/pytest-aiohttp-client/badge.svg?branch=main)](https://coveralls.io/github/sivakov512/pytest-aiohttp-client?branch=main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Python versions](https://img.shields.io/pypi/pyversions/pytest-aiohttp-client.svg)](https://pypi.python.org/pypi/pytest-aiohttp-client)
[![PyPi](https://img.shields.io/pypi/v/pytest-aiohttp-client.svg)](https://pypi.python.org/pypi/pytest-aiohttp-client)

## Installation

Install it via `pip` tool:

```bash
pip install pytest-aiohttp-client
```

or Poetry:

```bash
poetry add yandex-geocoder
```

## Usage example

Plugin provides `api` fixture, but you should define `aiohttp_app` fixture first:

```python
import pytest

from my_awesome_app import make_app


@pytest.fixture
def aiohttp_app() -> Application:
  return make_app()
```

### Default decoding

Fixture will decode and return payload by default as json or bytes (depends on `Content-Type` header):

```python
async def test_returns_json(api):
    got = await api.get("/json-url/")

    assert got == {"key": "value"}


async def test_returns_bytes(api):
    got = await api.get("/url/")

    assert got == b"Some text"
```

### Status code assertions

You can assert on status code:

```python
async def test_returns_ok(api):
    await api.get("/url/", expected_status=200)
```

### `Response` result

Type `as_response=True` if you need `ClientResponse` object:

```python
from aiohttp.client import ClientResponse

async def test_returns_response(api):
    got = await api.get("/url/", as_response=True)

    assert isinstance(got, ClientResponse)
```

## Development and contribution

First of all you should install [Poetry](https://python-poetry.org).

- install project dependencies

```bash
make install
```

- run linters

```bash
make lint
```

- run tests

```bash
make test
```

- feel free to contribute!
