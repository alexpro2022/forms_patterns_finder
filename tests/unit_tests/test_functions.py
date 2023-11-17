from aiohttp.test_utils import make_mocked_request
import pytest
from tests import conftest as c
from tests.fixtures.data import (
    data_test_is_date,
    data_test_is_email,
    data_test_is_match,
    data_test_is_phone_number,
    data_test_validate,
)


@pytest.mark.parametrize('value, expected', (
    *data_test_is_date.data,
))
def test_is_date(value, expected):
    assert c.is_date(value) == expected


@pytest.mark.parametrize('value, expected', (
    *data_test_is_phone_number.data,
))
def test_is_phone_number(value, expected):
    assert c.is_phone_number(value) == expected


@pytest.mark.parametrize('value, expected', (
    *data_test_is_email.data,
))
def test_is_email(value, expected):
    assert c.is_email(value) == expected


@pytest.mark.parametrize('value, expected', (
    *data_test_validate.data,
))
def test_validate(value, expected):
    assert c.validate(value) == expected


@pytest.mark.parametrize('value, expected', (
    (c.PATTERNS, c.PATTERNS[0]),
))
def test_get_best_match(value, expected):
    assert c.get_best_match(value) == expected


@pytest.mark.parametrize('pattern, form_data, expected', (
    *data_test_is_match.data,
))    
def test_is_match(pattern, form_data, expected):
    assert c.is_match(pattern, form_data) == expected


def test_make_app():
    assert isinstance(c.make_app(), c.web.Application)


@pytest.mark.skip(reason='Cannot properly mock a request')
@pytest.mark.parametrize('payload, expected', (
    ({'f_name1': 'value1', 'f_name2': 5}, [('f_name1', 'value1'), ('f_name2', 5)]),
    # ({'f_name1': 3, 'f_name2': 'value2'}, '[["f_name1","3"],["f_name2","value2"]]'),
))
def test_parse(payload, expected):
    request = make_mocked_request('POST', '/get_form', writer=payload)
    form_data = c.parse(request)
    assert form_data == expected
