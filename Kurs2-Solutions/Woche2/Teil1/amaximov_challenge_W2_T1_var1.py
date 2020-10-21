from gturtle import *
makeTurtle()

right(90)

def dreieck_klein():
    repeat 3:
        forward(50)
        left(120)

def dreieck_mittel():
    repeat 3:
        dreieck_klein()
        forward(50)
        right(120)
        
def dreieck_gross():
    repeat 3:
        dreieck_mittel()
        forward(50)
        right(60)
        forward(100)
        right(60)

setPenColor("deep pink")
setPenWidth(3)

repeat 3:
    dreieck_gross()
    forward(50)
    right(60)
    forward(300)
    right(60)




