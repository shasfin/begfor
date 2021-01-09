from gturtle import *
makeTurtle()

setPenColor("blue")

repeat 4:
    forward(50)
    right(90)
    repeat 2:
        forward(50)
        left(90)
    repeat 2:
        forward(50)
        right(90)

hideTurtle()