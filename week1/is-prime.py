number = int(input("Enter a number: "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        print("Not a prime")
        is_prime = False
print(is_prime)

