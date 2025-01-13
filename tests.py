import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_creating_instance_class_default_attributes_successfully_creating(self):
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
    def test_add_new_book_add_one_book_successfully_added(self, book_name):
        # Arrange
        collector = BooksCollector()
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert book_name in collector.books_genre and len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', ['', 'Название книги: длина равна 41 символу...'])
    def test_add_new_book_add_book_if_len_name_less_than1_or_greater_than40_book_not_added(self, book_name):
        # Arrange
        collector = BooksCollector()
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_book_with_existing_name_one_book_found(self):
        # Arrange
        collector = BooksCollector()
        book_name = 'Мастер и Маргарита'
        collector.add_new_book(book_name)
        # Act
        collector.add_new_book(book_name)
        # Assert
        assert len(collector.books_genre) == 1 and book_name in collector.books_genre
