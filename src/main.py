from fastapi import FastAPI


app = FastAPI()


@app.get('/v1/ping/')
async def root():
    return {'ping': 'pong'}
