from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import allure

class BasePage():
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

    @allure.step("Ожидание URL, содержащего '{text}'")
    def wait_url_contains(self, text: str):
        return self.wait.until(EC.url_contains(text))
    
    @allure.step("Закрыть окно и вернуться к исходному")
    def close_and_switch_to_window(self, original_window: str):
        self.driver.close()
        self.driver.switch_to.window(original_window)

    @allure.step("Проверить соответствие текущего URL паттерну '{pattern}'")
    def is_current_url_matches(self, pattern: str) -> bool:
        return pattern in self.driver.current_url
    
    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ожидание видимости элемента по локатору")
    def wait_visibility_of_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидание количества окон: {num_windows}")
    def wait_for_number_of_windows(self, num_windows: int):
        return self.wait.until(EC.number_of_windows_to_be(num_windows))
    
    @allure.step("Получить текущий URL")
    def get_current_url(self) -> str:
        return self.driver.current_url
    
    @allure.step("Открыть страницу заказа")
    def open_order_page(self, entry_point: str):
        self.click_order_button(entry_point)
        self.wait.until(EC.url_contains("/order"))

    @allure.step("Проверить наличие текста '{text}' в URL")
    def is_url_contains(self, text: str) -> bool:
        return text in self.driver.current_url
    
    def click_element_with_scroll(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        self.scroll_to_element(element)
        self.click(element)

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_element_to_be_clickable(self, locator) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Клик после ожидания кликабельности элемента {locator}")
    def click_after_wait(self, locator):
        element = self.wait_element_to_be_clickable(locator)
        self.click(element)