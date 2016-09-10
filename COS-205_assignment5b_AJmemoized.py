
# Write a function to compute the nth Fibonacci number. A Fibonacci sequence
# is a sequence of numbers where each successive number is the sum of the
# previous two. The classic Fibonacci sequence begins as 1, 1, 2, 3, 5, 8, 13, ...

import time

def fibo(n):
    memo = {}
    if n in memo:
        return memo
    if n <= 2:
        f = 1
    else:
        f = fibo(n-1)+fibo(n-2)
    memo[n] = f
    return f


# Then write a main program that prompts the user to enter n and prints out
# the nth Fibonacci number. For example, if the user enters 6, then it should print out 8.

start_time = time.time()
def main():
    start_time = time.time()
    n = eval(input("Please enter the desired nth Fibonacci number: "))
    number = fibo(n)
    print("The Fibonacci number in position", n, "is:", number)
    print("--- %s seconds ---" % (time.time() - start_time))
main()