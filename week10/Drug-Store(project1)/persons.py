import store
from datetime import datetime


class Personnel:
    personnel = []

    def __new__(cls, *args, **kwargs):
        assert isinstance(args[0], str) or isinstance(kwargs["name"], str), "Name must be a string"
        assert isinstance(args[1], int) or isinstance(kwargs["age"], int), "Age must be an integer"
        assert isinstance(args[2], store.Store) or isinstance(kwargs["the_store"], store.Store), "the store mus be an instance of store.Store"
        for personnel in cls.personnel:
            if personnel.personnel_id == args[3] or personnel.personnel_id == kwargs["personnel_id"]:
                raise ValueError("This ID already exists in personnel IDs")
        else:
            assert (isinstance(args[3], int) and 999 > args[3] > 9999 and
                    args[3] not in [s.personnel_id for s in Personnel.personnel]) or \
            (isinstance(kwargs["personnel_id"], int) and 999 > kwargs["personnel_id"] > 9999 and
             kwargs["personnel_id"] not in [s.personnel_id for s in Personnel.personnel]),\
                "Personnel ID must be 4-digits integer and unique"
        assert (isinstance(args[4], (int, float)) and args[4] > 0) or \
               (isinstance(kwargs["salary"], (int, float)) and kwargs["salary"] > 0), "salary must be a positive number"
        assert (isinstance(args[5], str) and args[5].lower() in ("intern", "junior", "senior")) or \
               (isinstance(kwargs["position"], str) and kwargs["position"].lower() in ("intern", "junior", "senior")),\
                "position must be a string (intern or junior or senior)"
        assert (isinstance(args[6], str) and args[6].lower() in ("full-time", "part-time", "other")) or \
            (isinstance(kwargs["work_schedule"], str) and kwargs["work_schedule"].lower() in ("full-time", "part-time", "other")), \
            "work schedule must be a string (full-time or part-time or other)"
        assert (isinstance(args[7], str) and args[7] not in [i.username for i in cls.personnel]) or \
               (isinstance(kwargs["username"], str) and kwargs["username"] not in
                [i.username for i in cls.personnel]), "Invalid username. you can't use this username..."
        assert (isinstance(args[8], str) and args[8] > 7 and any([i.isdigit() for i in args[8]]) and
                any([i.isupper for i in args[8]]) and any([i in '_!@#$()<>' for i in args[8]])) or \
               (isinstance(kwargs["password"], str) and kwargs["password"] > 7 and any([i.isdigit() for i in kwargs["password"]]) and
                any([i.isupper for i in kwargs["password"]]) and any([i in '_!@#$()<>' for i in kwargs["password"]])), \
                "Invalid password"

    def __init__(self, name, age, the_store, personnel_id, salary, position, work_schedule, username, password):
        self.name = name
        self.age = age
        self.the_store = the_store
        self.personnel_id = personnel_id
        self.salary = salary
        self.position = position
        self.work_schedule = work_schedule
        self.username = username
        self.password = password
        self.personnel.append(self)

    @classmethod
    def login(cls, username, password):
        for person in cls.personnel:
            if person.username == username and person.password == password:
                return True
        return False


class Manager(Personnel):
    def __init__(self, name, age, the_store, personnel_id, salary, position, work_schedule, username, password):
        super().__init__(name, age, the_store, personnel_id, salary, position, work_schedule, username, password)
        self.position = "manager"
        self.accesses = ["hire personnel", "check balance", "change salary", "change position", "change phone",
                         "change email"]
        self.menu = {
            "hire personnel": self.hire(input("What is employee name: "), input("What is employee age: "),
                                        self.the_store, int(input("What is employee personnel ID: ")),
                                        float(input("What is employee salary: ")), input("What is employee position"),
                                        input("What is employee work schedule: "), input("What is employee username: "),
                                        input("What is employee password: ")),
            "check balance": self.check_balance(),
            "change salary of employee": self.change_salary(int(input("What is employee ID: ")),
                                                            float(input("What is employee new salary: "))),
            "change position of employee": self.change_position(int(input("What is employee ID: ")),
                                                                input("What is employee new position:")),
            "change email of store": self.change_email(input("What is new email address: ")),
            "back to main menu": None
        }

    @staticmethod
    def hire(name, age, the_store, personnel_id, salary, position, work_schedule, username, password):
        Personnel(name, age, the_store, personnel_id, salary, position, work_schedule, username, password)

    def check_balance(self):
        return self.the_store.balance

    @staticmethod
    def change_salary(employee_id, new_salary):
        for user in Personnel.personnel:
            if user.personnel_id == employee_id:
                user.salary = new_salary

    @staticmethod
    def change_position(employee_id, new_position):
        for user in Personnel.personnel:
            if user.personnel_id == employee_id:
                user.position = new_position

    def change_email(self, new_email):
        self.the_store.email = new_email


class Pharmacist(Personnel):
    def __init__(self, name, age, the_store, personnel_id, salary, position, work_schedule, username, password):
        super().__init__(name, age, the_store, personnel_id, salary, position, work_schedule, username, password)
        self.accesses = ["make new drug", "add drug to store", "sell drug"]
        self.menu = {
            "define new drug": self.def_drug(input("What is drug name: "), input("What is drug's company: "),
                                input("what categories you suggest for this drug(separate by space):").split(" "),
                                datetime.strptime(input("What is drug exp-date(yyyy-mm-dd): "), "%Y-%m-%d"),
                                float(input("What is the drug's price: ")), input("What is drug qty: ")),
            "change quantity of a drug": self.change_quantity(input("What is drug name: "), int(input("What is drug new qty: ")))
        }

    @staticmethod
    def def_drug(name, company, categories, exp_date, price, qty):
        store.Drug(name, company, categories, exp_date, price, qty)

    def add_drug(self, *args, **kwargs):
        for drug_obj in args:
            if drug_obj.category not in self.the_store.shleves.keys(): # noqa
                print(f"There is no shelves in this drug category: {drug_obj.category}")
                print(f"categories must be in this list: {self.the_store.shleves.keys()}")
                return False
            else:
                self.the_store.shleves[drug_obj.category].append(drug_obj)
                print(f"drug {drug_obj} added to store {self.the_store.__name__} with category {drug_obj.category}")
        for drug_obj in kwargs.values():
            if drug_obj.category not in self.the_store.shleves.keys(): # noqa
                print(f"There is no shelves in this drug category: {drug_obj.category}")
                print(f"categories must be in this list: {self.the_store.shleves.keys()}")
                return False
            else:
                self.the_store.shleves[drug_obj.category].append(drug_obj)
                print(f"drug {drug_obj} added to store {self.the_store.__name__} with category {drug_obj.category}")
        return True

    @staticmethod
    def change_quantity(drug, quantity):
        for d in store.Drug.drugs:
            if d.name == drug:
                d.qty = quantity


class SalesClerk(Personnel):
    def __init__(self, name, age, the_store, personnel_id, salary, position, work_schedule, username, password):
        super().__init__(name, age, the_store, personnel_id, salary, position, work_schedule, username, password)
        self.accesses = ["sell drug"]
        self.menu = {
            "sell drug": self.sell(input("What is drug name: "), int(input("How many drugs you want to sell: "))),
            "show all drugs": self.show_all_drugs(),

        }

    def sell(self, drug, quantity):
        for d in self.the_store.Drug.drugs:
            if d.name == drug:
                d.qty -= quantity
                self.the_store.balance += quantity * d.price

    def show_all_drugs(self):
        for drug in self.the_store.Drug.drugs:
            if not drug.is_expired:
                print(drug)