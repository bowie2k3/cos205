
# Write a function to compute the nth Fibonacci number. A Fibonacci sequence
# is a sequence of numbers where each successive number is the sum of the
# previous two. The classic Fibonacci sequence begins as 1, 1, 2, 3, 5, 8, 13, ...


def fibo(n):
    seqa,seqb = 1,1
    for i in range(n-1):
        seqa,seqb = seqb,seqa+seqb
    return seqa


# Then write a main program that prompts the user to enter n and prints out
# the nth Fibonacci number. For example, if the user enters 6, then it should print out 8.


def main():
    prompt = eval(input("Please enter the desired nth Fibonacci number: "))
    number = fibo(prompt)
    print("The Fibonacci number in position", prompt, "is:", number)

main()