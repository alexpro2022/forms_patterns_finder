import pytest
from aiohttp import web
from deepdiff import DeepDiff

from tests.fixtures import data as d

ENDPOINT = '/get_form'


@pytest.mark.asyncio
@pytest.mark.parametrize('payload, expected', (
    *d.FULL_MATCH_SET,
    *d.GREATER_FIELDS_MATCH_SET,
    *d.BEST_MATCH_SET,
    *d.FULL_MISMATCH_SET,
    *d.FIELD_NAME_MISMATCH_SET,
    *d.FIELD_VALUE_MISMATCH_SET,
))
async def test_get_form_endpoint(async_client, payload, expected) -> None:
    response = await async_client.post(ENDPOINT, data=payload)
    assert response.status == web.HTTPOk.status_code
    result = await response.json()
    diff = DeepDiff(result, expected, ignore_order=True)
    assert not diff, diff


@pytest.mark.asyncio
async def test_hello(async_client):
    expected_response = 'Web-приложение для определения заполненных форм.'
    response = await async_client.get(ENDPOINT)
    assert response.status == web.HTTPOk.status_code
    assert await response.text() == expected_response
