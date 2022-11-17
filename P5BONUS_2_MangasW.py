import turtle

def tree(branchLen,t):
    if branchLen > 5:
        print("branch", branchLen)
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t) # FIRST
        t.left(40)
        tree(branchLen-15,t) # SECOND
        t.right(20)
        t.backward(branchLen)
        print("finished", branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.pensize(2)
    tree(75,t)
    myWin.exitonclick()

main()
