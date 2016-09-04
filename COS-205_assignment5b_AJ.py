
# Write a function to compute the nth Fibonacci number. A Fibonacci sequence
# is a sequence of numbers where each successive number is the sum of the
# previous two. The classic Fibonacci sequence begins as 1, 1, 2, 3, 5, 8, 13, ...


def fibo(n):
    fiba,fibb = 1,1
    for i in range(n-1):
        fiba,fibb = fibb,fiba+fibb
    return fiba


# Then write a main program that prompts the user to enter n and prints out
# the nth Fibonacci number. For example, if the user enters 6, then it should print out 8.


def main():

    n = eval(input("Please enter the desired nth Fibonacci number: "))
    number = fibo(n)
    print("The Fibonacci number in position", n, "is:", number)

main()