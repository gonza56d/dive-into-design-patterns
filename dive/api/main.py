"""Main module to run the FastAPI application."""

from fastapi import FastAPI

from dive.api.routers import abstract_factory, hello_world


app = FastAPI()
app.include_router(abstract_factory)
app.include_router(hello_world)
