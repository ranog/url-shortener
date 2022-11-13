from src.url_shortening import shorten_url


async def test_it_should_shorten_the_url():
    long_url = 'http://www.example.com'
    short_url = await shorten_url(long_url)
    assert len(long_url) > len(short_url)


async def test_it_should_return_long_url_when_short_url_gets_larger_size():
    long_url = 'http://w.co'
    short_url = await shorten_url(long_url)
    assert long_url == short_url


async def test_it_should_return_the_long_url_when_the_short_url_is_equal_in_length():
    long_url = 'http://w.com'
    short_url = await shorten_url(long_url)
    assert long_url == short_url
