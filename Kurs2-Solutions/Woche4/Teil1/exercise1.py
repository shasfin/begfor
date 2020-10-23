from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("deep pink")
setPenWidth(3)

def spiral_inside_out(innermost_side, outermost_side, increment):
    seite = innermost_side
    while seite <= outermost_side:
        forward(seite)
        right(90)
        seite += increment
    
def spiral_outside_in(innermost_side, outermost_side, decrement):
    seite = outermost_side
    while seite >= innermost_side:
        forward(seite)
        right(90)
        seite -= decrement

spiral_inside_out(5, 300, 5)
left(90)
spiral_outside_in(5, 300, 5)
    

