from dataclasses import dataclass, field

from dive.core.builder.parts import BassDrumType, BassPickup, Color, DrumSnare, GuitarBridge, GuitarPickup


@dataclass
class Guitar:

    model_name: str | None = None
    strings: int = 0
    color: Color = Color.NATURAL_WOOD
    pickups: list[GuitarPickup] = field(default_factory=list)
    bridge: GuitarBridge | None = None


@dataclass
class Bass:

    model_name: str | None = None
    strings: int = 0
    color: Color = Color.NATURAL_WOOD
    pickups: list[BassPickup] = field(default_factory=list)
    active_eq: bool = False


@dataclass
class Drums:

    model_name: str | None = None
    color: Color = Color.NATURAL_WOOD
    toms: int = 0
    snare_type: DrumSnare = None
    bass_drum_type: BassDrumType = None
