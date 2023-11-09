from enum import Enum


class Color(str, Enum):
    NATURAL_WOOD = 'NATURAL_WOOD'
    BLACK = 'BLACK'
    WHITE = 'WHITE'
    RED = 'RED'
    BLUE = 'BLUE'
    YELLOW = 'YELLOW'
    ORANGE = 'ORANGE'
    PURPLE = 'PURPLE'
    GREEN = 'GREEN'


class GuitarBridge(Enum):
    FIXED = 'FIXED'
    TUNE_O_MATIC = 'TUNE_O_MATIC'
    FLOYD_ROSE = 'FLOYD_ROSE'


class GuitarPickup(Enum):
    SINGLE_COIL = 'SINGLE_COIL'
    HUMBUCKER = 'HUMBUCKER'
    P90 = 'P90'


class BassPickup(Enum):
    PRECISION = 'PRECISION'
    JAZZ = 'JAZZ'


class DrumSnare(Enum):
    METAL = 'METAL'
    WOOD = 'WOOD'


class BassDrumType(Enum):
    SINGLE = 'SINGLE'
    DOUBLE = 'DOUBLE'
    DOUBLE_PEDAL = 'DOUBLE_PEDAL'
