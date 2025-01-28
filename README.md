В **conftest.py** находится фикстура для всех тестов.

**test_add_new_book** - Проверяем, что книги добавляются

**test_add_new_book_invalid_name** - Проверяем, что книга с именем больше 40 символов не добавляется

**test_add_duplicate_book** - Проверяем, что нельзя добавить одну и ту же книгу дважды. Должно остаться 3 книги.

**test_set_book_genre** - Проверяем установку жанра

**test_set_book_genre_invalid** - Проверяем, что жанр не устанавливается для несуществующей книги

**test_get_books_with_specific_genre** - Проверяем получение книг по жанру

**test_get_books_for_children** - Проверяем получение книг для детей

**test_get_books_for_children_with_age_rating** - Проверяем, что книги с возрастным рейтингом отсутствуют в списке для детей

**test_add_book_in_favorites** - Проверяем добавление книги в избранное

**test_add_book_in_favorites_already_in_favorites** - Проверяем, что книгу нельзя добавить повторно в избранное

**test_delete_book_from_favorites** - Проверяем удаление книги из избранного

**test_get_list_of_favorites_books** - Проверяем получение списка избранных книг
