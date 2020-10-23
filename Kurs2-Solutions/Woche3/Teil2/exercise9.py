from gturtle import *

makeTurtle()
hideTurtle()

def halb_polygon(farbe, seite, n_ecken):
    setPenColor(farbe)
    repeat n_ecken / 2:
        forward(seite)
        right(360/n_ecken)

def kreis(farbe1, farbe2):
    halb_polygon(farbe1, 3, 120)
    halb_polygon(farbe2, 3, 120)
    halb_polygon(farbe1, 3, 120)
    
repeat 2:
    kreis("orange", "dark green")
    right(180)
    kreis("dark green", "orange")
    right(180)
