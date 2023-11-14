from dataclasses import asdict

from fastapi.testclient import TestClient
import pytest

from dive.api.main import app
from dive.core.builder.cars import Car, Color
from dive.core.exceptions import NotFound
from dive.core.mongo_repo import MongoRepo


class TestBuilder:

    def setup_method(self) -> None:
        self.client = TestClient(app)
        self.url = '/builder'
        self.owner_name = 'test_owner'
        MongoRepo('cars').clear_collection()

    def test_create_car_success(self):
        response = self.client.post(f'{self.url}/{self.owner_name}')

        assert response.status_code == 201

    def test_get_car_success(self):
        expected_car = Car(owner_name=self.owner_name)
        self.client.post(f'{self.url}/{self.owner_name}')

        response = self.client.get(f'{self.url}/{self.owner_name}')

        assert response.status_code == 200
        assert response.json() == asdict(expected_car)

    def test_get_car_not_found(self):
        with pytest.raises(NotFound):
            self.client.get(f'{self.url}/{self.owner_name}')

    def test_update_car_parts_success(self):
        expected_car = Car(owner_name=self.owner_name)
        self.client.post(f'{self.url}/{self.owner_name}')

        response = self.client.get(f'{self.url}/{self.owner_name}')
        assert response.json() == asdict(expected_car)

        self.client.patch(
            f'{self.url}/{self.owner_name}',
            json={'command': 'set_color', 'value': 'RED'},
        )
        expected_car.color = Color.RED
        response = self.client.get(f'{self.url}/{self.owner_name}')
        assert response.json() == asdict(expected_car)

        self.client.patch(
            f'{self.url}/{self.owner_name}',
            json={'command': 'set_air_conditioner'},
        )
        expected_car.air_conditioner = True
        response = self.client.get(f'{self.url}/{self.owner_name}')
        assert response.json() == asdict(expected_car)

        self.client.patch(
            f'{self.url}/{self.owner_name}',
            json={'command': 'set_vin', 'value': 'MY_TESTING_VIN'},
        )
        expected_car.vin = 'MY_TESTING_VIN'
        response = self.client.get(f'{self.url}/{self.owner_name}')
        assert response.json() == asdict(expected_car)
