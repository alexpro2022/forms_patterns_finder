from tests import conftest as c
import pytest


def test_get_app(get_app) -> None:
    assert isinstance(get_app, c.web.Application)


def test_async_client(async_client) -> None:
    assert isinstance(async_client, c.TestClient)
