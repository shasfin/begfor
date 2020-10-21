from gturtle import *
makeTurtle()

def sierpinsky_dreieck(n, g):
    if (n == 0):
        repeat 3:
            forward(g)
            left(120)
    else:
        repeat 3:
            sierpinsky_dreieck(n-1, g)
            forward(g)
            right(60)
            forward((2**n-2)*g)
            right(60)

setPenColor("deep pink")
setPenWidth(2)

hideTurtle()
right(90)
sierpinsky_dreieck(5,10)
