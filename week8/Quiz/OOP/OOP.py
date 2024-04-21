class Person:
    persons = []

    def __new__(cls, *args, **kwargs):
        person = super().__new__(cls)
        print("__new__ called")
        return person

    @classmethod
    def saves(cls):
        print("saves called")
        obj = Person.__new__(cls)
        cls.persons.append(obj)


person1 = Person()
person1.saves()
print(person1.persons)