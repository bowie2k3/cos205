import math

prime_numbers = 0

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(int(input("How many numbers you wish to check: "))):
    if is_prime(i):
        prime_numbers += 1
        print(i)

print("We found " + str(prime_numbers) + " prime numbers.")