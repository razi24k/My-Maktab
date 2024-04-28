import uuid
import random
from datetime import datetime


class Category:
    dict_of_categories = {}

    @classmethod
    def add_category(cls, librarian, *args, **kwargs):
        if isinstance(librarian, Librarian):
            for category in args:
                assert isinstance(category, str), 'Category must be a string'
                if category not in cls.dict_of_categories.keys():
                    random_id = random.randint(1000, 9999)
                    while random_id in cls.dict_of_categories.values():
                        random_id = random.randint(1000, 9999)
                    cls.dict_of_categories[category] = random_id
                else:
                    print('Category already exists')

            for category in kwargs:
                assert isinstance(category, str), 'Category must be a string'
                if category not in cls.dict_of_categories.keys():
                    random_id = random.randint(1000, 9999)
                    while random_id in cls.dict_of_categories.values():
                        random_id = random.randint(1000, 9999)
                    cls.dict_of_categories[category] = random_id
                else:
                    print('Category already exists')
        else:
            print('Only librarians can add categories.')

    def __init__(self, cat_name):
        self.cat_name = cat_name

    def __len__(self):
        books_num = 0
        pages_num = 0
        for shelve in Shelves.shelves:
            for book in shelve.books:
                if book.category.cat_name == self.cat_name:
                    books_num += 1
                    pages_num += book.page_count
        return f"There is {books_num} books and {pages_num} pages in this genre"


cat1 = Category("sci_fi")
# cat2 = Category("Action")


class Book:
    def __init__(self, name, page_count, price, category, authors):
        self.name = name
        self.page_count = page_count
        self.uniq_id = uuid.uuid1()
        self._price = price
        self.category = category
        self.pub_id = self.category.dict_of_categories[category]
        # list_of_authors = ""
        # for item in authors:
        #     list_of_authors += f"{item.name}-"
        # print(list_of_authors)
        #
        # self.writers = list_of_authors
        self.authors = authors

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        assert isinstance(value, Category)
        self._category = value

    @property
    def price(self):
        return self._price

    @property
    def authors(self):
        return self._authors

    @authors.setter
    def authors(self, authors):
        for author in authors:
            assert isinstance(author, Author), f"authors must be of type Author class"
        self._authors = authors


# Person classes
class Author:
    def __new__(cls, name):
        assert isinstance(name, str), f"name must be of type str"
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name


class Librarian:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @staticmethod
    def search_for_name(book_name):
        print("-" * 89)
        print("|", "book name".center(16), "|", "shelf".center(10), "|", "authors".center(20), "|", "book ID".center(10), "|")
        print("-" * 89)
        for shelve in Shelves.shelves:
            for book in shelve.books:
                if book.name == book_name:
                    print("|", book.name.center(16), "|", shelve.shelf_number.center(10), "|",
                          str(*[author.name for author in book.authors]).center(20), "|", book.pub_id.center(10), "|")
                    print("-" * 89)

    @staticmethod
    def search_for_id(book_id):
        print("-" * 89)
        print("|", "book name".center(16), "|", "shelf".center(10), "|", "authors".center(20), "|",
              "book ID".center(10), "|")
        print("-" * 89)
        # cls.dict_of_categories[category] = random_id
        for shelve in Shelves.shelves:
            for book in shelve.books:
                if book.pub_id == book_id:
                    print("|", book.name.center(16), "|", shelve.shelf_number.center(10), "|",
                          str(*[author.name for author in book.authors]).center(20), "|", book.pub_id.center(10), "|")
                    print("-" * 89)

    @staticmethod
    def search_for_author(author_name):
        print("-" * 89)
        print("|", "book name".center(16), "|", "shelf".center(10), "|", "authors".center(20), "|",
              "book ID".center(10), "|")
        print("-" * 89)
        for shelve in Shelves.shelves:
            for book in shelve.books:
                for author in book.authors:
                    if author_name == author.name:
                        print("|", book.name.center(16), "|", shelve.shelf_number.center(10), "|",
                              str(*[author.name for author in book.authors]).center(20), "|", book.pub_id.center(10), "|")
                        print("-" * 89)

    @staticmethod
    def search_for_category(category_name):
        print("-" * 89)
        print("|", "book name".center(16), "|", "shelf".center(10), "|", "authors".center(20), "|",
              "book ID".center(10), "|")
        print("-" * 89)
        for shelve in Shelves.shelves:
            for book in shelve.books:
                if book.category == category_name:
                    print("|", book.name.center(16), "|", shelve.shelf_number.center(10), "|",
                          str(*[author.name for author in book.authors]).center(20), "|", book.pub_id.center(10), "|")
                    print("-" * 89)

    @staticmethod
    def retrieve_book(uid):
        for shelve in Shelves.shelves:
            for book in shelve.books:
                if book.uniq_id == uid:
                    x = ("|", book.name.center(16) + "|" + shelve.shelf_number.center(10) + "|" +
                         str(*[author.name for author in book.authors]).center(20) + "|" + book.pub_id.center(10) +
                         "|\n" + ("-" * 89))
                    return x
        return "There is not a book with this UID"

    @staticmethod
    def add_category(name_of_cat):
        Category(name_of_cat)

    @staticmethod
    def book_placement(shelf, *args):
        assert isinstance(shelf, Shelves), "your first argument is not a shelf"
        for book in args:
            assert isinstance(book, Book), "your provided argument is not a Book"
        shelf.add_book(*args)


# Places
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
        assert isinstance(new_opening_hours, datetime), "opening hour should be a datetime object"
        self._opening_hours = new_opening_hours


open_time = datetime(2024, 4, 19, 6, 30)
print(type(open_time))
library1 = Library(name="Shahid Beheshti", location="Mashhad", opening_hours=open_time)


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

    def __str__(self):
        return f"{self.shelf_number} - {self.unique_id} shelve with category: {self.books_category}"

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, new_books):
        self.books_category = new_books[0].category.dict_of_categories[new_books[0].category.cat_name]
        for book in new_books:
            assert isinstance(book, Book), "The book should be an instance of Book class"
            assert book.category.dict_of_categories[book.category.cat_name] == self.books_category, \
                f"all book categories must be the same values"
        self._books = new_books
        self.unique_id = str(Shelves.shelf_num) + " - " + str(new_books[0].category.dict_of_categories[new_books[0].category.cat_name])

    @property
    def max_capacity(self):
        return self._max_capacity

    def add_book(self, *args):
        for book in args:
            assert isinstance(book, Book), "The book should be an instance of Book class"
            book_cat = book.category.dict_of_categories[book.category.cat_name]
            assert book_cat == self.books_category, (f"category of this shelve is {self.books_category},"
                                                     f" the category of book {book} is:{book_cat}")
        for book in args:
            self._pages += book.page_count
            if self._pages <= self._max_capacity:
                print(self._pages)
            else:
                print(f"book {book.name} not added to shelf...")
                raise Exception("You have Exceeded the max_capacity")
            self.books.append(book)


author1 = Author("Alice")
author2 = Author("Bob")
author3 = Author("Charlie")

book1 = Book("Game Of Thrones", 100, 20, cat1, authors=[author1, author2, author3])
book2 = Book("Harry Potter", 50, 50, cat1, authors=[author1, author2, author3])
book3 = Book("The Forty Rules Of Love", 500, 50, cat1, authors=[author1, author2, author3])
