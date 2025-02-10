from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Переход по клику на «Личный кабинет»
def test_transfer_personal_account(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
        driver.find_element(By.XPATH, "//h2[text()='Вход']").click()
        
        # Заполнение формы входа
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "//input[@name='name']").send_keys(info['email'])
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(info['password'])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()
        time.sleep(1)
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        
        # Проверка успешного перехода
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Переход из личного кабинета в конструктор
def test_account_in_designer(url, driver, info):
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
        driver.find_element(By.XPATH, "//p[contains(text(),'Конструктор')]").click()

        # Проверка успешного перехода
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")))

# Переход из личного кабинета в логотип
def test_account_in_logo(url, driver, info):
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
        driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']//a//*[name()='svg']").click()

        # Проверка успешного перехода
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")))
