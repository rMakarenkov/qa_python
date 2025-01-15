import pytest

from main import BooksCollector


@pytest.fixture(scope='function')
def create_collector_with_not_empty_book_genre():
    collector = BooksCollector()

    for n in range(1, 11):
        name = f'Book {n}'
        collector.add_new_book(name)
        collector.set_book_genre(name, collector.genre[(n - 1) % 5])

    return collector
