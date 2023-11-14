"""Main module to run the FastAPI application."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from dive.api.routers import abstract_factory, builder, hello_world
from dive.core.exceptions import ClientError


app = FastAPI()
app.include_router(abstract_factory)
app.include_router(builder)
app.include_router(hello_world)

@app.exception_handler(Exception)
async def exception_handler(request: Request, err: Exception) -> JSONResponse:
    if isinstance(err, ClientError):
        return JSONResponse(
            status_code=err.status_code,
            content={'error_message': err.message}
        )
    return JSONResponse(
        status_code=err.status_code if hasattr(err, 'status_code') else 500,
        content={'error_message': err.message if hasattr(err, 'message') else 'Internal server error.'}
    )
