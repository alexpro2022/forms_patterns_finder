import pytest
import pytest_asyncio
from aiohttp import web
from aiohttp.test_utils import TestClient

from app.app import app_init
from app.calculation import get_best_match, is_match
from app.config import config
from app.data import load_data
from app.data.load_data import *
from app.data.types import *
from app.utils import *


@pytest_asyncio.fixture
async def async_client(aiohttp_client) -> TestClient:
    return await aiohttp_client(await app_init())
