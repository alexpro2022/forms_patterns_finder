from aiohttp import web

from app.calculation import find_pattern
from app.config import config
from app.utils import get_form_data


async def index(request: web.Request):
    return web.Response(text='Hello, world')


async def forms_view(request: web.Request):
    data = await get_form_data(request)
    result = await find_pattern(
        request.app['db'][config.collection_name], data
    )
    return web.json_response(data=result)
