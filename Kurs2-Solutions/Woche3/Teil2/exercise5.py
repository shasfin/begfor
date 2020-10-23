from gturtle import *

makeTurtle()
hideTurtle()

def quadrat(seite):
    repeat 4:
        forward(seite)
        right(90)

def muster(seite):
    repeat 4:
        quadrat(seite/4)
        right(90)
        forward(seite)
        
        
setPenColor("magenta")
muster(200)
