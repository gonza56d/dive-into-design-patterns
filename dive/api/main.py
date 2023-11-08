"""Main module to run the FastAPI application."""

from fastapi import FastAPI

from dive.api.routers.hello_world import hello_world


app = FastAPI()
app.include_router(hello_world)
