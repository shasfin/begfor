from gturtle import *
makeTurtle()

setPenColor("turquoise")

penUp()
back(200)
left(90)
forward(450)
right(90)
penDown()

repeat 7:
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(80)
    right(90)
    forward(60)
    right(90)
    forward(40)
    right(90)
    forward(20)
    right(90)
    repeat 2:
        forward(20)
        left(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(80)
    left(90)
    forward(100)
    left(90)

hideTurtle()