from gturtle import *
makeTurtle()

setPenColor("lime")
repeat 6:
    repeat 4:
        forward(50)
        right(90)
    penUp()
    right(90)
    forward(100)
    left(90)
    penDown()

right(180)

setPenColor("dark red")
repeat 5:
    penUp()
    right(90)
    forward(100)
    left(90)
    penDown()
    repeat 4:
        forward(50)
        right(90)

