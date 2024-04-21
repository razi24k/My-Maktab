import uuid
import random
from Persons import Author


class Category:
    dict_of_categories = {}

    def __init__(self, cat_name):
        self.cat_name = cat_name

    @property
    def cat_name(self):
        return self._cat_name

    @cat_name.setter
    def cat_name(self, cat_name: str):
        if cat_name not in Category.dict_of_categories.keys():
            random_id = random.randint(1000, 9999)
            while random_id in self.dict_of_categories.values():
                random_id = random.randint(1000, 9999)
            self._cat_name = cat_name
            Category.dict_of_categories[cat_name] = random_id
        else:
            raise Exception("Category already exists in list")


cat1 = Category("sci_fi")
cat2 = Category("Action")


class Book:
    def __init__(self, name, page_count, price, category, authors):
        self.name = name
        self.page_count = page_count
        self.uniq_id = uuid.uuid1()
        self._price = price
        self.category = category
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


book1 = Book("Game Of Thrones", 100, 20, cat1, authors=["Alice", "Bob", "Charlie"])
book2 = Book("Harry Potter", 50, 50, cat1, authors=["Alice", "Bob", "Charlie"])
book3 = Book("The Forty Rules Of Love", 500, 50, cat1, authors=["Alice", "Bob", "Charlie"])
