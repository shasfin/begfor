from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("Light Sea Green")

def spirale(side_initial, side_final, increment):
    side = side_initial
    while side <= side_final:
        forward(side)
        right(120)
        side += increment
            
spirale(5, 400, 5)
    

