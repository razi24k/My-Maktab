import library
from datetime import datetime


my_menu = library.Menu()
while True:
    main_menu_choice = my_menu.main_menu()
    if main_menu_choice == "1":
        while True:
            student_menu_choice = my_menu.student_menu()
            if student_menu_choice == "1":
                while True:
                    username, password = my_menu.student_login()
                    for student in library.Student.students:
                        if student.username == username and student.password == password:
                            while True:
                                student_login_choice = my_menu.student_login_menu()
                                if student_login_choice == "1":
                                    wanted_book = input("Enter book name: ")
                                    for book in library.Library.books:
                                        if book.name == wanted_book:
                                            borrow_date = datetime.today().day
                                            student.borrow_book(book, borrow_date)
                                        else:
                                            print("We have not any book with that name")
                                elif student_login_choice == "2":
                                    refactored_date = datetime.today().day
                                    student.book_extension(refactored_date)
                                elif student_login_choice == "3":
                                    book_name = input("Enter book name: ")
                                    for book in library.Library.books:
                                        if book.name == book_name:
                                            student.return_book(book)
                                elif student_login_choice == "4":
                                    print(student.calculate_late_fees())
                                elif student_login_choice == "5":
                                    student.save("students.txt")
                                    break
                                student.save("students.txt")
                        else:
                            print("Invalid Username or Password")
                            break
            elif student_menu_choice == "2":
                stu_name = input("Enter your name: ")
                stu_age = int(input("Enter your age: "))
                stu_username = input("Enter your username: ")
                stu_password = input("Enter your password: ")
                stu_phone_num = input("Enter your phone number: ")
                stu_number = input("Enter your student number: ")
                student1 = library.Student(stu_name, stu_age, stu_username, stu_password, stu_phone_num, stu_number)
                student1.save("students.txt")
            elif student_menu_choice == "3":
                break
    elif main_menu_choice == "2":
        while True:
            username, password = my_menu.librarian_login()
            for librarian in library.Librarian.librarians:
                if librarian.username == username and librarian.password == password:
                    while True:
                        librarian_menu_choice = my_menu.librarian_menu()
                        if librarian_menu_choice == "1":
                            book_lend = input("Enter name of the book that you want to lend: ")
                            student_username = input("Enter student username: ")
                            lib_menu = my_menu.lend_book(librarian, book_lend, student_username)
                            library.Library.save("library.txt")
                            print(f"book {book_lend} has been lended")
                        elif librarian_menu_choice == "2":
                            book_name = input("Enter name of the book that you want to add: ")
                            book_author = input("Enter author of the book: ")
                            book_price = input("Enter price of the book: ")
                            book1 = library.Book(book_name, book_author, book_price)
                            library.Library.add_book(librarian, book1)
                            library.Library.save("library.txt")
                        elif librarian_menu_choice == "3":
                            librarian.save("librarian.txt")
                            break
                else:
                    print("Invalid Username or password...")
                    break
    elif main_menu_choice == "3":
        break
