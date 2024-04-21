txt = input("Enter a sentence without space I'll fix it: ")
txt_list = list(txt)
result = ""
for i in txt_list:
    if i.isupper():
        result += i.rjust(2, " ")
    else:
        result += i
result = result.rstrip()
print(result)