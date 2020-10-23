from gturtle import *

makeTurtle()
hideTurtle()

setPenColor("Light Sea Green")
setPenWidth(10)

def bar(l):
    forward(l)
    back(l)
    right(90)
    penUp()
    forward(20)
    penDown()
    left(90)
    
groesse = 5
repeat 22:
    bar(groesse)
    groesse += 10
