from gturtle import *
makeTurtle()

repeat 6:
    repeat 2:
        repeat 4:
            forward(30)
            right(90)
        right(90)
        forward(30)
        left(90)
    forward(30)
    left(90)
    forward(60)
    right(90)

hideTurtle()