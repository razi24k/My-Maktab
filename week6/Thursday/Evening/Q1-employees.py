class Employee:
    count_of_employees = 0
    fixed_incremented = 1
    employee_list = list()

    def __init__(self, name, age, salary):
        Employee.count_of_employees += 1
        self.name = name
        self.age = age
        self._salary = salary
        Employee.employee_list.append(self)

    @property
    def salary(self):
        return self._salary + Employee.fixed_incremented

    @classmethod
    def give_raise_to_all(cls, value):
        cls.fixed_incremented += value

    def raise_employee(self, incremented_salary):
        self._salary += incremented_salary

    def __repr__(self):
        return f"This is {self.name}, He/She is {self.age} years old and his/her salary is {self.salary}"


em_akbar = Employee("akbar", 99, 9800)
em_sina = Employee("Sina", 20, 1200)
# Employee.give_raise_to_all(400)
em_sina.raise_employee(200)
print(em_akbar.salary)
# print(em_akbar.salary)
# print((sum(list(map(lambda x: x.salary, Employee.employee_list))))/Employee.count_of_employees)
