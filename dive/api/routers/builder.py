"""FastAPI routers for builder implementing car building."""

from fastapi import APIRouter

from dive.core.builder.builder import Builder


builder = APIRouter(prefix='/builder', tags=['builder'])


@builder.post('/{owner_name}')
async def create_car(owner_name: str):
    Builder.build_car(owner_name)


@builder.delete('/{owner_name}')
async def delete_car(owner_name: str):
    Builder.delete_car(owner_name)

