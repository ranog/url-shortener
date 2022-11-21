from google.cloud import firestore

from src.exceptions import ShortUrlError
from src.url_shortening import shorten_url


COLLECTION_NAME = 'testing-url-shortener'


class UrlShortenerRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    async def add(self, long_url: str):
        url_data = {'long_url': long_url, 'short_url': await shorten_url(long_url)}
        await self.collection.document(str(id(long_url))).set(url_data)

    async def get_long_url(self, short_url: str):
        url_data = await self.collection.where(field_path='short_url', op_string='==', value=short_url).get()
        try:
            return url_data[0].to_dict()['long_url']
        except IndexError:
            raise ShortUrlError(short_url)
