from Subjects import Category
from Places import Shelves


class Author:
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
                          str(*[author.name for author in book.authors]).center(20), "|", book.uniq_id.center(10), "|")
                    print("-" * 89)

    def retrieve_a_book(self):
        pass

    @staticmethod
    def add_category(name_of_cat):
        Category(name_of_cat)

    def book_replacement(self):
        pass


liber = Librarian('Ali', 21)
print(liber.name)