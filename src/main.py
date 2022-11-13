from fastapi import FastAPI


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}


@app.post('/v1/data/shorten/')
async def shorten(json: dict):
    # validador de URL      OK
    # encurtador de URL     OK
    # Salvar no database    NOK
    pass


@app.get('/v1/{short_url}/', status_code=301)
async def short(short_url: str):
    pass
