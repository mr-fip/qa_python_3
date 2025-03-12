import allure
from selenium.webdriver.support import expected_conditions as EC

@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Переход через логотип Самоката')
    def test_scooter_logo_navigation(self, home_page):
        home_page.click_scooter_logo()
        assert home_page.is_current_url_matches("https://qa-scooter.praktikum-services.ru/")
    
    @allure.title('Переход через логотип Яндекса')
    def test_yandex_logo_navigation(self, home_page):
        original_window = home_page.get_current_window()
        home_page.click_yandex_logo()
        home_page.wait.until(EC.number_of_windows_to_be(2))
        home_page.switch_to_new_window()
        assert home_page.wait.until(EC.url_contains("dzen.ru"))
        home_page.close_and_switch_to_window(original_window)