from src.url_shortener_repository import COLLECTION_NAME, UrlShortenerRepository
from src.url_shortening import shorten_url


async def test_it_should_persist_in_firestore(clean_collection):
    await clean_collection(COLLECTION_NAME)
    url = 'http://www.example.com'
    short_url = await shorten_url(url)
    expected_result = {
        'long_url': url,
        'short_url': short_url,
    }

    url_shortener_repository = UrlShortenerRepository()
    await url_shortener_repository.add(url)
    response = await url_shortener_repository.get(short_url)
    assert response == expected_result
