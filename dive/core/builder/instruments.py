from abc import ABC
from dataclasses import dataclass, field

from dive.core.builder.parts import BassDrumType, BassPickup, Color, DrumSnare, GuitarBridge, GuitarPickup


class Instrument(ABC):

    model_name: str | None = None
    color: Color = Color.NATURAL_WOOD


@dataclass
class Guitar(Instrument):

    strings: int = 0
    pickups: list[GuitarPickup] = field(default_factory=list)
    bridge: GuitarBridge | None = None


@dataclass
class Bass(Instrument):

    strings: int = 0
    pickups: list[BassPickup] = field(default_factory=list)
    active_eq: bool = False


@dataclass
class Drums(Instrument):

    toms: int = 0
    snare_type: DrumSnare = None
    bass_drum_type: BassDrumType = None
