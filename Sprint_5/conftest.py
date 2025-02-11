import pytest

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()   
