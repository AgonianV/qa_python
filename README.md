# qa_python
test_genre_len_list:Проверка, что список жанров состоит из 5 записей.

test_add_new_book_same_book_title:Проверка, что при добавлении одной и той же
книги через метод "add_new_book" в books_genre будет одна копия книги. 

test_set_book_genre_set_unknown_genre:Проверка, что при присваивании книге
жанра не из genre, отдает пустую строку в словаре в поле значение.

test_set_book_genre_set_genre_from_genre_list:Проверка, что при присваивании книге
жанра из genre, отдает соответсвующий жанр у книги.

test_get_book_genre_add_book_without_genre:Проверка, что при добавлении книги без жанра метод отдаст пустое значение.

test_get_books_with_specific_genre_output_detective:Проверка, что из 6 книг различных жанров,
метод при поиске детективов отдаст 3 книги в жанре Детектив.

test_get_books_genre_add_three_books_with_genre:Проверка, что при добавлении 3 книг получим словарь из 3 книг с жанрами.

test_get_books_for_children_add_not_adult_book:Проверка, что при добавлении Книги с валидным жанром, книга будет добавлена в детский список.

test_get_books_for_children_add_adult_book:Проверка, что при добавлении книги с невалидным(взрослым) данром, книга не будет добавлена в детский список.

test_add_book_in_favorites_add_two_books:Проверка, что при добавлении 2 книг в список избранного, метод отдаст спиоск из двух книг без жанра.

test_delete_book_from_favorites_delete_all_books:Проверка, что при добавлении 2 книг в список избранного и последующего удаления их из списка методом delete_book_from_favorites, список избранного будет пустым.

test_get_list_of_favorites_books_add_five_books:Проверка, что при добавлении 5 книг в список избранного, метод отдаст список из 5 добавленных книг.

