import pytest

@pytest.fixture
def info():
    return {
        "email": "ignatfaitulin18@yandex.ru",
        "password": "12345678",
        "name": "Ignat"
    }

@pytest.fixture
def url():
    return "https://stellarburgers.nomoreparties.site/"

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()   
