import os
import pickle


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Product:
    def __init__(self, name, price, qty):
        assert isinstance(name, str), f"Name must be a string"
        self.name = name
        assert isinstance(price, (float, int)) and price >= 0, f"Price must be a positive number"
        self.price = float(price)
        self.__quantity = qty

    def sell(self):
        if self.__quantity > 0:
            self.__quantity -= 1
        else:
            print("quantity is zero...")

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        assert isinstance(value, int) and value >= 0, f"Quantity must be an positive integer"

    @property
    def restock(self):
        return self._quantity

    @restock.setter
    def restock(self, qty: int):
        assert isinstance(qty, int) and qty >= 0, f"Quantity must be a positive number"
        self._quantity = qty

    def display_info(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self._quantity}")


class Inventory:
    all_products = []

    def __init__(self, products=None):
        if products is None:
            products = []
        assert isinstance(products, list), f"products must be a list"
        Inventory.all_products.extend(products)
        self._products = Inventory.all_products

    @classmethod
    def load_products(cls, file_path):
        with open(file_path, 'rb') as _:
            cls.all_products = pickle.load(_)

    @classmethod
    def save_products(cls, file_path):
        with open(file_path, 'wb') as _:
            pickle.dump(cls.all_products, _)

    @classmethod
    def add_product(cls, p: Product):
        assert isinstance(p, Product), f"product must be an instance of Product class"
        cls.all_products.append(p)

    @classmethod
    def update_product(cls, p_name, p_price):
        for p in cls.all_products:
            if p.name == p_name:
                p.price = p_price
            elif p_name not in [i.name for i in cls.all_products]:
                print(f"Product does not exist in our inventory...")

    @property
    def products(self):
        return self._products

    @classmethod
    def delete_product(cls, p_name):
        for p in cls.all_products:
            if p.name == p_name:
                cls.all_products.remove(p)
            elif p_name not in [i.name for i in cls.all_products]:
                print(f"Product does not exist in our inventory...")

    @classmethod
    def read_inventory(cls):
        print(f"All products in inventory: ")
        for p in cls.all_products:
            p.display_info()


class Menu:
    def __init__(self):
        pass

    @staticmethod
    def main_menu():
        print(f'''{"Main Menu".center(42, "*")}
*{"1. add product".title().center(40)}*
*{"2. update product".title().center(40)}*
*{"3. remove product".title().center(40)}*
*{"4. show all products".title().center(40)}*
*{"5. sell".title().center(40)}*
*{"6. restock".title().center(40)}*
*{"7. product's information".title().center(40)}*
*{"8. exit and save changes".title().center(40)}*''')
        print("*" * 42)
        print('Enter your choice at the bottom'.center(42))
        print(" " * 21, end="")
        user_choice = input(" ")
        return user_choice


if __name__ == "__main__":
    print("Welcome to my amazing shop! ")
    input("Press Enter to continue...")
    my_inventory = Inventory()
    my_inventory.load_products("products.txt")
    exit_program = False
    while not exit_program:
        clear()
        my_menu = Menu().main_menu()
        if my_menu == "1":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                try:
                    product_price = float(input(f"Enter product {product_name}'s price: "))
                    quantity = int(input(f"Enter {product_name}'s quantity: "))
                    product = Product(product_name, product_price, quantity)
                    my_inventory.add_product(product)
                except ValueError:
                    print("Invalid input")
                    continue
        elif my_menu == "2":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                try:
                    product_price = float(input(f"Enter product {product_name}'s price: "))
                    my_inventory.update_product(product_name, product_price)
                except ValueError:
                    print("Invalid price...")
                    continue
        elif my_menu == "3":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                my_inventory.delete_product(product_name)
        elif my_menu == "4":
            my_inventory.read_inventory()
            input("Please press enter to back to menu: ")
        elif my_menu == "5":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                for p in my_inventory.all_products:
                    if p.name == product_name:
                        p.sell()
                    elif product_name not in [i.name for i in my_inventory.products]:
                        print("Product not found in inventory...")
        elif my_menu == "6":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                for p in my_inventory.all_products:
                    if p.name == product_name:
                        try:
                            quantity = int(input(f"Enter {product_name}'s quantity: "))
                            p.restock = quantity
                        except ValueError:
                            print("Invalid quantity")
                            continue
                    elif product_name not in [i.name for i in my_inventory.all_products]:
                        print("entered shit")
                        print(f"Product {product_name} not found in inventory...")
        elif my_menu == "7":
            clear()
            while True:
                product_name = input("Enter product name(enter exit to back to main menu): ")
                if product_name.lower() == "exit":
                    break
                for p in my_inventory.all_products:
                    if p.name == product_name:
                        p.display_info()
                else:
                    print("Product not found in inventory...")
        elif my_menu == "8":
            my_inventory.save_products("products.txt")
            exit_program = True
