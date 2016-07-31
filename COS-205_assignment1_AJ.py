#    COS-205_assignment1_AJ.py
#    A program that computes the interest accrued on an account
#    over a specified number of years into the future


def main():
    print("This program calculates the future value")
    print("of an investment over a specified period.")
    print()
    # prompt the user to enter the principal amount,
    # the yearly interest rate as a decimal number, the number
    # of compounding periods in a year, and the duration.
    principal = eval(input("Please enter the principal contribution: "))
    rate = eval(input("Please enter the annual interest rate as a decimal (ex. 4% is .04): "))
    periods = eval(input("Please enter the number of compounding periods in a year: "))
    years = eval(input("Please enter the number of years to calculate: "))
    print()
    # To compute the value in 10 years for example, the program should loop 10 *
    # periods times and accrue rate /period interest on each iteration.
    loopcount = years * periods
    for i in range(loopcount):
        principal = principal * (1 + rate / periods)

    # display the principal value at the end of the duration.
    print("The value in", years,"years is:", "$%0.2f"%(principal))


main()
