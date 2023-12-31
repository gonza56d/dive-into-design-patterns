from dataclasses import dataclass
from enum import Enum



class Color(str, Enum):
    """Color options for car."""
    BLUE = 'BLUE'
    RED = 'RED'
    YELLOW = 'YELLOW'
    ORANGE = 'ORANGE'
    GREEN = 'GREEN'
    PURPLE = 'PURPLE'
    GREY = 'GREY'
    BLACK = 'BLACK'
    WHITE = 'WHITE'


class CarTires(str, Enum):
    """Tires brand options for car."""
    BRIDGESTONE = 'BRIDGESTONE'
    PIRELLI = 'PIRELLI'
    MICHELIN = 'MICHELIN'


class CarEngine(str, Enum):
    """Engine type options for a car."""
    LINE_FOUR = 'LINE_FOUR'
    LINE_FIVE = 'LINE_FIVE'
    LINE_SIX = 'LINE_SIX'
    V_FOUR = 'V_FOUR'
    V_SIX = 'V_SIX'
    V_EIGHT = 'V_EIGHT'
    ELECTRIC = 'ELECTRIC'


class CarRoof(str, Enum):
    """Roof type options for a car."""
    REGULAR = 'REGULAR'
    CONVERTIBLE = 'CONVERTIBLE'
    OPEN_TOP = 'OPEN_TOP'


@dataclass
class Car:

    owner_name: str
    color: Color | None = None
    tires: CarTires | None = None
    engine: CarEngine | None = None
    roof: CarRoof = CarRoof.OPEN_TOP
    air_conditioner: bool = False
    stereo: bool = False
    gps: bool = False
    auto_transmission: bool = False
    smart_tv: bool = False
    skylight: bool = False
    airbag: bool = False
    vin: str | None = None
    spoiler: bool = False
    neon_lights: Color | None = None
    xenon_headlights: bool = False
    custom_exhaust: bool = False


class CarBuilder:
    
    def __init__(self, owner_name: str | None = None, **initial_state) -> None:
        self.car = Car(owner_name=owner_name, **initial_state) if owner_name is not None else None

    def _get_enum_option(self, option: str | Enum, enum_: Enum) -> Enum:
            if isinstance(option, Enum):
                return option
            try:
                return enum_(option)
            except ValueError:
                raise ValueError(
                    f'"{option}" is not a valid option for {enum_.__class__.__name__}.\n'
                    f'Try one of the following: {",".join(k for k in dict(enum_.__members__).keys())}.'
                )

    def set_color(self, color: str | Color) -> None:
        self.car.color = self._get_enum_option(color, Color)

    def set_tires(self, tires: str | CarTires) -> None:
        self.car.tires = self._get_enum_option(tires, CarTires)

    def set_engine(self, engine: str | CarEngine) -> None:
        self.car.color = self._get_enum_option(engine, CarEngine)

    def set_roof(self, roof: str | CarRoof) -> None:
        self.car.roof = self._get_enum_option(roof, CarRoof)

    def set_air_conditioner(self) -> None:
        self.car.air_conditioner = True

    def set_stereo(self) -> None:
        self.car.stereo = True

    def set_gps(self) -> None:
        self.car.gps = True

    def set_auto_transmission(self) -> None:
        self.car.auto_transmission = True

    def set_smart_tv(self) -> None:
        self.car.smart_tv = True

    def set_skylight(self) -> None:
        self.car.skylight = True

    def set_airbarg(self) -> None:
        self.car.airbag = True

    def set_vin(self, vin: str) -> None:
        self.car.vin = vin

    def set_spoiler(self) -> None:
        self.car.spoiler = True

    def set_neon_lights(self, color: str | Color) -> None:
        self.car.neon_lights = self._get_enum_option(color, Color)

    def set_xenon_headlights(self) -> None:
        self.car.xenon_headlights = True

    def set_custom_exhaust(self) -> None:
        self.car.custom_exhaust = True
