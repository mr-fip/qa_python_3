from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = 'ignatfaitulin18@yandex.ru'
PASSWORD = '12345678'
URL = 'https://stellarburgers.nomoreparties.site/'

LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"
PERSONAL_CABINET_LINK = "//p[contains(text(),'Личный Кабинет')]"
REGISTER_LINK = "//a[contains(text(),'Зарегистрироваться')]"
RECOVER_PASSWORD_LINK = "//a[contains(text(),'Восстановить пароль')]"
LOGIN_HEADER = "//h2[text()='Вход']"
NAME_INPUT = "//input[@name='name']"
PASSWORD_INPUT = "//input[@type='password']"
SUBMIT_BUTTON = "//button[text()='Войти']"
CON_BUTTON = "//a[contains(text(),'Войти')]"
ORDER_BUTTON = "//button[text()='Оформить заказ']"

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, LOGIN_HEADER)))
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(password)
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()

# Вход по кнопке "Войти в аккаунт"
def test_login1(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
<<<<<<< HEAD
=======
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ORDER_BUTTON)))
>>>>>>> ff464d1 (Versin_5)

# Вход через кнопку "личный кабинет"
def test_login2(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, PERSONAL_CABINET_LINK).click()
    login(driver, EMAIL, PASSWORD)
<<<<<<< HEAD
=======
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ORDER_BUTTON)))
>>>>>>> ff464d1 (Versin_5)

# Вход через кнопку в форме регистрации
def test_login3(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, PERSONAL_CABINET_LINK).click()
    driver.find_element(By.XPATH, REGISTER_LINK).click()
    driver.find_element(By.XPATH, CON_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
<<<<<<< HEAD
=======
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ORDER_BUTTON)))
>>>>>>> ff464d1 (Versin_5)

#Вход через кнопку в форме восстановления пароля
def test_login4(driver):
    driver.get(URL)
    driver.find_element(By.XPATH, PERSONAL_CABINET_LINK).click()
    driver.find_element(By.XPATH, RECOVER_PASSWORD_LINK).click()
    driver.find_element(By.XPATH, CON_BUTTON).click()
    login(driver, EMAIL, PASSWORD)
<<<<<<< HEAD
=======
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ORDER_BUTTON)))
>>>>>>> ff464d1 (Versin_5)
