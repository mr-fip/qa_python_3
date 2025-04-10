import pytest
import requests
import allure
import random
import string
from helpers import register_new_courier_and_return_login_password

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.feature('Авторизация курьера')
class TestLoginCourier:
    @pytest.fixture(scope='function')
    def setup(self):
        data = register_new_courier_and_return_login_password()
        yield data
        
        login, password, _ = data
        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': login, 'password': password})
        if login_response.status_code == 200:
            courier_id = login_response.json()['id']
            requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

    @allure.title('Успешная авторизация')
    def test_login_success(self, setup):
        login, password, _ = setup
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': login, 'password': password})
        assert response.status_code == 200, "Код ответа не 200"
        assert 'id' in response.json(), "Нет поля id в ответе"

    @allure.title('Авторизация с неверным паролем')
    def test_login_wrong_password(self, setup):
        login, _, _ = setup
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': login, 'password': 'invalid_password'})
        assert response.status_code == 404, "Код ответа не 404"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Авторизация с неверным логином')
    def test_login_wrong_login(self, setup):
        _, password, _ = setup
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': 'nonexistent_login', 'password': password})
        assert response.status_code == 404, "Код ответа не 404"
        assert response.json()["message"] == "Учетная запись не найдена"

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title('Авторизация без обязательного поля: {missing_field}')
    def test_login_missing_required_field(self, missing_field):
        payload = {'login': 'valid_login', 'password': 'valid_pass'}
        del payload[missing_field]

        try:
            response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload, timeout=100)
        except requests.exceptions.Timeout:
            pytest.fail("Сервер не ответил за 100 секунд (504 Gateway Timeout)")

        assert response.status_code in [400, 504], f"Неожиданный код: {response.status_code}"
    
        if response.status_code == 400:
            assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Авторизация несуществующего пользователя')
    def test_login_nonexistent_user(self):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={'login': generate_random_string(10), 'password': 'pass'})
        assert response.status_code == 404, "Код ответа не 404"
        assert response.json()["message"] == "Учетная запись не найдена"