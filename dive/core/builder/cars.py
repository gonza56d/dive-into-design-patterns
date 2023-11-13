from dataclasses import dataclass
from enum import auto, Enum


class Color(str, Enum):
    """Color options for car."""
    BLUE = auto()
    RED = auto()
    YELLOW = auto()
    ORANGE = auto()
    GREEN = auto()
    PURPLE = auto()
    GREY = auto()
    BLACK = auto()
    WHITE = auto()


class CarTires(str, Enum):
    """Tires brand options for car."""
    BRIDGESTONE = auto()
    PIRELLI = auto()
    MICHELIN = auto()


class CarEngine(str, Enum):
    """Engine type options for a car."""
    LINE_FOUR = auto()
    LINE_FIVE = auto()
    LINE_SIX = auto()
    V_FOUR = auto()
    V_SIX = auto()
    V_EIGHT = auto()
    ELECTRIC = auto()


class CarRoof(str, Enum):
    """Roof type options for a car."""
    REGULAR = auto()
    CONVERTIBLE = auto()
    OPEN_TOP = auto()


@dataclass
class Car:

    color: Color | None = None
    tires: CarTires | None = None
    engine: CarEngine | None = None
    roof: CarRoof = CarRoof.OPEN_TOP()
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


class CarFactory:
    
    def __init__(self) -> None:
        self.car = Car()

    def _get_enum_option(self, option: str | Enum, enum: Enum) -> Enum:
            if option(isinstance, Enum):
                return option
            try:
                return enum(option)
            except ValueError:
                raise ValueError(
                    f'"{option}" is not a valid option for {enum.__class__.__name__}.\n'
                    f'Try one of the following: {",".join(k for k in dict(enum.__members__).keys())}.'
                )

    def set_color(self, color: str | Color) -> None:
        option = self._get_enum_option(color, Color)
        self.car.color = option

    def set_tires(self, tires: str | CarTires) -> None:
        option = self._get_enum_option(tires, CarTires)
        self.car.tires = option
