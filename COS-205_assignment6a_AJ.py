# Write a program that accepts a speed limit and a clocked speed from the user,
# and either prints a message indicating the speed was legal or prints the amount
# of the fine, if the speed was illegal.


def speeding(limit, clocked):
    fine = 0
    if limit >= clocked:
        print("Speed was legal.")
        exit(0)
    else:
        if limit < clocked:
            # The speeding ticket fine policy in Podunskville is $50 plus $5 for each mph over
            fine = (clocked - limit) * 5
    # the speed limit plus a penalty of $200 for any speed over 90 mph
        if clocked > 90:
            fine += 200
        return fine


def main():
    print()
    limit = eval(input("Please enter posted speed limit: "))
    speed = eval(input("Please enter clocked speed: "))
    fine = speeding(limit, speed)
    print("The amount of the fine is $" + str(fine))

main()