import pytest
from main import BooksCollector

@pytest.fixture(autouse=True)
def collector():
    collector = BooksCollector()
    collector.add_new_book("1984")
    collector.add_new_book("Гарри Поттер")
    collector.add_new_book("Ужасный детектив")
    collector.set_book_genre("1984", "Фантастика")
    collector.set_book_genre("Гарри Поттер", "Мультфильмы")
    collector.set_book_genre("Ужасный детектив", "Ужасы")
    return collector
