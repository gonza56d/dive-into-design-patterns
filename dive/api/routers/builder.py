"""FastAPI routers for builder implementing car building."""

from fastapi import APIRouter

from dive.core.builder.builder import Builder
from dive.core.builder.cars import Car


builder = APIRouter(prefix='/builder', tags=['builder'])


@builder.post('/{owner_name}', status_code=201)
async def create_car(owner_name: str):
    Builder.build_car(owner_name)


@builder.delete('/{owner_name}', status_code=204)
async def delete_car(owner_name: str):
    Builder.delete_car(owner_name)


@builder.get('/{owner_name}')
async def get_car(owner_name: str) -> Car:
    car = Builder.get_car(owner_name=owner_name)
    return car
