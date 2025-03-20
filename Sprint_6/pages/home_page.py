from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators
import allure

class HomePage(BasePage):
    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click(BasePageLocators.COOKIE_BANNER)

    @allure.step("Нажать на вопрос №{index}")
    def click_question(self, index: int):
        question_locator = (HomePageLocators.QUESTION[0], f"{HomePageLocators.QUESTION[1]}[{index + 1}]")
        self.click_with_actions(question_locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, index: int) -> str:
        answers = self.find_all(HomePageLocators.ANSWER)
        return self.get_text(answers[index])

    @allure.step("Нажать кнопку заказа ({position})")
    def click_order_button(self, position: str = 'header'):
        locator = (HomePageLocators.ORDER_BUTTON_HEADER if position == 'header' else HomePageLocators.ORDER_BUTTON_FOOTER)
        self.click(locator)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса")
    def click_yandex_logo(self):
        self.click(BasePageLocators.YANDEX_LOGO)