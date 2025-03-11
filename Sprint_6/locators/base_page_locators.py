from selenium.webdriver.common.by import By

class BasePageLocators:
    SCOOTER_LOGO = (By.XPATH, '//img[@src="/assets/scooter.png"]')
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]')
    COOKIE_BANNER = (By.CSS_SELECTOR, '#rcc-confirm-button')