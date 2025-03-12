from .base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
        try:
            rental_period = self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD)
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", rental_period)
            rental_period.click()
            
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//div[@class='Dropdown-menu']")
                )
            )
            period_locator = (OrderPageLocators.RENTAL_PERIOD_OPTION[0], 
                              OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period))
            option = self.wait.until(
                EC.element_to_be_clickable(period_locator)
            )
            self.driver.execute_script("arguments[0].click();", option)

        except Exception as e:
            self.driver.save_screenshot("period_selection_error.png")
            raise
    
    @allure.step("Клик по телу страницы")
    def click_body(self):
        body = self.find((By.TAG_NAME, 'body'))
        self.click(body)

    @allure.step("Выбор цвета: {color}")
    def _select_color(self, color: str):
        self.click(OrderPageLocators.COLOR_CHECKBOX)

    @allure.step("Выбор станции метро: {metro}")
    def _select_metro(self, metro: str):
        self.click(OrderPageLocators.METRO_STATION)
        self.click((By.XPATH, f"//div[text()='{metro}']"))

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получение сообщения об успешном заказе")
    def get_success_message(self) -> str:
        return self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
