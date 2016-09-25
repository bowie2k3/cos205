# COS-205_assignment6b_AJ.py
# Modify the program you wrote for Programming Assignment 3 (Module 3) to handle the case when the line
# does not intersect the circle. You should use Python’s exception handling using try/catch to catch
# the error and print out a customized error message.


from graphics import *
from math import *


def main():

    win = GraphWin('COS205 Module 3', 480, 480)
    try:
        #   Input: Radius of the circle and the y-intercept of the line. Prompt the user for these values.
        r = eval(input("Please provide the desired radius of the circle: "))
        ycept = eval(input("Please provide the desired y-intercept: "))

        #   Output: Draw a circle centered at (0,0) with the given radius in a window
        #   with coordinates running from (–10,–10) to (10,10).
        # win = GraphWin('COS205 Module 3', 480, 480)
        win.setCoords(-10, -10, 10, 10)
        center = Point(0, 0)
        c = Circle(center, r)
        c.setFill('red')
        c.draw(win)

        #    Draw a horizontal line across the window with the given y-intercept.
        line = Line(Point(-10, ycept), Point(10, ycept))
        line.draw(win)

        # Calculate x axis points of intercept
        # Formula for the intersection values of x:
        # where r is the radius and y is the y-intercept.
        #  (+/-)x = sqrt(r ** 2 - y ** 2)
        x1 = round(sqrt(r ** 2 - ycept ** 2),2)
        x2 = -x1

        x = 0
        y1 = round(sqrt(r ** 2 - x * x),2)
        y2 = -y1

        #    Print out the x values of the points of intersection in the upper left-hand corner of the window.
        xmsg = 'X = ' + str(x1) + ' ' + str(x2)
        ymsg = 'Y = ' + str(y1) + ' ' + str(y2)
        t = Text(Point(-6, 9), xmsg)
        t.setSize(8)
        t.draw(win)
        t2 = Text(Point(-6, 8), ymsg)
        t2.setSize(8)
        t2.draw(win)

        #    Draw the two points of intersection in red.
        point1 = Circle(Point(x1, y1), 0.2)
        point1.setFill('red')
        point2 = Circle(Point(x2, y2), 0.2)
        point2.setFill('red')
        point1.draw(win)
        point2.draw(win)

    except ValueError:
        print("\nThe line does not intersect the circle.")

    #   When the user clicks anywhere on the window, it should close.
    win.getMouse()
    win.close()

main()
