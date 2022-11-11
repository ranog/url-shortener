import pytest

from src.exceptions import InvalidUrl
from src.url_validator import validate


async def test_it_should_return_url():
    url = 'http://www.example.com'
    validated_url = validate(url)
    assert url == validated_url


async def test_it_should_raise_exception_when_it_is_not_valid_url():
    url = 'ftp://invalid.url'
    with pytest.raises(InvalidUrl):
        validate(url)


async def test_it_should_raise_exception_when_it_is_not_url():
    url = 'not a url'
    with pytest.raises(InvalidUrl):
        validate(url)


async def test_it_should_raise_exception_when_url_is_not_a_string():
    url = 123
    with pytest.raises(InvalidUrl):
        validate(url)


async def test__it_should_raise_exception_when_url_is_none():
    url = None
    with pytest.raises(InvalidUrl):
        validate(url)
