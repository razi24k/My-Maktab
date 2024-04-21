number = int(input("Enter a number: "))
if number <= 1:
    print("Invalid")
else:
    divisors = [i for i in range(1, number//2 + 1) if number % i == 0]
    if sum(divisors) == number:
        print("Yes")
    else:
        print("No")
