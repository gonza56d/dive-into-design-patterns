from abc import ABC, abstractmethod

from dive.core.builder.instruments import Guitar, Instrument
from dive.core.builder.parts import Color, GuitarBridge, GuitarPickup


class InstrumentBuilder(ABC):

    def __init__(self, instrument: Instrument):
        self.instrument = instrument

    @abstractmethod
    def set_model_name(self, name: str) -> None:
        pass

    @abstractmethod
    def paint(self, color: str) -> None:
        pass

    @abstractmethod
    def finish_assembly(self, *args) -> None:
        pass


class GuitarBuilder(InstrumentBuilder):

    def __init__(self, instrument: Guitar):
        self.instrument = instrument
        super().__init__(instrument)

    def set_model_name(self, name: str) -> None:
        self.instrument.model_name = f'Guitar {name}'

    def paint(self, color: str) -> None:
        try:
            selected_color = Color(color)
        except ValueError:
            raise ValueError(f'Color {color} not available.')
        self.instrument.color = selected_color

    def finish_assembly(
            self,
            strings: int,
            pickups: [GuitarPickup],
            bridge: GuitarBridge
    ) -> None:
        self.instrument.strings = 6
        self.instrument.pickups = pickups
        self.instrument.bridge = bridge
