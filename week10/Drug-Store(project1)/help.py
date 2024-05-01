import os
from functools import wraps

user = 'AmirHossein'


def clear():
    os.system('clear')


def check_login(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if user:
            return func()
        else:
            return 'permission denied!'

    return wrap


class Menu:
    def login():
        return 'login'

    def register():
        return 'register'

    @check_login
    @staticmethod
    def add_drug():
        return 'add drug'

    def __call__(self):
        for i, k in enumerate(Menu.__dict__):
            if not k.startswith('__'):
                print(i, '-', k)


menu = Menu()
#
# if __name__ == '__main__':
#     while True:
#         try:
#             clear()
#             menu()
#             reply = input('> ')
#             funcs = [key for key, func in Menu.__dict__.items() if not key.startswith('__')]
#             func_name = funcs[int(reply) - 1]
#             clear()
#             print(type(func_name), func_name)
#             func = getattr(Menu, func_name)
#             # print(func.__name__)
#             # func()
#             # print(func())
#             print(Menu.add_drug())
#             input('> press enter')
#         except Exception as e:
#             print(e)
#             input('error!')
#             continue
#         except KeyboardInterrupt:
#             exit()
# from pprint import pprint

import os


class Pharmacy:
    user_menu = {}
    admin_menu = {}
    buy_drug_meny = {1: "show_inventory"}

    def run(self):
        pass


user = None


def clear():
    os.system('clear')


def check_login():
    return True


def has_permission():
    pass


def login():
    return 'login attempt'


menu = {
    '1': {'name': 'login',
          'function': login,
          'condition': (lambda: False if user else True)()},

    '2': {'name': 'register',
          'condition': (lambda: False if user else True)()},

    '3': {
        'name': 'add_drug',
        'function': None,
        'condition': (lambda: True if user else False)()
    },
    '4': [
        {1: ...},
        {2: ...},
        {3: ...}
    ]

}

while True:
    clear()
    # print(menu)
    for i, (k, v) in enumerate(menu.items()):
        print(i, k, v)

    reply = input('> ')