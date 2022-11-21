import pytest

from src.exceptions import LongUrlError
from src.url_validator import validate


async def test_it_should_return_url():
    long_url = 'http://www.example.com'
    validated_url = await validate(long_url)
    assert long_url == validated_url


async def test_it_should_raise_exception_when_it_is_not_valid_url():
    long_url = 'ftp://invalid.url'
    with pytest.raises(LongUrlError):
        await validate(long_url)


async def test_it_should_raise_exception_when_it_is_not_url():
    long_url = 'not a url'
    with pytest.raises(LongUrlError):
        await validate(long_url)


async def test_it_should_raise_exception_when_url_is_not_a_string():
    long_url = 123
    with pytest.raises(LongUrlError):
        await validate(long_url)


async def test__it_should_raise_exception_when_url_is_none():
    long_url = None
    with pytest.raises(LongUrlError):
        await validate(long_url)
