from pydantic import BaseModel, HttpUrl, ValidationError

from src.exceptions import InvalidUrl


class UrlTemplate(BaseModel):
    url: HttpUrl


def validate(url: str):
    try:
        valid_url = UrlTemplate(url=url)
    except ValidationError:
        raise InvalidUrl(url)
    return valid_url.url
