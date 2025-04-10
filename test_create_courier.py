import pytest
import requests
import allure
import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

@allure.feature('Создание курьера')
class TestCreateCourier:
    @allure.title('Успешное создание курьера')
    def test_create_courier_success(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {"login": login, "password": password, "firstName": first_name}

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 201, "Код ответа не 201"
        assert response.json() == {"ok": True}, "Тело ответа не {'ok': true}"

        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={"login": login, "password": password})
        courier_id = login_response.json()["id"]
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

    @allure.title('Создание дубликата курьера')
    def test_create_duplicate_courier(self):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        payload = {"login": login, "password": password, "firstName": first_name}

        requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 409, "Код ответа не 409"
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

        login_response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data={"login": login, "password": password})
        courier_id = login_response.json()["id"]
        requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    @allure.title('Создание курьера без обязательного поля: {missing_field}')
    def test_create_courier_missing_required_field(self, missing_field):
        payload = {"login": generate_random_string(10), "password": generate_random_string(10), "firstName": generate_random_string(10)}

        del payload[missing_field]

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        assert response.status_code == 400, "Код ответа не 400"
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"