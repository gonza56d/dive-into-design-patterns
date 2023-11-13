"""FastAPI routers for builder implementing car building."""

from fastapi import APIRouter

from dive.api.io.deserializers import UpdateCar
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


@builder.patch('/{owner_name}')
async def update_car(owner_name: str, update_car: UpdateCar) -> Car:
    car = Builder.update_car(owner_name=owner_name, update_car=update_car)
    return car
