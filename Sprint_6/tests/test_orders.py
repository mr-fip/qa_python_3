import allure
import pytest

@allure.feature('Оформление заказа')
class TestOrderFlow:
    @pytest.mark.parametrize("entry_point,personal_info,rent_info", [
        ('header', {
            'name': 'Иван',
            'last_name': 'Иванов',
            'address': 'ул. Пушкина, 10',
            'metro': 'Сокольники',
            'phone': '+79991234567'
        }, {
            'date': '2024-03-15',
            'period': 'сутки', 
            'color': 'black',
            'comment': 'Тестовый заказ'
        })
    ])
    
    def test_order_flow(self, order_page, entry_point, personal_info, rent_info, home_page):
        home_page.open_order_page(entry_point)
        order_page.fill_personal_info(**personal_info)
        order_page.fill_rent_info(**rent_info)
        order_page.confirm_order()
        assert 'Заказ оформлен' in order_page.get_success_message()