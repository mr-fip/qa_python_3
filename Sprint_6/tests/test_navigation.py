import allure

@allure.feature('Навигация')
class TestNavigation:
    @allure.title('Переход через логотип Самоката')
    def test_scooter_logo_navigation(self, home_page):
        home_page.click_scooter_logo()
        assert home_page.is_url_contains("https://qa-scooter.praktikum-services.ru/")
    
    @allure.title('Переход через логотип Яндекса')
    def test_yandex_logo_navigation(self, home_page):
        original_window = home_page.get_current_window()
        home_page.click_yandex_logo()
        home_page.wait_for_number_of_windows(2)
        home_page.switch_to_new_window()
        assert home_page.wait_url_contains("dzen.ru"), (f"Ожидаемый URL содержит 'dzen.ru', фактический URL: {home_page.get_current_url()}")
        home_page.close_and_switch_to_window(original_window)