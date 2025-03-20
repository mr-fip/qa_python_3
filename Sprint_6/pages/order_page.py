from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step("Заполнение информации о аренде с датой: {date}, периодом: {period}, цветом: {color}, комментарием: {comment}")
    def fill_rent_info(self, date: str, period: str, color: str, comment: str):
        self.input(OrderPageLocators.DATE, date)
        self.click_body()
        self._select_rental_period(period)
        self._select_color(color)
        self.input(OrderPageLocators.COMMENT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Заполнение личной информации с именем: {name}, фамилией: {last_name}, адресом: {address}, станцией метро: {metro}, телефоном: {phone}")
    def fill_personal_info(self, name: str, last_name: str, address: str, metro: str, phone: str):
        self.input(OrderPageLocators.NAME, name)
        self.input(OrderPageLocators.LAST_NAME, last_name)
        self.input(OrderPageLocators.ADDRESS, address)
        self._select_metro(metro)
        self.input(OrderPageLocators.PHONE, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Выбор периода аренды: {period}")
    def _select_rental_period(self, period: str):
        self.click_with_actions(OrderPageLocators.RENTAL_PERIOD)
        self.wait_visibility_of_element(OrderPageLocators.DROPDOWN_MENU)
        period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0], OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period))
        self.click_with_actions(period_locator)
    
    @allure.step("Клик по телу страницы")
    def click_body(self):
        body = self.find(OrderPageLocators.BODY)
        self.click(body)

    @allure.step("Выбор цвета: {color}")
    def _select_color(self, color: str):
        self.click(OrderPageLocators.COLOR_CHECKBOX)

    @allure.step("Выбор станции метро: {metro}")
    def _select_metro(self, metro: str):
        self.click(OrderPageLocators.METRO_STATION)
        metro_locator = (OrderPageLocators.METRO_STATION_OPTION[0], OrderPageLocators.METRO_STATION_OPTION[1].format(metro))
        self.click(metro_locator)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self) -> str:
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
