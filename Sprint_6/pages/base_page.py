from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Поиск элемента {locator}")
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Поиск всех элементов {locator}")
    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step("Клик по элементу")
    def click(self, element_or_locator):
        if isinstance(element_or_locator, tuple):
            self.find(element_or_locator).click()
        else:
            element_or_locator.click()

    @allure.step("Получить текущее окно")
    def get_current_window(self) -> str:
        return self.driver.current_window_handle

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def input(self, locator, text):
        self.find(locator).send_keys(text)

    @allure.step("Получить текст элемента или локатора")
    def get_text(self, element_or_locator):
        return self.find(element_or_locator).text if isinstance(element_or_locator, tuple) else element_or_locator.text

    @allure.step("Выбрать опцию из выпадающего списка {locator}")
    def select_dropdown_option(self, locator):
        self.click(locator)

    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self):
        self.wait.until(EC.number_of_windows_to_be(2))
        new_window = [w for w in self.driver.window_handles 
                     if w != self.driver.current_window_handle][0]
        self.driver.switch_to.window(new_window)

    @allure.step("Проверить наличие текста '{text}' в URL")
    def is_url_contains(self, text: str) -> bool:
        return text in self.driver.current_url
    
    @allure.step("Закрыть окно и вернуться к исходному")
    def close_and_switch_to_window(self, original_window: str):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    @allure.step("Проверить соответствие текущего URL паттерну '{pattern}'")
    def is_current_url_matches(self, pattern: str) -> bool:
        return pattern in self.driver.current_url
