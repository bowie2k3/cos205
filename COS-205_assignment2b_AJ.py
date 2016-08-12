#   COS-205_assignment2b_AJ.py
#   A program that finds the sum of the first n natural numbers.
#   The program prompts the user for the value of n then prints the sum

def main():
    n = eval(input("Please enter a whole number: "))
    print()

    # initialize total to 1 to include real number range up-to and including provided number.
    total = 1

    for number in range(n):
        total = number + total

    print(total)

main()
