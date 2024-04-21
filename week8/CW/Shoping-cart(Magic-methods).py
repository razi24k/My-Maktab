class Item:
    def __new__(cls, name, price):
        # print(f"new called")
        assert isinstance(name, str), f"Only strings are accepted for item name"
        assert isinstance(price, (int, float)), f"Only numbers are accepted for item price"
        return super().__new__(cls)

    def __init__(self, name, price):
        # print(f"init called")
        self.name = name
        self.price = price

    def __str__(self):
        return f"Item: {self.name} has price: {self.price}$"


class ShoppingCart:
    @staticmethod
    def get_value(item_name):
        if isinstance(item_name, str):
            return item_name
        elif isinstance(item_name, Item):
            return item_name.name

    def __init__(self, items=None):
        if items is None:
            self.items = []

    def __str__(self):
        cart = []
        for item in self.items:
            cart.append(item.name + "-" + str(item.price) + "$")
        return "\n".join(cart)
        # def generator():
        #     for item in self.items:
        #         yield f"{item.name} - {item.price}$"
        # return "\n".join(list(generator()))

    def __len__(self):
        return len(self.items)

    def __contains__(self, new_item):
        for item in self.items:
            if item.name == self.get_value(new_item):
                return True
        else:
            return False

    def __add__(self, other_cart):
        assert isinstance(other_cart, ShoppingCart), f"Unexpected type {type(other_cart)} != {ShoppingCart.__name__}"
        cls = self.__class__
        new_cart = cls()
        for item in self.items:
            new_cart.add_item(item)
        for item in other_cart.items:
            new_cart.add_item(item)
        return new_cart

    # def __radd__(self, other_cart):
    #     return self.__add__(other_cart)

    def add_item(self, *args, **kwargs):
        for item in args:
            assert isinstance(item, Item), f"Unexpected argument type: {type(item)} != <class '{Item.__name__}'>"
            self.items.append(item)
        for item in kwargs.values():
            assert isinstance(item, Item), f"Unexpected argument type: {type(item)} != <class '{Item.__name__}'>"
            self.items.append(item)

    def remove_item(self, *args, **kwargs):
        for item in args:
            assert isinstance(item, Item), f"Unexpected argument type: {type(item)} != <class '{Item.__name__}'>"
            self.items.remove(item)
        for item in kwargs.values():
            assert isinstance(item, Item), f"Unexpected keyword argument type: {type(item)} != <class '{Item.__name__}'>"
            self.items.remove(item)

    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price


my_item = Item("Apple", 300)
my_item2 = Item("Banana", 400)
my_cart = ShoppingCart()
my_cart.add_item(my_item)
my_cart2 = ShoppingCart()
my_cart2.add_item(my_item2)
my_cart3 = my_cart2 + my_cart
print(my_cart3)
# print(my_item in my_cart)
# print(my_item2 in my_cart)
# print(my_item2 in my_cart3 and my_item in my_cart3)
# print(my_cart3.total_price())
# print(my_cart2.total_price())
# print(my_cart.total_price())