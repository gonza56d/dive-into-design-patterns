"""Pydantic classes to serialize outputs from the API."""

from pydantic import BaseModel


class OHelloWorld(BaseModel):
    """Serialize hello world request."""

    message: str
