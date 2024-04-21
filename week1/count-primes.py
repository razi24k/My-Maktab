x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
primes = []
if x < y:
    for i in range(x, y):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
else:
    print("second number has to be greater than first number")
print(primes)
