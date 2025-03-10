from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = 'ignatfaitulin18@yandex.ru'
PASSWORD = '12345678'
URL = 'https://stellarburgers.nomoreparties.site/'

LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"
LOGIN_HEADER = "//h2[text()='Вход']"
NAME_INPUT = "//input[@name='name']"
PASSWORD_INPUT = "//input[@type='password']"
SUBMIT_BUTTON = "//button[text()='Войти']"
PERSONAL_ACCOUNT_LINK = "Личный Кабинет"
DESIGNER_LINK = "//p[contains(text(),'Конструктор')]"
LOGO_LINK = "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']"
ACCOUNT_LINK = "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']"
MAIN_PAGE_HEADER = "//h1[@class='text text_type_main-large mb-5 mt-10']"

def login(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGIN_BUTTON))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, LOGIN_HEADER))).click()
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(EMAIL)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

# Переход в личный кабинет
def test_transfer_personal_account(driver):
    login(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, PERSONAL_ACCOUNT_LINK))).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ACCOUNT_LINK)))

# Переход из личного кабинета в конструктор
def test_account_in_designer(driver):
    login(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, PERSONAL_ACCOUNT_LINK))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, DESIGNER_LINK))).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, MAIN_PAGE_HEADER)))

# Переход из личного кабинета в лого
def test_account_in_logo(driver):
    login(driver)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, PERSONAL_ACCOUNT_LINK))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, LOGO_LINK))).click()
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, MAIN_PAGE_HEADER)))
