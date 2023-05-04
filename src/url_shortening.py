from hashlib import blake2b


async def shorten_url(long_url: str):
    return blake2b(long_url.encode(), digest_size=4).hexdigest()
