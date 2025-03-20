from selenium.webdriver.common.by import By

class BasePageLocators:
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/']/img[contains(@src, 'scooter')]")
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]')
    COOKIE_BANNER = (By.CSS_SELECTOR, '#rcc-confirm-button')