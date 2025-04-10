import requests
import allure

@allure.feature('Список заказов')
class TestGetOrdersList:
    @allure.title('Получение списка заказов')
    def test_get_orders_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')
        assert response.status_code == 200, "Ожидался код 200"
        
        response_data = response.json()
        assert "orders" in response_data, "Ключ 'orders' отсутствует в ответе"
        assert isinstance(response_data["orders"], list), "'orders' не является списком"
        
        if len(response_data["orders"]) > 0:
            required_fields = ["id", "track", "status", "firstName", "lastName", "address"]
            for order in response_data["orders"]:
                for field in required_fields:
                    assert field in order, f"Поле {field} отсутствует в заказе"