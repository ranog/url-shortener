from hashlib import blake2b

from src.url_shortening import shorten_url


async def test_it_should_shorten_the_url():
    long_url = 'http://www.example.com'
    short_url = await shorten_url(long_url)
    assert len(long_url) > len(short_url)


async def test_it_should_return_the_shortened_URL():
    long_url = 'http://w.co'
    short_url = await shorten_url(long_url)
    assert short_url == blake2b(long_url.encode(), digest_size=4).hexdigest()
