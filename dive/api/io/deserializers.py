"""Pydantic classes to deserialize inputs to the API."""

from typing import Callable

from pydantic import BaseModel

from dive.core.builder.cars import CarBuilder


class UpdateCar(BaseModel):

    command: str
    value: str | None = None

    def _get_command(self) -> Callable:
        commands = {
            'set_color': CarBuilder().set_color,
            'set_tires': CarBuilder().set_tires,
            'set_engine': CarBuilder().set_engine,
            'set_roof': CarBuilder().set_roof,
            'set_air_conditioner': CarBuilder().set_air_conditioner,
            'set_stereo': CarBuilder().set_stereo,
            'set_gps': CarBuilder().set_gps,
            'set_auto_transmission': CarBuilder().set_auto_transmission,
            'set_smart_tv': CarBuilder().set_smart_tv,
            'set_skylight': CarBuilder().set_skylight,
            'set_airbarg': CarBuilder().set_airbarg,
            'set_vin': CarBuilder().set_vin,
            'set_spoiler': CarBuilder().set_spoiler,
            'set_neon_lights': CarBuilder().set_neon_lights,
            'set_xenon_headlights': CarBuilder().set_xenon_headlights,
            'set_custom_exhaust': CarBuilder().set_custom_exhaust
        }
        return commands[self.command]
