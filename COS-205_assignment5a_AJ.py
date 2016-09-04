# Write functions for the following:
# sphereArea (radius): It returns the surface area of a sphere having the given radius.
# The formula is  A = 4 πr2.

import math

def sphereArea(radius):
    area = 4 * math.pi * radius**2
    return area

#  sphereVolume(radius): It returns the volume of a sphere having the given radius.
# The formula is  V = (4/3) πr3.

def sphereVolume(radius):
    vol = (4/3) * math.pi * radius**3
    return vol

# Then write a main program that uses these functions to compute the surface area
# and volume of a sphere given the radius. The program should prompt the user for
# the radius and then print out the surface area and volume.

def main():
    radius = eval(input("Please enter radius of a sphere: "))

    area = sphereArea(radius)
    volume = sphereVolume(radius)

    print("The area of the sphere is", "%0.2f"%area, "and its volume is", "%0.2f"%volume)

main()
# Submit your program as a single file named “COS-205_assignment 5a_<your initials>.py”,
# which should include both functions as well as the main program.


