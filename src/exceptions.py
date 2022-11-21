class URLError(Exception):
    pass


class LongUrlError(URLError):
    def __init__(self, long_url: str) -> None:
        super().__init__(f'{long_url} is not a valid url')


class ShortUrlError(URLError):
    def __init__(self, short_url: str) -> None:
        super().__init__(f'{short_url} does not exist in repository')
