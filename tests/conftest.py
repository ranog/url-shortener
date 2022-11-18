import pytest
from google.cloud import firestore
from httpx import AsyncClient

from src.main import app


@pytest.fixture
async def async_http_client() -> AsyncClient:
    async with AsyncClient(app=app, base_url='http://test') as async_client:
        yield async_client


@pytest.fixture
def clean_collection():
    async def _clean_collection(collection_path, async_client=firestore.AsyncClient()):
        async_collection_reference = async_client.collection(collection_path)
        await async_client.recursive_delete(reference=async_collection_reference)

    return _clean_collection
