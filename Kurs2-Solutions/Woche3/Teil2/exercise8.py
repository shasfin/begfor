from gturtle import *

makeTurtle()
hideTurtle()

def quadrat(seite):
    repeat 4:
        forward(seite)
        left(90)

def window(seite, row, column):
    repeat column:
        repeat row:
            quadrat(seite)
            left(90)
            forward(seite)
            right(90)
        right(90)
        forward(row*seite)
        left(90)
        forward(seite)
    right(180)
    forward(column*seite)
    left(180)
    
def pala(laenge):
    seite = laenge / 9
    forward(seite * 3)
    right(90)
    window(seite,6,2)
    right(90)
    forward(seite * 3)
    right(180)
    
def mulino(laenge):
    repeat 4:
        pala(laenge)
        right(90)
        
right(45) 
mulino(180)
# pala(180)
# window(20,6,2)
