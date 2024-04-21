Z_len, A_B_len = list(map(int, input("Please enter Z len and A,B len seperated by spaces: ").split(" ")))
while Z_len < 0 or A_B_len < 0:
    print("Invalid input")
    Z_len, A_B_len = list(map(int, input("Please enter Z len and A,B len seperated by spaces: ").split(" ")))
Z = list(map(int, input("Please enter amounts of Z list seperated by spaces: ").split(" ")))
while len(Z) != Z_len:
    print("number of amounts out of range")
    print(f"you entered {Z_len} number as len of Z")
    Z = list(map(int, input("Please enter amounts of Z list seperated by spaces: ").split(" ")))
A = list(map(int, input("Please enter amounts of A list seperated by spaces: ").split(" ")))
while len(A) != A_B_len:
    print("number of amounts out of range")
    print(f"you entered {A_B_len} number as len of A")
    A = list(map(int, input("Please enter amounts of A list seperated by spaces: ").split(" ")))
B = list(map(int, input("Please enter amounts of B list seperated by spaces: ").split(" ")))
while len(B) != A_B_len:
    print("number of amounts out of range")
    print(f"you entered {A_B_len} number as len of B")
    A = list(map(int, input("Please enter amounts of B list seperated by spaces: ").split(" ")))
happiness = 0
for i in A:
    if i in Z:
        happiness += 1
for i in B:
    if i in Z:
        happiness -= 1
print(f"your happiness is {happiness}")

