import pytest
import requests
import random
import string
from data.urls import COURIER_URL

def generate_random_string(length: int) -> str:
    return "".join(random.choice(string.ascii_lowercase) for _ in range(length))

def register_new_courier() -> tuple[str, str, str]:
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    response = requests.post(COURIER_URL, data={"login": login, "password": password, "firstName": first_name})
    
    if response.status_code == 201:
        return (login, password, first_name)
    else:
        pytest.fail("Не удалось создать курьера")