from aiohttp import web
from app.app import app_init


if __name__ == "__main__":
    web.run_app(app_init())
