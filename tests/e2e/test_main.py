from httpx import AsyncClient


async def test_it_should_ping_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}


async def test_it_should_shorten_successfully(async_http_client: AsyncClient):
    response = await async_http_client.post('/v1/data/shorten/', json={})
    assert response.status_code == 200


async def test_it_should_short_url_successfully(async_http_client: AsyncClient):
    response = await async_http_client.get('/v1/short_url/')
    assert response.status_code == 301
