# COS-205_assignment7_AJ.py
# Euclid's algorithm n, m=m, n%m (i.e., n is replaced by m, and m is replaced by n%m) until m is 0.


def gcd(n, m):
        while m:
            n, m = m, n % m
        return n


def main():
    error = "The number entered is not a positive whole number!"
    while True:
        n, m = 0, 0
        # prompt user for two positive whole numbers
        # if the user enters a zero or negative number, display an error
        while n <= 0 or n % 1 != 0:
            n = eval(input("\nEnter a positive whole number: "))
            if n <= 0 or n % 1 != 0:
                print(error)
        while m <= 0 or m % 1 != 0:
            m = eval(input("Enter a second positive whole number: "))
            if m <= 0 or m % 1 != 0:
                print(error)
        print("\nThe GCD of", n, "and", m, "is", gcd(n, m))
        ans = input("\nCompute another GCD (Y/N): ").lower()
        if ans in ["no", "n"]:
            print("\nGoodbye")
            break
        if ans in ["yes", "y"]:
            continue


main()
