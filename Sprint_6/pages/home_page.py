from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def accept_cookies(self):
        self.click(BasePageLocators.COOKIE_BANNER)

    def click_question(self, index: int):
        questions = self.find_all(HomePageLocators.QUESTION)
        self.click(questions[index])

    def get_answer_text(self, index: int) -> str:
        answers = self.find_all(HomePageLocators.ANSWER)
        return self.get_text(answers[index])

    def click_order_button(self, position: str = 'header'):
        locator = HomePageLocators.ORDER_BUTTON_HEADER if position == 'header' else HomePageLocators.ORDER_BUTTON_FOOTER
        self.click(locator)

    def click_scooter_logo(self):
        self.click(BasePageLocators.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(BasePageLocators.YANDEX_LOGO)

    def is_current_url(self, url: str) -> bool:
        return self.driver.current_url == url

    def get_current_window(self) -> str:
        return self.driver.current_window_handle

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        new_window = [window for window in self.driver.window_handles 
                     if window != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

    def is_url_contains(self, text: str) -> bool:
        return text in self.driver.current_url

    def close_and_switch_to_window(self, original_window: str):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    def open_order_page(self, entry_point: str):
        self.click_order_button(entry_point)
        self.wait.until(EC.url_contains("/order"))