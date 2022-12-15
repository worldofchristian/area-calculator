import turtle
import numpy

circleR = input("Type the size of your desired circle and hit enter\n")

area = ""

def printer():
    global circleR
    """
    initalizes turtle window as a private variable (to avoid it from popping
    up before there's an input to use)

    checks if the input is suitable to be used

    if it is, calls the calculator, prints the area to terminal, opens turtle window 
    """

    # turtle window
    t = turtle.Turtle()

    # error messages
    if int(circleR) > 500:
        print("that's a little too big")
    elif int(circleR) < 1:
        print("needs to be at least one pixel")

    # runs the calculator, runs, turtle, prints to terminal
    elif 2000 > int(circleR) > 1:
        calculator()

        print("Area:")
        print(area,"px")

        t.pensize(10)
        t.circle(int(circleR))
        turtle.Screen().exitonclick()

def calculator():
    global circleR, area

    area = (((int(circleR)/2)**2)*numpy.pi)
    return area

printer()