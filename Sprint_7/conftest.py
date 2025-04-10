import pytest
import requests
from helpers import register_new_courier
from data.urls import LOGIN_URL, COURIER_URL

@pytest.fixture
def courier():
    login, password, first_name = register_new_courier()
    yield login, password, first_name
    response = requests.post(LOGIN_URL, data={"login": login, "password": password})
    if response.status_code == 200:
        courier_id = response.json()["id"]
        requests.delete(f"{COURIER_URL}/{courier_id}")