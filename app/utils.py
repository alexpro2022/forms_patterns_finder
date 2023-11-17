import re
from datetime import datetime as dt
from aiohttp import web

from app.data import types as t
from app.config import config


def info(obj, raise_assert: bool = True):
    if hasattr(obj, '__dict__'):
        obj = f'!!!__dict__: {vars(obj)}'
    print(obj)
    if raise_assert:
        assert 0


async def get_form_data(request: web.Request) -> dict[str, str]:
    """Parse, validate and change value to the type(value)."""
    data = await request.post()
    return {f_name: validate(f_value) for f_name, f_value in data.items()}


def validate(value: str) -> str:
    if is_date(value):
        return t.DATE_TYPE
    if is_phone_number(value):
        return t.PHONE_NUMBER_TYPE
    if is_email(value):
        return t.EMAIL_TYPE
    return t.TEXT_TYPE


def is_date(value: str) -> bool:
    for format in config.date_formats:
        try:
            return bool(dt.strptime(value, format))
        except ValueError:
            pass
    return False


def is_phone_number(value: str) -> bool:
    return _fullmatch(config.regex_phone_number, value)


def is_email(value: str) -> bool:
    return _fullmatch(config.regex_email, value)


def _fullmatch(pattern: str, value: str) -> bool:
    pattern = re.compile(pattern)
    return bool(re.fullmatch(pattern, value))
