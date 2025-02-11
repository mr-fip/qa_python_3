from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

EMAIL = 'ignatfaitulin18@yandex.ru'
PASSWORD = '12345678'
NAME = 'Ignat'
URL = 'https://stellarburgers.nomoreparties.site/'

REGISTER_BUTTON = "/html/body/div/div/main/section[2]/div/button"
REGISTER_LINK = "//a[contains(text(),'Зарегистрироваться')]"
NAME_INPUT = "/html/body/div/div/main/div/form/fieldset[1]/div/div/input"
EMAIL_INPUT = "/html/body/div/div/main/div/form/fieldset[2]/div/div/input"
PASSWORD_INPUT = "/html/body/div/div/main/div/form/fieldset[3]/div/div/input"
SUBMIT_BUTTON = "//button[text()='Зарегистрироваться']"
SUCCESS_BUTTON = "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
ERROR_MESSAGE = "//p[contains(@class, 'input__error')]"

# Проверка регистрации
def test_registration_success(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, REGISTER_BUTTON))).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, REGISTER_LINK))).click()
    
    # Заполнение формы
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(NAME)
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()
    
    # Проверка успешной регистрации
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, SUCCESS_BUTTON)))

# Проверка на некорректный пароль
def test_registration_invalid_password(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, REGISTER_BUTTON))).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, REGISTER_LINK))).click()

    # Заполнение формы с коротким паролем
    driver.find_element(By.XPATH, NAME_INPUT).send_keys(NAME)
    driver.find_element(By.XPATH, EMAIL_INPUT).send_keys(EMAIL)
    driver.find_element(By.XPATH, PASSWORD_INPUT).send_keys('12345')
    driver.find_element(By.XPATH, SUBMIT_BUTTON).click()
    
    # Проверка сообщения об ошибке
    error = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ERROR_MESSAGE)))
    assert error.text == 'Некорректный пароль'
