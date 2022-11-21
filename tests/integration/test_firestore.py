import pytest

from src.exceptions import ShortUrlError
from src.url_shortener_repository import COLLECTION_NAME, UrlShortenerRepository
from src.url_shortening import shorten_url


async def test_it_should_persist_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    long_url = 'http://www.example.com'
    short_url = await shorten_url(long_url)
    url_shortener_repository = UrlShortenerRepository()
    await url_shortener_repository.add(long_url)
    response = await url_shortener_repository.get_long_url(short_url)
    assert response == long_url


async def test_it_should_create_only_one_record_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    long_url = 'http://www.dummy.com'
    short_url = await shorten_url(long_url)
    url_shortener_repository = UrlShortenerRepository()
    await url_shortener_repository.add(long_url)
    await url_shortener_repository.add(long_url)
    url_data = await url_shortener_repository.collection.where(
        field_path='short_url',
        op_string='==',
        value=short_url,
    ).get()
    assert len(url_data) == 1


async def test_it_should_raise_exception_when_the_short_url_does_not_exist_in_the_repository(clean_collection):
    await clean_collection(COLLECTION_NAME)
    with pytest.raises(ShortUrlError):
        await UrlShortenerRepository().get_long_url('dummy_short_url')
