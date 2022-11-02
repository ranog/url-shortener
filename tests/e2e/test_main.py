from httpx import AsyncClient

from src.main import app


async def test_it_should_ping_successfully():
    async with AsyncClient(app=app, base_url='http://test') as aysnc_client:
        response = await aysnc_client.get('/v1/ping/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}
