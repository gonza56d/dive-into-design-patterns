"""Pydantic classes to deserialize inputs to the API."""

from typing import Callable

from pydantic import BaseModel

from dive.core.builder.cars import CarBuilder


class UpdateCar(BaseModel):

    command: str
    value: str | None = None

    def _get_command(self, car_builder: CarBuilder) -> Callable:
        commands = {
            'set_color': car_builder.set_color,
            'set_tires': car_builder.set_tires,
            'set_engine': car_builder.set_engine,
            'set_roof': car_builder.set_roof,
            'set_air_conditioner': car_builder.set_air_conditioner,
            'set_stereo': car_builder.set_stereo,
            'set_gps': car_builder.set_gps,
            'set_auto_transmission': car_builder.set_auto_transmission,
            'set_smart_tv': car_builder.set_smart_tv,
            'set_skylight': car_builder.set_skylight,
            'set_airbarg': car_builder.set_airbarg,
            'set_vin': car_builder.set_vin,
            'set_spoiler': car_builder.set_spoiler,
            'set_neon_lights': car_builder.set_neon_lights,
            'set_xenon_headlights': car_builder.set_xenon_headlights,
            'set_custom_exhaust': car_builder.set_custom_exhaust
        }
        return commands[self.command]
