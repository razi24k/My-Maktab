class Human:
    planet = "Earth"

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Human("John", 18)
person1.planet = "Mars"
print(person1.planet)
print(Human.planet)