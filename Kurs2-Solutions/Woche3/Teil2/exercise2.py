from gturtle import *

makeTurtle()
hideTurtle()

def dreieck(seite):
    repeat 3:
        forward(seite)
        right(120)

setPenColor("lime")
for groesse in range(20,140,20):
    dreieck(groesse)
