from gturtle import *

makeTurtle()
hideTurtle()

def stern(farbe, seite, winkel):
    setPenColor(farbe)
    right(winkel)
    repeat 8:
        forward(seite)
        right(90)
        forward(seite)
        left(45)
    left(winkel)
        
def show_stern_glow():
    repeat 10:
        show_stern("yellow", 50, 35)
        show_stern("orange", 50, 35)
        
def show_stern(farbe, seite, winkel):
        stern(farbe, seite, winkel)
        delay(5)
        clear()

        
show_stern_glow()

penUp()
forward(100)
left(90)
forward(100)
right(90)
penDown()
stern("blue", 100, 50)

seite = 10
winkel = 10
while seite < 100:
    show_stern("purple", seite, winkel)
    winkel += 5
    seite += 1
