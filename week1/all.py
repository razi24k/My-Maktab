# Q 6
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(0, len(my_list)):
    print(i, my_list[i])

# Q 7
ten_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_half = ten_list[:len(ten_list) // 2]
second_half = ten_list[len(ten_list)//2:]
print(f"The first half is {first_half}, and the second half is {second_half}")

# Q 8
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[-4:])

# Q 9
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[-2:-9:-2])

# Q 10
my_list = input("enter some number separated by spaces: ").split(" ")
if my_list[0] == "":
    my_list.pop()
print(my_list)
print(not bool(my_list))

# Q 11
my_list1 = input("enter some number separated by spaces: ").split(" ")
my_list2 = input("enter some number separated by spaces: ").split(" ")
my_list1.extend(my_list2)
print

# Q 12
my_list = input("Enter a list of numbers seperated by spaces: ").split()
num_list = list(map(int, my_list))
primes_list = []
for num in num_list:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes_list.append(num)
print(sorted(primes_list, reverse=True))

# Q 13
# 13-1
my_list = input("Enter a list of numbers: ").split()
nums = list(map(int, my_list))
nums.sort(reverse=True)
print(nums)
# 13-2
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))
if x > y and x > z:
    if y > z:
        print(x, y, z)
    else:
        print(x, z, y)
elif y > x and y > z:
    if x > z:
        print(y, x, z)
    else:
        print(y, z, x)
else:
    if x > y:
        print(z, x, y)
    else:
        print(z, y, x)

# Q 14
# 14-1
num = int(input("Enter a number: "))
counter = 0
while num > 0:
    counter += 1
    num //= 10
print(counter)
# 14-2
num = input("Enter a number: ")
print(len(num))

# Q 15
text1 = input("Enter a string: ").lower()
text2 = input("Enter another string: ").lower()
for i in text1:
    if i not in text2 or text1.count(i) != text2.count(i):
        print("Not an Anagram")
        break
else:
    print("Anagram")

# Q 16
# 1
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
unique_list = []
for i in my_list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)
# 2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
unique_list = list(set(my_list))
print(unique_list)

# Q 17
string = input("Enter a word: ").lower()
unique_str = ""
for i in string:
    if i not in unique_str:
        unique_str +=i
print(unique_str)

# Q 18
# # 1
text = input("Enter a text: ")
counter = 0
counter += text.count('x')
counter += text.count('X')
print(counter)
# 2
copy_text = text.lower()
cntX = copy_text.count('x')
print(cntX)

# Q 19
text = input("Enter a text: ").lower()
abc_count = text.count("abc")
print(abc_count)

# Q 20
my_list = list(map(int, input("Enter the numbers separated by spaces: ").split(" ")))
evens = [i for i in my_list if i % 2 == 0]
evens.sort(reverse=True)
print(evens)