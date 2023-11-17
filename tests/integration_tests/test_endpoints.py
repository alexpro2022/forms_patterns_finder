import pytest
from deepdiff import DeepDiff

from tests import conftest as c
from tests.fixtures import data as d

ENDPOINT = '/get_form'
HTTP_OK = 200


@pytest.mark.asyncio
@pytest.mark.parametrize('payload, expected', (
    *d.FULL_MATCH_SET,
    *d.GREATER_FIELDS_MATCH_SET,
    *d.BEST_MATCH_SET,
    *d.FULL_MISMATCH_SET,
    *d.FIELD_NAME_MISMATCH_SET,
    *d.FIELD_VALUE_MISMATCH_SET,
))
async def test_get_form_endpoint(
    async_client: c.TestClient, payload: dict, expected: dict
) -> None:
    response = await async_client.post(ENDPOINT, data=payload)
    assert response.status == HTTP_OK
    result = await response.json()
    diff = DeepDiff(result, expected, ignore_order=True)
    assert not diff
