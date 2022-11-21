from fastapi import FastAPI
from fastapi.responses import Response

from src.url_shortener_repository import UrlShortenerRepository
from src.url_shortening import shorten_url
from src.url_validator import validate


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/data/shorten/')
async def shorten(json: dict):
    long_url = json.get('long_url')
    await validate(long_url)
    await UrlShortenerRepository().add(long_url)
    return await shorten_url(long_url)


@app.get('/v1/{short_url}/', status_code=301)
async def short(short_url: str):
    return Response(headers={'location': await UrlShortenerRepository().get_long_url(short_url)}, status_code=301)
