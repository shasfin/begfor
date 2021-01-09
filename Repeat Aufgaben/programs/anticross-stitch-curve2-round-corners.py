from gturtle import *
makeTurtle()

setPenColor("blue")

penUp()
back(85)
penDown()

def lft(angle):
    repeat 10:
       forward(1)
       left(angle/10)
       
def rgt(angle):
    repeat 10:
       forward(1)
       right(angle/10)

repeat 4:
    forward(43)
    rgt(90)
    repeat 2:
        forward(43)
        lft(90)
    forward(43)
    rgt(90)
    forward(43)
    lft(90)
    
    repeat 3:
        forward(43)
        rgt(90)
        repeat 2:
            forward(43)
            lft(90)
        repeat 2:
            forward(43)
            rgt(90)
    forward(43)
    rgt(90)
    repeat 2:
        forward(43)
        lft(90)
    forward(43)
    rgt(90)
    forward(43)
    lft(90)
    

