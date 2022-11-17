import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myTurtle.pensize(2)
myTurtle.pencolor("blue")


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(45)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,150)
myWin.exitonclick()
