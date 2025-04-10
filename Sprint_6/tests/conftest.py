import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from data import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    page = HomePage(driver)
    page.accept_cookies()
    return page

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)