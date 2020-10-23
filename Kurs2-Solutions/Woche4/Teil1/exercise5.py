from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("medium purple")

def hexagon_spirale(side_initial, side_final, increment):
    side = side_initial
    while side <= side_final:
        forward(side)
        right(60)
        side += increment
            
hexagon_spirale(5, 400, 2)
    

