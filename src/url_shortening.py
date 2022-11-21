import hashlib


async def shorten_url(long_url: str):
    return hashlib.blake2b(long_url.encode(), digest_size=4).hexdigest()
