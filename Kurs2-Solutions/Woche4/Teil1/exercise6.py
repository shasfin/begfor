from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("medium purple")

def circle(l, n):
    repeat n:
        forward(l)
        right(360/n)
            
l = 1
n = 120
repeat 8:
    circle(l, n)
    l += 1
    
right(180)

l = 5
n = 60
repeat 8:
    circle(l, n)
    n += 60
