class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError
        return self.value / other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value


num1 = Number(970)
num2 = Number(98)
print(num1 * num2)
print(num1 + num2)
print(num1 - num2)
print(num1 / num2)
print(num1 > num2)
print(num1 >= num2)
print(num1 == num2)
