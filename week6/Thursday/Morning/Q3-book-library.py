class Book:
    def __init__(self, title, author, genre, availability=True):
        self.title = title
        self.author = author
        self.genres = genre
        self.availability = availability

    def borrow(self):
        if not self.availability:
            print("Book is borrowed")
        else:
            self.availability = not self.availability


my_book = Book(title="Morning", author="Rasool", genre="Action", availability=True)
my_book.borrow()
print(my_book.availability)
my_book.borrow()
print(my_book.availability)
