from gturtle import *
makeTurtle()

def quadrat40():
    repeat 4:
        forward(40)
        right(90)

setPenColor("dodger blue")
setPenWidth(3)

repeat 8:
    quadrat40()
    right(90)
    forward(40)
    left(90)
    penUp()
    back(20)
    penDown()


