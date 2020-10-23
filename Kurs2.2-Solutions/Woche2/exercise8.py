from gturtle import *

makeTurtle()
hideTurtle()

laenge = 0.1
winkel = 15

while laenge <= 10 and winkel >= 1:
    forward(laenge)
    right(winkel)
    laenge+=0.05
    winkel-=0.05

