from uuid import uuid4

from google.cloud import firestore

from src.url_shortening import shorten_url


COLLECTION_NAME = 'testing-url-shortener'


class UrlShortenerRepository:
    def __init__(self):
        self.collection = firestore.AsyncClient().collection(COLLECTION_NAME)

    async def add(self, url: str):
        url_data = {'id': str(uuid4()), 'long_url': url, 'short_url': await shorten_url(url)}
        await self.collection.document(url_data['id']).set(url_data)

    async def get(self, short_url: str):
        data = self.collection.where(field_path='short_url', op_string='==', value=short_url)
        url_data = await data.get()
        return url_data[0].to_dict()['long_url']
