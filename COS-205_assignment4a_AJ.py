# COS-205_assignment4a_AJ.py
# Write a program that calculates and prints out the numeric value
# of a single name provided as input by the user.

# The value of a name is determined by summing up the values of the letters
# of the name where “a” or “A” is 1, “b” or “B” is 2, and so on, up to “z” or “Z” being 26

name = input("Please enter a name: ")
name = name.lower()

total = 0
for each in name:
    val = ord(each)-96
    total = total + val

print("The numeric value of the name is:", total)


