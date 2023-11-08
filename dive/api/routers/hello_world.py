"""FastAPI routers for hello world."""

from fastapi import APIRouter

from dive.api.io.serializers import OHelloWorld


hello_world = APIRouter(prefix='/hello_world', tags=['hello_world'])


@hello_world.get('')
async def get_hello_world(my_name: str = 'guest') -> OHelloWorld:
    """Get greeting from Dive API."""
    return OHelloWorld(
        message=(
            f'Hi {my_name}, greetings from Dive API! '
            'You\'re seeing our hello world response :) '
            'I hope you learn a lot about classic patterns to improve your dev skills!'
        )
    )
