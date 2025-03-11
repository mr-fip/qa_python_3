import allure
import pytest

@allure.feature('FAQ')
class TestQuestions:
    QUESTIONS = [
    (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (1, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (2, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее.")
]
    @pytest.mark.parametrize("question_data", QUESTIONS, ids=lambda x: f"Question {x[0]+1}")
    def test_question(self, home_page, question_data):
        question_num, expected = question_data
        home_page.click_question(question_num)
        assert home_page.get_answer_text(question_num) == expected