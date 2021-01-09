from gturtle import *
makeTurtle()

setPenColor("blue")

penUp()
back(100)
penDown()

repeat 4:
    forward(50)
    right(90)
    repeat 2:
        forward(50)
        left(90)
    forward(50)
    right(90)
    forward(50)
    left(90)
    
    repeat 4:
        forward(50)
        right(90)
        repeat 2:
            forward(50)
            left(90)
        repeat 2:
            forward(50)
            right(90)

    left(180)
    
hideTurtle()