class URLError(Exception):
    pass


class LongUrlError(URLError):
    def __init__(self, long_url: str) -> None:
        super().__init__(f'{long_url} is not a valid url')
