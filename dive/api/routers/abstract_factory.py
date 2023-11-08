"""FastAPI routers for abstract factory implementing furniture factory."""

from fastapi import APIRouter

from dive.api.io.serializers import OFurniture
from dive.core.abstract_factory.main import Main

abstract_factory = APIRouter(prefix='/abstract_factory', tags=['abstract_factory'])


@abstract_factory.get('')
async def get_furniture(my_age: int) -> OFurniture:
    factory = Main(my_age)
    chair, coffee_table, sofa = factory.order_furniture()
    return OFurniture(
        chair=chair.__class__.__name__,
        coffee_table=coffee_table.__class__.__name__,
        sofa=sofa.__class__.__name__
    )
