from selenium.webdriver.common.by import By

class OrderPageLocators:
    NAME = (By.CSS_SELECTOR, 'input[placeholder*="Имя"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder*="Фамилия"]')
    ADDRESS = (By.CSS_SELECTOR, 'input[placeholder*="Адрес"]')
    METRO_STATION = (By.CLASS_NAME, 'select-search__input')
    PHONE = (By.CSS_SELECTOR, 'input[placeholder*="Телефон"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(., "Далее")]')
    DATE = (By.CSS_SELECTOR, 'input[placeholder*="Когда привезти"]')
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(), 'Срок аренды')]/..")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{0}']")
    COLOR_CHECKBOX = (By.XPATH, "//input[@id='black']")
    COMMENT = (By.CSS_SELECTOR, 'input[placeholder*="Комментарий"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[contains(., "Да")]')
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(., "Заказ оформлен")]')
    DROPDOWN_MENU = (By.XPATH, "//div[@class='Dropdown-menu']")