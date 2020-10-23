from gturtle import *

makeTurtle()
hideTurtle()

def diagramm(liste, sfactor):
    red = 0
    green = 0
    blue = 255
    setPenWidth(20)
    for elem in liste:
        green = elem*sfactor
        setPenColor(red, green, blue)
        
        forward(elem*sfactor)
        back(elem*sfactor)
        
        penUp()
        right(90)
        forward(30)
        left(90)
        penDown()
        
        
diagramm([100,200,120,150,180,30,45, 255], 1)
        
