from gturtle import *
makeTurtle()

setPenWidth(3)
setPenColor("lime")

def makeCircle():
    repeat 100:
        forward(1)
        right(3)
    setPenColor("dark red")
    repeat 20:
        forward(1)
        right(3)
    setPenColor("lime")
    
        
def showCircle(move, angle):
    right(angle)
    makeCircle()
    left(angle)
    delay(5)
    clear()
    penUp()
    right(90)
    forward(move)
    left(90)
    penDown()
            
hideTurtle()
speed(-1)

penUp()
left(90)
forward(400)
right(90)
penDown()

move = 10
angle = 0
repeat 80:
    showCircle(move, angle)
    angle = angle + 12

