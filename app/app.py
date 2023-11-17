from aiohttp import web

from app.config import config
from app.data import load_data
from app.db import setup_db
from app.routes import setup_routes


def make_app() -> web.Application:
    app = web.Application()
    setup_routes(app)
    return app


async def app_init(
    database_url: str = config.database_url
) -> web.Application:
    app = make_app()
    app['db'] = await setup_db(database_url, load_data.PATTERNS)
    return app
