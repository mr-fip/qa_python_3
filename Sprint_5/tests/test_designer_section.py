from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://stellarburgers.nomoreparties.site/'

SAUCE_SECTION = (By.XPATH, "//span[contains(text(),'Соусы')]")
TOPPINGS_SECTION = (By.XPATH, "//span[contains(text(),'Начинки')]")
ROLLS_SECTION = (By.XPATH, "//span[contains(text(),'Булки')]")

def click_section(driver, section_locator, expected_tab_index):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(section_locator)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"div.tab_tab__1SPyG:nth-child({expected_tab_index})")))

# Проверка секций
def test_designer_section(driver):
    driver.get(url)
    
    click_section(driver, SAUCE_SECTION, 2)
    click_section(driver, TOPPINGS_SECTION, 3)
    click_section(driver, ROLLS_SECTION, 1)

    # Проверка на видимость первой секции (Булки)
    assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tab_tab__1SPyG:nth-child(1)")))
