# COS-205_assignment7_AJ.py
# v1.2 - Added is_whole function and error handling.


def gcd(n, m):
    while m:
        n, m = m, n % m
    return n


def is_whole(x):
    error = "The number entered is not a positive whole number!"
    # Check that a number is positive and whole
    if x > 0 and x % 1 == 0:
        return True
    # if the user enters a zero or negative number, display an error
    elif x < 0 or x % 1 != 0:
        print(error)


def main():
    error = "The number entered is not a positive whole number!"
    try:
        while True:
            n, m = 0, 0
            # prompt user for two positive whole numbers
            print()
            while not is_whole(n):
                n = eval(input("Enter a positive whole number: "))
                if n == 0:
                    print(error)
            while not is_whole(m):
                m = eval(input("Enter a second positive whole number: "))
                if m == 0:
                    print(error)
            print("\nThe GCD of", n, "and", m, "is", gcd(n, m))
            # After computing a GCD, your program should ask the user if he or she would like to do
            # another computation or not. If the user enters Yes or Y (case insensitive),
            ans = input("\nCompute another GCD (Y/N): ").lower()
            if ans in ["no", "n"]:
                print("\nGoodbye!")
                break
            if ans in ["yes", "y"]:
                continue
    except NameError:
        print("Sorry, that was not a valid number.  Please try again.")
    except SyntaxError:
        print("Sorry, that was not a valid number.  Please try again.")


main()
