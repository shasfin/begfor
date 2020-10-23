from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("teal")

def spiral(l, n):
    repeat n:
        forward(l)
        right(360/n)
        l += 1

spiral(1, 120)
