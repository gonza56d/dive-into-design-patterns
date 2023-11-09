from fastapi.testclient import TestClient
import pytest

from dive.api.main import app


class TestAbstractFactory:

    def setup_method(self) -> None:
        self.client = TestClient(app)
        self.url = '/hello_world'

    @pytest.mark.parametrize('request_name', [None, 'Gonza'])
    def test_hello_world_success(self, request_name: str):
        response = self.client.get(self.url, params={'my_name': request_name} if request_name else None)

        my_name = request_name or 'guest'
        assert response.status_code == 200
        assert response.json() == {
            'message': (
                f'Hi {my_name}, greetings from Dive API! '
                'You\'re seeing our hello world response :) '
                'I hope you learn a lot about classic patterns to improve your dev skills!'
            )
        }
