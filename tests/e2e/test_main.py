from httpx import AsyncClient

from src.url_shortener_repository import COLLECTION_NAME, UrlShortenerRepository
from src.url_shortening import shorten_url


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_shorten_successfully(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    long_url = 'http://www.example.com'
    short_url = await shorten_url(long_url)
    response = await async_http_client.post('/v1/data/shorten/', json={'long_url': long_url})
    assert response.status_code == 200
    assert response.json() == short_url


async def test_it_should_short_url_successfully(clean_collection, async_http_client: AsyncClient):
    await clean_collection(COLLECTION_NAME)
    url = 'http://www.dummy.url.com'
    await UrlShortenerRepository().add(url)
    short_url = await shorten_url(url)
    response = await async_http_client.get(f'/v1/{short_url}/')
    assert response.status_code == 301
    assert response.json() == url
