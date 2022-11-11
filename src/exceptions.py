class URLError(Exception):
    pass


class InvalidUrl(URLError):
    def __init__(self, url: str) -> None:
        super().__init__(f'{url} is not valid')
