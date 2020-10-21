from gturtle import *
makeTurtle()

def quadrat50():
    repeat 4:
        forward(50)
        right(90)

setPenColor("deep pink")
setPenWidth(3)

repeat 6:
    repeat 2:
        quadrat50()
        forward(50)
    back(100)
    right(90)
    forward(50)
    left(90)


