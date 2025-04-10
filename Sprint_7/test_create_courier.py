import pytest
import requests
import allure
from helpers import generate_random_string
from data.urls import COURIER_URL
from data.messages import DUPLICATE_ERROR, MISSING_FIELDS_CREATE

@allure.feature("Создание курьера")
class TestCreateCourier:
    @allure.title("Успешное создание курьера")
    def test_create_success(self):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10), "firstName": generate_random_string(10)}
        response = requests.post(COURIER_URL, data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание дубликата")
    def test_create_duplicate(self, courier):
        login, password, first_name = courier
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(COURIER_URL, data=payload)
        assert response.status_code == 409
        assert response.json()["message"] == DUPLICATE_ERROR

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("Отсутствие обязательного поля: {field}")
    def test_missing_field(self, field):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10), "firstName": generate_random_string(10)}
        del payload[field]
        response = requests.post(COURIER_URL, data=payload)
        assert response.status_code == 400
        assert response.json()["message"] == MISSING_FIELDS_CREATE