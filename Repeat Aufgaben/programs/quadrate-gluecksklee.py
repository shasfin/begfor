﻿from gturtle import *
makeTurtle()

repeat 4:
    repeat 3:
        repeat 4:
            forward(30)
            right(90)
        right(90)
        forward(30)
    forward(30)
    left(90)
    forward(120)
    right(90)

hideTurtle()