import hashlib


async def shorten_url(url: str):
    return hashlib.blake2b(url.encode(), digest_size=4).hexdigest()
