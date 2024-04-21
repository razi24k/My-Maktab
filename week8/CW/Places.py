from datetime import datetime
import Subjects


class Library:
    def __init__(self, name, location, opening_hours):
        self.name = name
        self.location = location
        self.opening_hours = opening_hours

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        assert isinstance(new_name, str), "It should be a STR"
        self._name = new_name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location):
        assert isinstance(new_location, str), "It should be a STR"
        self._location = new_location

    @property
    def opening_hours(self):
        return self._opening_hours

    @opening_hours.setter
    def opening_hours(self, new_opening_hours):
        assert new_opening_hours.isnumeric(), "It should be a number"
        self._opening_hours = new_opening_hours


open_time = datetime(2024, 4, 19, 6, 30)


class Shelves(list):
    shelf_num = 0
    shelves = []

    def __init__(self, max_capacity, books):
        # https://realpython.com/inherit-python-list/
        super().__init__(item for item in books)
        self.books = books
        self._max_capacity = max_capacity
        self._pages = 0
        self.__class__.shelf_num += 1
        self.shelf_number = self.__class__.shelf_num
        for book in books:
            self._pages += book.page_count
            if self._pages <= max_capacity:
                print(self._pages)
            else:
                raise Exception("You have Exceeded the max_capacity")
        self.__class__.shelves.append(self)

    def __len__(self):
        return self._pages

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, new_books):
        self.books_category = new_books[0].category.dict_of_categories[new_books[0].category.cat_name]
        for book in new_books:
            assert isinstance(book, Subjects.Book), "The book should be an instance of Book class"
            assert book.category.dict_of_categories[book.category.cat_name] == self.books_category, \
                f"all book categories must be the same values"
        self._books = new_books
        self.unique_id = str(Shelves.shelf_num) + " - " + str(new_books[0].category.dict_of_categories[new_books[0].category.cat_name])

    @property
    def max_capacity(self):
        return self._max_capacity

    def add_book(self, *args):
        for book in args:
            assert isinstance(book, Subjects.Book), "The book should be an instance of Book class"
            book_cat = book.category.dict_of_categories[book.category.cat_name]
            assert book_cat == self.books_category, (f"category of this shelve is {self.books_category},"
                                                 f" the category of book {book} is:{book_cat}")
        for book in args:
            self._pages += book.page_count
            if self._pages <= self._max_capacity:
                print(self._pages)
            else:
                print(f"book {book.uniq_id} not added to shelf...")
                raise Exception("You have Exceeded the max_capacity")
            self.books.append(book)


shelve1 = Shelves(300, [Subjects.book1])
shelve1.add_book(Subjects.book2, Subjects.book3)
print(len(shelve1))
# print(shelve1.unique_id)
# print(Subjects.book1.category.dict_of_categories[Subjects.book1.category.cat_name])
# print(Subjects.book2.category.dict_of_categories[Subjects.book2.category.cat_name])
