txt_list = list(input("Please provide your magic word: "))
letters = 0
digits = 0
for item in txt_list:
    if item.isalpha():
        letters += 1
    elif item.isdigit():
        digits += 1
print(f"letters: {letters}\ndigits: {digits}")