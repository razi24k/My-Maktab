from datetime import datetime
import pickle


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Human):
    students = []

    def __new__(cls, *args, **kwargs):
        username = args[2]
        password = args[3]
        phone_num = args[4]
        student_num = args[-1]
        assert isinstance(username, str) and len(username) > 7, "Invalid username"
        assert isinstance(password, str) and len(password) > 7, "Invalid password"
        assert isinstance(phone_num, str) and len(phone_num) == 11 and phone_num.startswith("0") and phone_num.isalnum()\
            , "Invalid phone number"
        assert isinstance(student_num, str) and len(student_num) == 8 and student_num.isalnum()\
            , "Invalid student number"
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age, username, password, phone_num, student_num):
        super().__init__(name=name, age=age)
        self.username = username
        self.password = password
        self.phone_num = phone_num
        self.student_num = student_num
        self.borrowed_book = None
        self.book_extension = False
        self.book_access = False
        self.late_fees = 0
        self.remaining_days = 0
        self.__class__.students.append(self)

    def __str__(self):
        return f"phone number: {self.phone_num}, student number: {self.student_num}, borrowed book: {self.borrowed_book}"

    def borrow_book(self, the_book, date):
        assert isinstance(date, datetime), "Invalid date object"
        assert isinstance(the_book, Book), "Invalid book object"
        self.borrow_date = date # noqa
        for book in Library.books:
            if book.name == the_book.name and self.book_access:
                self.book_access = False
                book.is_borrowed = True
                self.borrowed_book = book
                self.remaining_days = datetime.now().day - self.borrow_date.day

    def book_extension(self, date_extension):
        assert isinstance(date_extension, datetime), "Invalid date object"
        if not self.book_extension:
            self.book_extension = True
            self.borrow_date = date_extension # noqa
        else:
            print("You have already extended the delivery time of your borrowed book.")

    def return_book(self, the_book):
        if the_book not in Library.books and self.borrowed_book == the_book:
            Library.books.append(the_book)
            self.borrowed_book = None
            self.borrowed_book = True
            self.calculate_late_fees()
            self.remaining_days = 0

    def calculate_late_fees(self):
        if self.remaining_days > 14 and self.book_extension:
            self.late_fees += 5000 * (self.remaining_days - 14)
        return self.late_fees

    @classmethod
    def save(cls, file_path):
        with open(file_path, "wb") as _:
            pickle.dump(cls.students, _)

    @classmethod
    def load(cls, file_path):
        with open(file_path, "rb") as _:
            cls.students = pickle.load(_)


class Librarian(Human):
    librarians = []

    def __new__(cls, *args, **kwargs):
        username = args[2]
        password = args[3]
        assert isinstance(username, str) and len(username) > 7, "Invalid username"
        assert isinstance(password, str) and len(password) > 7, "Invalid password"
        instance = super().__new__(cls)
        return instance

    def __init__(self, name, age, username, password):
        super().__init__(name=name, age=age)
        self.username = username
        self.password = password
        self.__class__.librarians.append(self)

    @staticmethod
    def lend_book(the_student, the_book):
        for student in Student.students:
            if student.name == the_student.name:
                for book in Library.books:
                    if book.name == the_book.name:
                        the_book = book
                        if not student.book_access:
                            Library.books.pop(Library.books.index(the_book))
                            student.book_access = True
                        else:
                            print("student has already borrowed a book...")
                else:
                    print("Book not found")
        else:
            print("Student not found")

    @classmethod
    def save(cls, file_path):
        with open(file_path, "wb") as _:
            pickle.dump(cls.librarians, _)

    @classmethod
    def load(cls, file_path):
        with open(file_path, "rb") as _:
            cls.librarians = pickle.load(_)


class Book:
    def __init__(self, name, author, price):
        self.name = name
        self.price = price
        self.author = author
        self.is_borrowed = False


class Library:
    books = []

    def __init__(self, name, location):
        self.name = name
        self.location = location

    @classmethod
    def add_book(cls, librarian, book):
        assert isinstance(librarian, Librarian), f"{librarian} is Not an object of Librarian"
        assert isinstance(book, Book), f"{book} is Not an object of Book"
        cls.books.append(book)

    @classmethod
    def save(cls, file_path):
        with open(file_path, "wb") as _:
            pickle.dump(cls.books, _)

    @classmethod
    def load(cls, file_path):
        with open(file_path, "rb") as _:
            cls.books = pickle.load(_)


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def main_menu():
        print(f'''{"Main Menu".center(42, "*")}
*{"1. enter as student".title().center(40)}*
*{"2. enter as librarian".title().center(40)}*
*{"3. exit".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @staticmethod
    def student_menu():
        print(f'''{"student Menu".center(42, "*")}
*{"1. login".title().center(40)}*
*{"2. signup".title().center(40)}*
*{"3. back to main menu".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @staticmethod
    def student_login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password

    @staticmethod
    def student_login_menu():
        print(f'''{"student Menu".center(42, "*")}
*{"1. borrow book".title().center(40)}*
*{"2. extension book".title().center(40)}*
*{"3. return book".title().center(40)}*
*{"4. calculate late fees".title().center(40)}*
*{"5. exit".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @staticmethod
    def librarian_login():
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        return username, password

    @staticmethod
    def librarian_menu():
        print(f'''{"librarian Menu".center(42, "*")}
*{"1. lend book".title().center(40)}*
*{"2. add book".title().center(40)}*
*{"3. back to main menu".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @staticmethod
    def lend_book(librarian, book, student_username):
        for student in Student.students:
            if student.username == student_username:
                for b in Library.books:
                    if b.name == book:
                        librarian.lend_book(the_student=student, the_book=b)


