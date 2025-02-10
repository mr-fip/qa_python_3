from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# Проверка что Булки, Соусы, Начинки кликабельны
def test_designer_section(url, driver, info):
        driver.get(url)
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(),'Соусы')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(2)")))
        driver.find_element(By.XPATH, "//span[contains(text(),'Начинки')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(3)")))
        driver.find_element(By.XPATH, "//span[contains(text(),'Булки')]").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(1)")))
        