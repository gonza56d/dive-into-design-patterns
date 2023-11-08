from abc import ABC, abstractmethod


class Chair(ABC):
    pass


class CoffeeTable(ABC):
    pass


class Sofa(ABC):
    pass


class Factory(ABC):

    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass
