from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Вход через нопку "Войти в аккаунт"
def test_login1(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        
        # Заполнение формы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

# Вход через кнопку "Личный кабинет"
def test_login2(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        
        # Заполнение формы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

# Вход через кнопку "Регистрации"
def test_login3(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Зарегистрироваться')]").click()
        
        # Заполнение формы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj']"))).click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))

# Вход через кнопку "Восстановить пароль"
def test_login4(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()
        
        # Заполнение формы входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj']"))).click()

        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        
        # Проверка успешного входа
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Оформить заказ']")))