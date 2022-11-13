async def shorten_url(url: str):
    short_url = f'{id(url):x}'
    if len(url) <= len(short_url):
        return url
    return short_url
