import pytest
import requests
import allure
from data.urls import ORDERS_URL
from data.test_data import BASE_ORDER

@allure.feature("Создание заказа")
class TestCreateOrder:
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Создание с цветом: {color}")
    def test_create_with_colors(self, color):
        order = BASE_ORDER.copy()
        order["color"] = color
        response = requests.post(ORDERS_URL, json=order)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание без цвета")
    def test_create_without_color(self):
        order = BASE_ORDER.copy()
        del order["color"]
        response = requests.post(ORDERS_URL, json=order)
        assert response.status_code == 201
        assert "track" in response.json()