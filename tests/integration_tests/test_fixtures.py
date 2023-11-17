from tests import conftest as c


def test_get_app(get_app) -> None:
    assert isinstance(get_app, c.web.Application)
    assert isinstance(get_app.get('db'), c.AgnosticDatabase)


def test_async_client(async_client) -> None:
    assert isinstance(async_client, c.TestClient)
