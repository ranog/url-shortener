from pydantic import BaseModel, HttpUrl, ValidationError

from src.exceptions import LongUrlError


class UrlTemplate(BaseModel):
    url: HttpUrl


async def validate(long_url: str):
    try:
        valid_url = UrlTemplate(url=long_url)
    except ValidationError:
        raise LongUrlError(long_url)
    return valid_url.url
