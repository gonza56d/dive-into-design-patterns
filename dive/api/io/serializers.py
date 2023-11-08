"""Pydantic classes to serialize outputs from the API."""

from pydantic import BaseModel

from dive.core.abstract_factory.abstract import Chair, CoffeeTable, Sofa


class OHelloWorld(BaseModel):
    """Serialize hello world request."""

    message: str


class OFurniture(BaseModel):
    """Serialize get furniture request."""

    chair: str
    coffee_table: str
    sofa: str
