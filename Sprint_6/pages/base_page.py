from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, element_or_locator):
        if isinstance(element_or_locator, tuple):
            self.find(element_or_locator).click()
        else:
            element_or_locator.click()

    def input(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, element_or_locator):
        return self.find(element_or_locator).text if isinstance(element_or_locator, tuple) else element_or_locator.text

    def is_current_url_matches(self, pattern):
        return pattern in self.driver.current_url

    def select_dropdown_option(self, locator):
        self.click(locator)