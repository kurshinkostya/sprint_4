import pytest
from main import BooksCollector


class TestBooksCollector:

    # тест на добавление книг
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2, 'Книги не добавились'

    # декоратор для параметризации
    @pytest.mark.parametrize('book_names', ['', 
                'Название_книги_на_сорок_один_символ_отриц',
                'Название_книги_на_сорок_два_символаа_отриц'])
    
    # тест на добавления некорректной книги
    def test_add_new_book_add_negative_book(self, collector, book_names):
        collector.add_new_book(book_names)
        assert len(collector.get_books_genre()) == 0, 'Проверка условия метода не пройдена, книга добавилась'

    # тест на добавление жанра к книге — ожидаемый положительный результат
    def test_set_book_genre_added_genre_book_positive_result(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Детективы')
        assert collector.books_genre.get('Шерлок Холм') == 'Детективы'

    # тест на добавление жанра, который не является списком
    def test_set_book_genre_add_genre_is_not_list(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Жанр_которого_нет')
        assert collector.books_genre.get('Шерлок Холм') == '', 'Книге добавился жанр которого нет в допустимых жанрах'

    # тест на получения жанра книги по названию — ожидаемый положительный результат
    def test_get_book_genre_for_name_positive_result(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.set_book_genre('Шерлок Холм', 'Детективы')
        assert collector.get_book_genre('Шерлок Холм') == 'Детективы'

    # тест на получения книг определённого жанра - возвращаются две книги детективного жанра
    def test_get_books_with_specific_genre_get_two_books_detectiv(self, collector):
        collector.books_genre = {'Шерлок Холмс': 'Детективы', 
                               'Шерлок Холмс_1': 'Детективы', 
                               'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Мультфильмы'}
        assert len(collector.get_books_with_specific_genre('Детективы')) == 2

    # тест на получения детских книг — возвращаются две книги
    def test_get_books_for_children_two_books(self, collector):
        collector.books_genre = {'Шерлок Холмс': 'Мультфильмы', 
                               'Шерлок Холмс_1': 'Детективы', 
                               'Шерлок Холмс_2': 'Ужасы',
                               'Шерлок Холмс_3': 'Комедии'}
        assert len(collector.get_books_for_children()) == 2

    # тест на добавления книги в избранное — добавляется одна книга
    def test_add_book_in_favorites_add_one_book(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        assert len(collector.get_list_of_favorites_books()) == 1 and collector.favorites[0] == 'Шерлок Холм'

    # тест на добавления книги в избранное — добавляются две книги, одна из которых дубликат
    def test_add_book_in_favorites_add_two_double_book(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        assert len(collector.get_list_of_favorites_books()) == 1, 'В избранное добавился дубль книги'

    # тест на удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Шерлок Холм')
        collector.add_book_in_favorites('Шерлок Холм')
        collector.delete_book_from_favorites('Шерлок Холм')
        assert len(collector.favorites) == 0


