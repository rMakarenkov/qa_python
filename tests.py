import random
import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_creating_instance_class_with_default_attributes_successfully(self):
        # Arrange
        default_collector_instance = {'books_genre': {},
                                      'favorites': [],
                                      'genre': ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'],
                                      'genre_age_rating': ['Ужасы', 'Детективы']}
        # Act
        collector = BooksCollector()
        # Assert
        assert collector.__dict__ == default_collector_instance

    @pytest.mark.parametrize('book_name', ['Х', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_new_book_add_one_book_successfully(self, book_name):
        # Arrange
        collector = BooksCollector()
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert book_name in collector.books_genre and len(collector.books_genre) == 1

    def test_add_new_book_add_one_book_genre_is_empty(self):
        # Arrange
        collector = BooksCollector()
        book_name = 'Тестовая книга'
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert collector.books_genre[book_name] == ''

    @pytest.mark.parametrize('book_name', ['', 'Название книги: длина равна 41 символу...'])
    def test_add_new_book_add_book_if_len_name_less_than1_or_greater_than40_failed(self, book_name):
        # Arrange
        collector = BooksCollector()
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_with_existing_name_failed(self):
        # Arrange
        collector = BooksCollector()
        book_name = 'Мастер и Маргарита'
        collector.add_new_book(book_name)
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert len(collector.books_genre) == 1 and book_name in collector.books_genre

    def test_set_book_genre_existing_genre_successfully(self):
        # Arrange
        collector = BooksCollector()
        book_name = 'Book 1'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        # Act
        collector.set_book_genre(book_name, book_genre)
        # Assert
        assert collector.books_genre[book_name] == book_genre

    def test_get_book_genre_existing_book_successfully(self):
        # Arrange
        collector = BooksCollector()
        book_name = 'Book 1'
        book_genre = random.choice(collector.genre)
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        # Act
        actual_genre = collector.get_book_genre(book_name)
        # Assert
        assert actual_genre == book_genre

    def test_get_books_with_specific_genre_existing_genre_successfully(self, create_collector_with_not_empty_book_genre):
        # Arrange
        collector = create_collector_with_not_empty_book_genre
        specific_genre = random.choice(collector.genre)
        expected_books = list(filter(lambda book: collector.books_genre[book] == specific_genre,
                                     collector.books_genre.keys()))
        # Act
        actual_books_after_specific_search = collector.get_books_with_specific_genre(specific_genre)
        # Assert
        assert actual_books_after_specific_search == expected_books

    def test_get_books_genre_successfully(self, create_collector_with_not_empty_book_genre):
        # Arrange
        collector = create_collector_with_not_empty_book_genre
        expected_books_genre = collector.books_genre
        # Act
        actual_books_genre = collector.get_books_genre()
        # Assert
        assert actual_books_genre == expected_books_genre


