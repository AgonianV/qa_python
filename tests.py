from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_genre_len_list(self):
        collector = BooksCollector()
        assert len(collector.genre) == 5
    @pytest.mark.parametrize('title_input', ['Love', 'Не-что!', '1', ' '])
    def test_add_new_book_same_book_title(self, title_input):
        collector = BooksCollector()
        collector.add_new_book(title_input)
        collector.add_new_book(title_input)
        collector.add_new_book(title_input)

        assert collector.books_genre == {title_input: ''}

    def test_set_book_genre_set_unknown_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Нечто')
        collector.set_book_genre('Нечто', 'Боевик')
        assert collector.books_genre == {'Нечто': ''}


    @pytest.mark.parametrize('genre_input', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_genre_from_genre_list(self, genre_input):
        collector = BooksCollector()
        collector.add_new_book('Мстители, битва без конечностей')
        collector.set_book_genre('Мстители, битва без конечностей', genre_input)
        assert collector.books_genre == {'Мстители, битва без конечностей' : genre_input}


    def test_get_book_genre_add_book_without_genre(self):
        collectors = BooksCollector()
        collectors.add_new_book('Дикий питон')
        assert collectors.get_book_genre('Дикий питон') == ''


    def test_get_books_with_specific_genre_output_detective(self):
        collectors = BooksCollector()
        titles = ["Человек-Паук","Шерлок Холмс","Луноход","Убийца","Большой брат","Сыщик"]
        genres = ["Мультфильмы","Детективы","Фантастика","Детективы","Комедии","Детективы"]
        for title,genre in zip(titles, genres):
            collectors.add_new_book(title)
            collectors.set_book_genre(title,genre)
        assert collectors.get_books_with_specific_genre('Детективы') == ['Шерлок Холмс', 'Убийца', 'Сыщик']

    def test_get_books_genre_add_three_books_with_genre(self):
        collectors = BooksCollector()

        collectors.add_new_book("Дюна")
        collectors.set_book_genre("Дюна", "Фантастика")
        collectors.add_new_book("Мгла")
        collectors.set_book_genre("Мгла", "Ужасы")
        collectors.add_new_book("Вверх")
        collectors.set_book_genre("Вверх", "Мультфильмы")
        assert collectors.get_books_genre() == {'Вверх': 'Мультфильмы', 'Дюна': 'Фантастика', 'Мгла': 'Ужасы'}


    def test_get_books_for_children_add_not_adult_book(self):
        collectors = BooksCollector()
        collectors.add_new_book('Винни Пух')
        collectors.set_book_genre('Винни Пух', 'Мультфильмы')
        assert collectors.get_books_for_children() == ['Винни Пух']


    def test_get_books_for_children_add_adult_book(self):
        collectors = BooksCollector()
        collectors.add_new_book('Зона')
        collectors.set_book_genre('Зона', 'Ужасы')
        assert collectors.get_books_for_children() == []


    def test_add_book_in_favorites_add_two_books(self):
        collectors = BooksCollector()

        collectors.add_new_book('Зона')
        collectors.set_book_genre('Зона', 'Ужасы')
        collectors.add_book_in_favorites('Зона')

        collectors.add_new_book('Луна')
        collectors.set_book_genre('Луна', 'Фантастика')
        collectors.add_book_in_favorites('Луна')
        assert collectors.favorites == ['Зона', 'Луна']

    def test_delete_book_from_favorites_delete_all_books(self):
        collectors = BooksCollector()

        collectors.add_new_book('Зона')
        collectors.set_book_genre('Зона', 'Ужасы')
        collectors.add_book_in_favorites('Зона')

        collectors.add_new_book('Луна')
        collectors.set_book_genre('Луна', 'Фантастика')
        collectors.add_book_in_favorites('Луна')
        if len(collectors.favorites) == 2:
            collectors.delete_book_from_favorites('Зона')
            collectors.delete_book_from_favorites('Луна')
            assert  len(collectors.favorites) == 0


    def test_get_list_of_favorites_books_add_five_books(self):
        titles = ['Дюна','Робот','Александр Македонский','Пиши сокращай','Акула убийца']
        collectors = BooksCollector()

        for title in titles:
            collectors.add_new_book(title)
            collectors.add_book_in_favorites(title)

        assert collectors.get_list_of_favorites_books() == titles and len(collectors.get_list_of_favorites_books()) == 5
