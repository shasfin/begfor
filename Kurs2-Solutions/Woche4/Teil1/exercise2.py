from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("purple")

def quadrat_spirale(l, n):
    repeat n:
        repeat 4:
            forward(l)
            right(90)
        l += 5
        right(360/n)
            
quadrat_spirale(5, 50)
    

