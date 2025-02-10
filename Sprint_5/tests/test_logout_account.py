from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Проверка логаута через личный кабинет
def test_logout(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//h2[text()='Вход']").click()
        
        # Заполнение формы входа
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(text(),'Выход')]").click()

        # Проверка успешного выхода
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))
