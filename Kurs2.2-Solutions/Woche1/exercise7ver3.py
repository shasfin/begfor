from gturtle import *

makeTurtle()

# Uses the fact that all values >255 are interpreted as 255 and <0 as 0.
def welle(color):
    up = color["up"]
    helligkeit = color["helligkeit"]
    if up:
        helligkeit += 1
    else:
        helligkeit -= 1
    if helligkeit >= 512:
        up = False
    if helligkeit <= -255:
        up = True
    return {"up": up, "helligkeit": helligkeit}
    
hideTurtle()

setPenWidth(20)

penUp()
left(90)
forward(500)
right(180)
penDown()

rot = {"up": False, "helligkeit": 512}
gruen = {"up": True, "helligkeit": 0}
blau = {"up": False, "helligkeit": 0}

repeat 1024:
    setPenColor(rot["helligkeit"], gruen["helligkeit"], blau["helligkeit"])
    forward(1)
    rot = welle(rot)
    gruen = welle(gruen)
    blau = welle(blau)
    
    

