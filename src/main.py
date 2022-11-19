from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.url_shortener_repository import UrlShortenerRepository
from src.url_shortening import shorten_url
from src.url_validator import validate


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/data/shorten/')
async def shorten(json: dict):
    url = json.get('long_url')
    await validate(url)
    await UrlShortenerRepository().add(url)
    return await shorten_url(url)


@app.get('/v1/{short_url}/', status_code=301)
async def short(short_url: str):
    url_data = await UrlShortenerRepository().get(short_url)
    return RedirectResponse(url_data[0]['long_url'], status_code=301)
