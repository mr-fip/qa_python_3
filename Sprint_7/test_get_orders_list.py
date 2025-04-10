import requests
import allure
from data.urls import ORDERS_URL

@allure.feature("Список заказов")
class TestOrdersList:
    @allure.title("Получение списка")
    def test_get_orders(self):
        response = requests.get(ORDERS_URL)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)