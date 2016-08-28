# Write a program that counts the number of words in a text file.

# the program should print out [...] the number of words in the file.
# Your program should prompt the user for the file name, which
# should be stored at the same location as the program.
# It should consider anything that is separated by white space or
# new line on either side of a contiguous group of characters or
# character as a word.

def main():
    fname = input("Please enter the filename: ")
    infile = open(fname, "r")
    data = infile.read()
    stripnl = data.replace("\n", " ")
    words = stripnl.split(" ")
    count = len(words)
    print("The number of words in the file is: ", count)

main()