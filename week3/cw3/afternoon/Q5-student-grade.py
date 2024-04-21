student_grades = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Emily": 90,
    "Michael": 88
}


def student_grade(stu_name):
    try:
        return student_grades[stu_name]
    except KeyError:
        print("This student is not in our database!")
        return None


while True:
    add_or_show = input("<<menu>>\n---------- \n1: add \n2: show grades \n3: stop program!\nEnter your choice here: ")
    add = False
    show = False
    if add_or_show == "1":
        add = True
    elif add_or_show == "2":
        show = True
    elif add_or_show == "3":
        break
    else:
        print("Invalid input! Try again")
        continue
    while add:
        name = input("Provide student name(blank to quit): ").title()
        if not name:
            add = False
            break
        try:
            grade = float(input("Provide student's grade: "))
        except ValueError:
            print("Invalid input")
            continue
        student_grades[name] = grade
    while show:
        name = input("Provide student name that you want to show his grade(blank to exit): ").title()
        if not name:
            show = False
        else:
            try:
                print(student_grade(name))
            except KeyError:
                print("This student is not in our database!")
                continue

