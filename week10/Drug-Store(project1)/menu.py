import persons


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def main_menu():
        print(f'''{"Main Menu".center(42, "*")}
*{"1. login".title().center(40)}*
*{"2. register".title().center(40)}*
*{"3. exit".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice

    @staticmethod
    def login(username, password):
        choice = Menu.main_menu()
        if choice == "1":
            for user in persons.Personnel.personnel:
                if user.username == username and user.password == password:
                    for i, (k, v) in enumerate(user.menu.items()):
                        print(f"{i+1}. {k}")


