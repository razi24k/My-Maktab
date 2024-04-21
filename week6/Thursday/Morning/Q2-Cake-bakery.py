from pydantic import BaseModel


class Cake(BaseModel):
    flavor: str
    size: int
    price: float

    def describe(self):
        return f"The {self.flavor} cake has a {self.size} size with {self.price} price"


my_cake = Cake(flavor="Vanilla", size=20, price=120)
print(my_cake.describe())
