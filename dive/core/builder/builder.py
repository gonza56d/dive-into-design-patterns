from dataclasses import asdict

from dive.core.builder.cars import Car, CarBuilder
from dive.core.mongo_repo import MongoRepo


class Builder:

    repo = MongoRepo('cars')

    @staticmethod
    def build_car(owner_name: str):
        car = CarBuilder(owner_name=owner_name).car
        Builder.repo.write(asdict(car))

    @staticmethod
    def delete_car(owner_name: str):
        Builder.repo.delete({'owner_name': owner_name})

    @staticmethod
    def get_car(owner_name: str) -> Car:
        result = Builder.repo.read({'owner_name': owner_name})
        return Car(**result)
