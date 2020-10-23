from gturtle import *

makeTurtle()

penUp()
left(90)
forward(400)
right(180)
penDown()


setPenWidth(20)

gruen = 0

repeat 256:
    setPenColor(255, gruen, 0)
    forward(3)
    gruen = gruen + 1
