class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name

    @classmethod
    def register_animal(cls, animal_name):
        if cls.space > 0:
            cls.animals.append(animal_name)
            print(f"Animal {animal_name} registered successfully")
            cls.space -= 1
        else:
            print(f"Lack of enough space...")

    @classmethod
    def unregister_animal(cls, animal_name):
        if animal_name in cls.animals:
            cls.animals.remove(animal_name)
            cls.space += 1
        else:
            print(f"Animal {animal_name} has not been registered...")

    @staticmethod
    def cost_of_treatment(hours, cost_per_hour):
        return f"{hours * cost_per_hour}$"

    @staticmethod
    def info():
        return f"Animals list: {Vet.animals}\nSpace: {Vet.space}"
