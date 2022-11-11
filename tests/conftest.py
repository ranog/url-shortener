import pytest
from httpx import AsyncClient

from src.main import app


@pytest.fixture
async def async_http_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as async_client:
        yield async_client
