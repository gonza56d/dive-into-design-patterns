from dive.core.abstract_factory.abstract import Chair, CoffeeTable, Factory, Sofa
from dive.core.abstract_factory.furniture import (
    ModernChair,
    ModernCoffeeTable,
    ModernSofa,
    VictorianChair,
    VictorianCoffeeTable,
    VictorianSofa
)


class VictorianFactory(Factory):

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


class ModernFactory(Factory):

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

    def create_sofa(self) -> Sofa:
        return ModernSofa()
