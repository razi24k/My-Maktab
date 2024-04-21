class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, number):
        the_item = (name, number)
        self.items.append(the_item)

    def remove_item(self, name):
        my_items = [i[0] for i in self.items]
        if name in my_items:
            self.items.remove(name)
