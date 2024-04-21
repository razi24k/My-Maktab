class Shape:
    def __init__(self, name: str, color: str):
        assert isinstance(name, str) and isinstance(color, str), "Invalid type for name or color"
        self.name = name
        self.color = color

    def display_name(self):
        print(f"Name of Shape is {self.name}")

    def display_color(self):
        print(f"Color of Shape is {self.color}")


class Rectangle(Shape):
    def __init__(self, name: str, color: str, length: int, width: int):
        super().__init__(name=name, color=color)
        assert isinstance(width, (float, int)) and isinstance(length, (float, int)), "Invalid type for width or height"
        self.width = width
        self.length = length

    def diameter(self):
        return (self.width + self.length) * 2

    def area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, name: str, color: str, side1: int, side2: int, side3: int, height: int):
        super().__init__(name=name, color=color)
        assert isinstance(side1, (float, int)) and isinstance(side2, (float, int)) and isinstance(side3, (float, int))\
            and isinstance(height, (float, int)), f"Invalid type for one or more than one of sides and height"
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.height = height

    def diameter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.diameter() / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
