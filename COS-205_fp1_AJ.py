# COS-205_fp1_AJ.py
# Final Project 1 of 4
# Write a program to draw a quiz score histogram.


from graphics import *


def main():
    # program should read data from a file,
    file = open('qscores.txt', 'r')
    # each line of the file contains one number in the range 0 to 10
    scores = [0,1,2,3,4,5,6,7,8,9,10]
    for i in file:
        scores[int(i)] += 1
    # Draw score histogram window
    win = GraphWin("Quiz Score Histogram", 360, 360)
    win.setCoords(0, 0, 36, 36)
    # X & Y Axis Lines
    Line(Point(1, 5), Point(35, 5)).draw(win)
    Line(Point(1, 5), Point(1, 25)).draw(win)
    title = Text(Point(10, 25), "Student Score Histogram")
    title.setFill('Black')
    title.draw(win)
    position = 2
    for i in range(11):
        # Count the number of occurrences of each score
        # draw a vertical bar chart for each possible score (0 to 10)
        # height corresponding to the number that score.
        bar = Rectangle(Point(position,5),Point(position+2,scores[i]+5))
        bar.setFill("Blue")
        bar.draw(win)
        # shift bar for each line/score
        position += 3
    position = 3
    for i in range(11):
        # Added score text to each bar
        Text(Point(position,4),i).draw(win)
        # shift text pring along with each line
        position += 3
    file.close()
    #   When the user clicks anywhere on the window, it should close.
    closetext = Text(Point(17.5, 2), "Click anywhere to close")
    closetext.setFill('Red')
    closetext.draw(win)
    win.getMouse()
    win.close()



main()
