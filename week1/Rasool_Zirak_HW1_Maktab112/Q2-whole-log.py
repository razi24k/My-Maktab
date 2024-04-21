x = int(input("Enter your number so I can show you that is it either power of two or not: "))
power = 1
base = 2
powered_two = 0
while powered_two <= x:
    powered_two = base ** power
    if x == powered_two:
        print(f"Yes! logarithm of {x} in base 2 is a whole number and that number is {power}")
        break
    else:
        power += 1
else:
    print(f"unfortunately logarithm of {x} in base 2 is not a whole number")
