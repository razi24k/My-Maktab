from datetime import datetime
import Subjects





shelve1 = Shelves(300, [Subjects.book1])
shelve1.add_book(Subjects.book2, Subjects.book3)
print(len(shelve1))
# print(shelve1.unique_id)
# print(Subjects.book1.category.dict_of_categories[Subjects.book1.category.cat_name])
# print(Subjects.book2.category.dict_of_categories[Subjects.book2.category.cat_name])
