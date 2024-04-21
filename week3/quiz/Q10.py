password = input("Enter your password: ")
length_pass = False
if len(password) > 7:
    length_pass = True
upper_pass = False
lower_pass = False
digit_pass = False
for i in password:
    if i.isupper():
        upper_pass = True
    elif i.islower():
        lower_pass = True
    elif i.isdigit():
        digit_pass = True
if all([length_pass, upper_pass, lower_pass, digit_pass]):
    print(True)
else:
    print(False)