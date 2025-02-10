from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Проверка регистрации
def test_registration_success(info, url, driver):
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))).click()
        
    # Заполнение формы
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(info['name'])
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(info['email'])
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(info['password'])
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
    # Проверка успешной регистрации
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")))

def test_registration_invalid_password(info, driver, url):
    driver.get(url)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button').click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Зарегистрироваться')]"))).click()

    # Заполнение формы с коротким паролем
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(info['name'])
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(info['email'])
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys('12345')
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
        
    # Проверка сообщения об ошибке
    error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'input__error')]")))
    assert error.text == 'Некорректный пароль'
