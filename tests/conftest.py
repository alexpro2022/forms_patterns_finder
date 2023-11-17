from aiohttp import web
import pytest
import pytest_asyncio
from aiohttp.test_utils import TestClient  # noqa

from app.calculation import get_best_match, is_match  # noqa
from app.data.load_data import *  # noqa
from app.data.types import *  # noqa
from app.app import make_app
from app.config import config
from app.data import load_data
from app.db import setup_db
from app.utils import *  # noqa


@pytest_asyncio.fixture
async def get_db():
    return await setup_db(config.database_url, load_data.PATTERNS)


@pytest_asyncio.fixture
async def get_app(get_db) -> web.Application:
    app = make_app()
    app["db"] = get_db
    return app


@pytest.fixture
def async_client(aiohttp_client, event_loop, get_app):
    return event_loop.run_until_complete(aiohttp_client(get_app))
