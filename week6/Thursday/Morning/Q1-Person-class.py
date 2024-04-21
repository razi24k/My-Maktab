class Person:
    def __init__(self, name, age, address):
        assert self.validate_name(name), "Invalid name"
        self.name = name

        assert self.validate_age(age), "Invalid age"
        self.age = age

        assert self.validate_address(address), f"Invalid address"
        self.address = address

    def introduce(self):
        return f"{self.name} is : {self.age} with address {self.address}"

    def change_address(self, new_address):
        self.address = new_address
        return self.introduce()

    def validate_age(self, age):
        if isinstance(age, (int, float)):
            return True

    def validate_name(self, name):
        if isinstance(name, str):
            return True

    def validate_address(self, address):
        if isinstance(address, str):
            return True


Person1 = Person("John", 30, "Tehran, Azaadi")
print(Person1.introduce())
print(Person1.change_address('Shomal, nur'))