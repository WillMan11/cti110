# CTI 110
# P5 T1 - Simple Graphics
# MangasW
# 8/11/2022


def drawTop(width):
    print("#" * width)

def drawSides(width):
    width = width - 2
    print("#" + " " * width + "#")

def drawMiddle(width, height):
    # for height times, draw sides with this width
    for line in range(height):
        drawSides(width)
    

def main():
    # program start here
    print("This program draws a rectangle")
    width = int(input("How wide?"))
    height = int(input("How tall?"))
    # draw top of box
    drawTop(width)
    # draw middle
    drawMiddle(width, height)
    # draw bottom
    drawTop(width)





# start program
main()
