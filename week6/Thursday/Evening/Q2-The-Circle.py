class Circle:
    pi = 3.141

    def __init__(self, radius):
        assert self.validation(radius), "Error: Invalid radius"
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def perimeter(self):
        return 2 * Circle.pi * self.radius

    def display_circle(self):
        print(f"The circle area is {Circle.area(self)}, perimeter is {Circle.perimeter(self)}")

    def validation(self, radius):  # noqa
        return radius if (isinstance(radius, int) or isinstance(radius, float)) else None

    def radius_from_perimeter(self, perimeter): # noqa
        return perimeter/(2 * Circle.pi)

    @staticmethod
    def square_meters_to_square_feets(square_meters): # noqa
        return square_meters * 10.764


circle = Circle(3)
circle.display_circle()

print(circle.radius_from_perimeter(18.846))
print(Circle.square_meters_to_square_feets(20))
