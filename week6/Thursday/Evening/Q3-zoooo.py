class Animal:
    animals_list = list()

    def __init__(self, name, age, species):
        self.name = name

        assert self.validate_age(age), "Error : Age shouldn't be a text or negative"
        self.age = age

        self.species = species
        Animal.animals_list.append(species)

    @staticmethod
    def validate_age(age):
        return isinstance(age, int) and age > 0

    def specie_changer(self, new_spec):
        self.species = new_spec

    @staticmethod
    def get_species_count():
        return len(set(Animal.animals_list))

    def __repr__(self):
        return f"Name:{self.name},Age:{self.age}, Species:{self.species} "


my_dog = Animal("dOGGY", 2, "Germ")
my_other_cat = Animal("catty", 4, "Persian")
my_cat = Animal("Leo", 4, "Persian")

print(Animal.get_species_count())