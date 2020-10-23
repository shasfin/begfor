from gturtle import *

makeTurtle()

def vieleck(anz, laenge):
    repeat anz:
        forward(laenge)
        right(360/anz)
        
        
def mandala(outer, inner, side):
    repeat outer:
        vieleck(inner, side)
        right(360/outer)
        
def showmandala(outer, inner, side):
    mandala(outer, inner, side)
    delay(50)
    clear()
    
    
hideTurtle()
repeat 360:
    showmandala(6,4,50)
    right(10)
    
