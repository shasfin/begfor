from gturtle import *
makeTurtle()

setPenColor("blue")

repeat 3:
    repeat 4:
        forward(100)
        right(90)
    right(45)
    penUp()
    forward(sqrt(2)*50) # oder einen halben quadrat
    penDown()
    left(45)
