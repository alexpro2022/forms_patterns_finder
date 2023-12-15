from aiohttp import web
from aiohttp.test_utils import TestClient


def test_async_client(async_client) -> None:
    assert isinstance(async_client, TestClient)
    assert isinstance(async_client.app, web.Application)
