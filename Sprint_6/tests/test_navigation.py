import allure
import time
@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Переход через логотип Самоката')
    def test_scooter_logo_navigation(self, home_page):
        home_page.click_scooter_logo()
        assert home_page.is_current_url("https://qa-scooter.praktikum-services.ru/")

    @allure.title('Переход через логотип Яндекса')
    def test_yandex_logo_navigation(self, home_page):
        original_window = home_page.get_current_window()
        home_page.click_yandex_logo()
        time.sleep(1)
        home_page.switch_to_new_window()
        assert home_page.is_url_contains("dzen.ru") or home_page.is_url_contains("yandex.ru")
        home_page.close_and_switch_to_window(original_window)