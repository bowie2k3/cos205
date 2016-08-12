#   COS-205_assignment2a_AJ.py
#   A program that calculates the area of a triangle
#   given user input for the lengths of its three sides

import math

def main():
    a, b, c = eval(input("Please enter the length of each side separated by commas (ex. a, b, c): "))
    print()

    # calculate sides, s = (a + b + c) / 2
    s = (a + b + c) / 2

    # calculate area
    a = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("The area of the triangle is:", a)

main()
