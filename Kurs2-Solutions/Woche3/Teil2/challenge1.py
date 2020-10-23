from gturtle import *

makeTurtle()
hideTurtle()

def quadrat(seite):
    repeat 4:
        forward(seite)
        right(90)

def sternOld(seite):
    repeat 8:
        forward((seite/3)/sqrt(2))
        right(90)
        forward((seite/3)/sqrt(2))
        right(45)
        forward(seite/3)
        back(seite/3)
        right(180)
        
def stern(seite):
    repeat 2:
        penUp()
        repeat 2:
            forward(seite/2)
            right(90)
        penDown()
        quadrat(seite)
        penUp()
        repeat 2:
            forward(seite/2)
            right(90)
        penDown()
        right(45)
    left(90)

        
setPenColor("orange")
stern(150)
stern(300)
