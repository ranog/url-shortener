from src.url_shortener_repository import COLLECTION_NAME, UrlShortenerRepository
from src.url_shortening import shorten_url


async def test_it_should_persist_in_firestore(clean_collection):
    await clean_collection(COLLECTION_NAME)
    url = 'http://www.example.com'
    short_url = await shorten_url(url)
    url_shortener_repository = UrlShortenerRepository()
    await url_shortener_repository.add(url)
    long_url = await url_shortener_repository.get(short_url)
    assert long_url == url
