from typing import Tuple

from dive.core.abstract_factory.abstract import Chair, CoffeeTable, Factory, Sofa
from dive.core.abstract_factory.factory import ModernFactory, VictorianFactory


class Main:

    def __init__(self, age: int):
        self.factory: Factory = VictorianFactory() if age > 60 else ModernFactory()

    def order_furniture(self) -> Tuple[Chair, CoffeeTable, Sofa]:
        return (
            self.factory.create_chair(),
            self.factory.create_coffee_table(),
            self.factory.create_sofa()
        )
