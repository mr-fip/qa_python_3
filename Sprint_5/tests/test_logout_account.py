from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

EMAIL = 'ignatfaitulin18@yandex.ru'
PASSWORD = '12345678'
URL = 'https://stellarburgers.nomoreparties.site/'

LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"
LOGIN_HEADER = "//h2[text()='Вход']"
NAME_INPUT = "//input[@name='name']"
PASSWORD_INPUT = "//input[@type='password']"
SUBMIT_BUTTON = "//button[text()='Войти']"
PERSONAL_CABINET_LINK = "//p[contains(text(),'Личный Кабинет')]"
LOGOUT_BUTTON = "//button[contains(text(),'Выход')]"
LOGIN_PAGE_BUTTON = "//button[text()='Войти']"

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, LOGIN_HEADER)))
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

# Проверка выхода из аккаунта
def test_logout(driver):
    driver.get(URL)
    
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
    
    time.sleep(1)
    driver.find_element(By.XPATH, PERSONAL_CABINET_LINK).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, LOGOUT_BUTTON)))
    driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
    
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, LOGIN_PAGE_BUTTON)))
