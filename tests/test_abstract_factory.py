from fastapi.testclient import TestClient
import pytest

from dive.api.main import app


class TestAbstractFactory:

    def setup_method(self) -> None:
        self.client = TestClient(app)
        self.url = '/abstract_factory'

    @pytest.mark.parametrize('request_age', [18, 34, 61, 74])
    def test_get_furniture_success(self, request_age: int):
        response = self.client.get(self.url, params={'my_age': request_age})

        assert response.status_code == 200
        assert response.json() == {
            'chair': 'ModernChair',
            'coffee_table': 'ModernCoffeeTable',
            'sofa': 'ModernSofa'
        } if request_age < 60 else {
            'chair': 'VictorianChair',
            'coffee_table': 'VictorianCoffeeTable',
            'sofa': 'VictorianSofa'
        }

    @pytest.mark.parametrize('request_age', [None, 'not a number'])
    def test_get_furniture_bad_request(self, request_age):
        response = self.client.get(self.url, params={'my_age': request_age} if request_age else request_age)
        assert response.status_code == 422
