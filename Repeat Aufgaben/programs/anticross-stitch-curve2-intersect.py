from gturtle import *
makeTurtle()

setPenColor("blue")

penUp()
back(100)
penDown()

repeat 4:
    forward(150)
    left(90)
    forward(100)
    right(90)
    repeat 3:
        forward(150)
        repeat 2:
            right(90)
            forward(50)
        right(90)
    forward(150)
    right(90)
    forward(100)
    left(90)

hideTurtle()