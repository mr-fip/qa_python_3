import pytest

class TestBooksCollector:

    def test_add_new_book(self, collector):
        collector.add_new_book("1984")
        collector.add_new_book("Гарри Поттер")
        assert "1984" in collector.get_books_genre()
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_add_new_book_invalid_name(self, collector):
        collector.add_new_book("A" * 41)
        assert "A" * 41 not in collector.get_books_genre()

    def test_add_duplicate_book(self, collector):
        collector.add_new_book("1984")
        initial_count = len(collector.get_books_genre())
        collector.add_new_book("1984")
        assert len(collector.get_books_genre()) == initial_count

    def test_set_book_genre(self, collector):
        collector.set_book_genre("1984", "Фантастика")
        assert collector.get_book_genre("1984") == "Фантастика"

    def test_set_book_genre_invalid(self, collector):
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert collector.get_book_genre("Неизвестная книга") is None

    @pytest.mark.parametrize(
        "genre, expected_books",[
        ("Фантастика", ["1984"]), 
        ("Мультфильмы", ["Гарри Поттер"]), 
        ("Ужасы", [])
        ])
    
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        books = collector.get_books_with_specific_genre(genre)
        assert books == expected_books

    def test_get_books_for_children(self, collector):
        books = collector.get_books_for_children()
        assert books == ["Гарри Поттер"]

    def test_get_books_for_children_with_age_rating(self, collector):
        collector.add_new_book("Детективный роман")
        collector.set_book_genre("Детективный роман", "Детективы")
        books = collector.get_books_for_children()
        assert books == ["Гарри Поттер"]

    def test_add_book_in_favorites(self, collector):
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.favorites

    def test_add_book_in_favorites_already_in_favorites(self, collector):
        collector.add_book_in_favorites("1984")
        initial_count = collector.favorites.count("1984")
        collector.add_book_in_favorites("1984")
        assert collector.favorites.count("1984") == initial_count

    def test_delete_book_from_favorites(self, collector):
        collector.add_book_in_favorites("1984")
        assert "1984" in collector.favorites
        collector.delete_book_from_favorites("1984")
        assert "1984" not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_book_in_favorites("1984")
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["1984"]
