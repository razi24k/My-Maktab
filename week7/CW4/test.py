# class Maktab:
#     def __init__(self, name, maktab_id):
#         self.name = name
#         self._id = maktab_id

#     @property
#     def id(self):  # getter
#         print("ID, Getter called !")
#         return hash(str(self._id))

#     @id.setter
#     def id(self, value):  # setter
#         print("ID, Setter called !")
#         assert isinstance(value, int), "ID must be integer"
#         self._id = value


# m = Maktab("Example", 123)
# print(m.id)  # This will trigger the getter method
# m.id = 456  # This will trigger the setter method
# print(m.id)

my_list = []
if not my_list:
    print("No list")
