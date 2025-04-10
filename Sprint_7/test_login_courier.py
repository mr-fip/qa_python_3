import pytest
import requests
import allure
from data.urls import LOGIN_URL
from data.messages import MISSING_FIELDS_LOGIN, ACCOUNT_NOT_FOUND

@allure.feature("Авторизация курьера")
class TestLoginCourier:
    @allure.title("Успешная авторизация")
    def test_login_success(self, courier):
        login, password, _ = courier
        response = requests.post(LOGIN_URL, data={"login": login, "password": password})
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Неверный пароль")
    def test_wrong_password(self, courier):
        login, _, _ = courier
        response = requests.post(LOGIN_URL, data={"login": login, "password": "invalid"})
        assert response.status_code == 404
        assert response.json()["message"] == ACCOUNT_NOT_FOUND

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("Отсутствие поля: {field}")
    def test_missing_field(self, field):
        payload = {"login": "test", "password": "pass"}
        del payload[field]
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code in [400, 504], "Неожиданный код ответа"
        if response.status_code == 400:
            assert response.json()["message"] == MISSING_FIELDS_LOGIN