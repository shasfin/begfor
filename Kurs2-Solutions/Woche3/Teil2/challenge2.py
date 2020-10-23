from gturtle import *

makeTurtle()
hideTurtle()

def strahl(farbe1, farbe2, groesse):
    setPenColor(farbe1)
    repeat 50:
        forward(groesse/100)
        right(3)
    setPenColor(farbe2)
    right(180)
    gr = groesse / 20
    repeat 10:
        dot(gr)
        gr /= 1.2
        penUp()
        repeat 5:
            forward(groesse/100)
            left(3)
        penDown()
    right(180)
    
def mandala(farbe1, farbe2, groesse, n_rep):
    repeat n_rep:
        strahl(farbe1, farbe2, groesse)
        right(360/n_rep)
        
mandala("red", "green", 400, 17)
