from gturtle import *

makeTurtle()

# Uses the fact that all values >255 are interpreted as 255 and <0 as 0.
def welle(color):
    up = color["up"]
    helligkeit = color["helligkeit"]
    if up:
        helligkeit += 8
    else:
        helligkeit -= 8
    if helligkeit >= 512:
        up = False
    if helligkeit <= -255:
        up = True
    return {"up": up, "helligkeit": helligkeit}
    
hideTurtle()

def strahl():
    penUp()
    forward(255+127)
    penDown()
    right(180)
    gradient()
    penUp()
    forward(255)
    left(180)
    penDown()

def gradient():
    rot = {"up": False, "helligkeit": 512}
    gruen = {"up": True, "helligkeit": 0}
    blau = {"up": False, "helligkeit": 0}
    
    repeat 127:
        setPenColor(rot["helligkeit"], gruen["helligkeit"], blau["helligkeit"])
        forward(1)
        rot = welle(rot)
        gruen = welle(gruen)
        blau = welle(blau)

setPenWidth(40)
penUp()
back(200)
penDown()

left(90)
repeat 37:
    strahl()
    right(5)

    
    

