import pytest
from deepdiff import DeepDiff

from tests import conftest as c
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
async def test_get_form_endpoint(async_client: c.TestClient, payload: dict, expected):
    response = await async_client.post(ENDPOINT, data=payload)
    assert response.status == 200
    result = await response.json()
    #content = await response.content.read()
    #result = content.decode()
    diff = DeepDiff(result, expected, ignore_order=True)
    assert not diff  # , info(f'\n\n{result}\n\n{expected}\n\n', raise_assert=False)


'''
    #async with aiohttp.ClientSession(trust_env=True) as session:
        #async with session.get(ENDPOINT, ssl=False) as response:  # 'http://python.org'

async def hello(request):
    return web.Response(text='Hello, world')


async def test_hello(aiohttp_client):
    app = web.Application()
    app.router.add_get('/', hello)
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text



@pytest.mark.asyncio
@pytest.mark.parametrize('input_data, expected', (
    ({'f_name1': 'value1', 'f_name2': 5}, 'asd'),
    ({'f_name1': 3, 'f_name2': 'value2'}, '[["f_name1","3"],["f_name2","value2"]]'),
))
async def test_get_form_endpoint(async_client: c.AsyncClient, input_data: dict, expected):
    response = await async_client.post('/get_form', data=input_data)
    assert response.status_code == 200
    result = response.content.decode()
    assert result == expected, info(f'\n\n{result}\n\n{expected}\n\n', raise_assert=False)
'''
