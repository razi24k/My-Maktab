the_number = input("Enter a number: ")
while not the_number.isdigit():
    print("Please enter a number. come on!")
    the_number = input("Enter a number: ")

my_dict0_9 = {
    '0': '',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

my_dict10_19 = {
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety'
}

if len(the_number) == 2 and int(the_number) > 19:
    print(f"{my_dict10_19[str(int(the_number[0]) * 10)]} {my_dict0_9[the_number[1]]}")
elif len(the_number) == 2 and int(the_number) < 20:
    print(f"{my_dict10_19[the_number]}")
elif len(the_number) == 3:
    if int(the_number[1:]) > 19:
        print(
            f"{my_dict0_9[the_number[0]]} hundred {my_dict10_19[str(int(the_number[1]) * 10)]} {my_dict0_9[the_number[2]]}")
    elif int(the_number[1:]) < 20:
        print(f"{my_dict0_9[the_number[0]]} hundred {my_dict10_19[the_number[1:]]}")