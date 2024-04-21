# import the product function from itertools module
# from itertools import product
#
#
# x = 123
# x_str = str(x)
# x_str_list = list(x_str)
# # print(xsl)
# my_list = []
# for i in range(1, len(x_str_list)+1):
#     my_list.append(list(product(x_str_list, repeat=i)))
# res_list = []
# # print(my_list)
# for i in my_list:
#     for j in i:
#         if all(j.count(d) == 1 for d in j):
#             res_list.append(j)
# # print(res_list)
# joined_list = []
# for i in res_list:
#     joined_list.append("".join(i))
# # print(joined_list)
# int_res_list = list(map(int, joined_list))
# print(int_res_list)
# print("The cartesian product using repeat:")
# print(list(product([1, 2], repeat=3)))
# print()
#
# print("The cartesian product of the containers:")
# print(list(product(['geeks', 'for', 'geeks'], '2')))
# print()
#
# print("The cartesian product of the containers:")
# print(list(product('AB', [3, 4])))
from itertools import permutations

# print("All the permutations of the given list is:")
# print(list(permutations([1, 'geeks'], 2)))
# print()
#
# print("All the permutations of the given string is:")
# print(list(permutations('AB')))
# print()
#
# print("All the permutations of the given container is:")
# print(list(permutations(range(3), 3)))
x = 547
x_str = str(x)
x_str_list = list(x_str)
# print(xsl)
res_list = []
for i in range(1, len(x_str_list)+1):
    res_list.append(list(permutations(x_str_list, i)))
# print(my_list)
joined_list = []
for i in res_list:
    for j in i:
        joined_list.append("".join(j))
# print(joined_list)
int_res_list = list(map(int, joined_list))
print(int_res_list)