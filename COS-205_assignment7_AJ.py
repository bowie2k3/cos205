"""The greatest common divisor (GCD) of two values can be computed using Euclid’s algorithm.
Starting with the values of n and m where n > m, we repeatedly apply the formula:

n, m=m, n%m (i.e., n is replaced by m, and m is replaced by n%m) until m is 0.
At that point, n is the GCD of the original n and m.

Your program should prompt the user for two positive whole numbers (i.e., 1, 2, 3, …).
If the user enters a zero or negative number, your program should display an error message
and keep prompting until a valid number is entered.

After computing a GCD, your program should ask the user if he or she would like
to do another computation or not. If the user enters Yes or Y (case insensitive),
it should do another computation; and if the user enters No or N (case insensitive),
it should terminate execution.
"""


def gcd():
    result = 0
    while True:
        n = eval(input("Please enter a positive whole number: "))
        m = eval(input("Please enter a second whole number: "))
        if n > 0 and m > 0:
            while m > 0:
                n = m
                m = n % m
            print("The GCD of ", n, "and", m, "is", result)
        else:
            print("The number entered is not a positive whole number!")


gcd()