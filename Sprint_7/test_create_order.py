import pytest
import requests
import allure

@allure.feature('Создание заказа')
class TestCreateOrder:
    BASE_ORDER_DATA = {
        'firstName': 'Рокси',
        'lastName': 'Фиксик',
        'address': 'Москва',
        'metroStation': 1,
        'phone': '+79999999999',
        'rentTime': 1,
        'deliveryDate': '2023-10-10',
        'comment': 'Комментарий',
        'color': []
    }

    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.title('Создание заказа с цветом: {color}')
    def test_create_order_with_colors(self, color):
        order_data = self.BASE_ORDER_DATA.copy()
        order_data['color'] = color
        
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_data)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title('Создание заказа без указания цвета (поле отсутствует)')
    def test_create_order_without_color_field(self):
        order_data = self.BASE_ORDER_DATA.copy()
        if 'color' in order_data:
            del order_data['color']
        
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=order_data)
        assert response.status_code == 201
        assert 'track' in response.json()