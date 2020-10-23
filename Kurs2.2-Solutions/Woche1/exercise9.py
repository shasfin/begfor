from gturtle import *

makeTurtle()

def vieleck(anz, laenge):
    repeat anz:
        forward(laenge)
        right(360/anz)
        
        
def mandala(outer, inner, side):
    repeat outer:
        vieleck(inner, side)
        right(360/outer)
        
def showmandala(outer, inner, side):
    mandala(outer, inner, side)
    delay(5)
    clear()
  
# Uses the fact that all values >255 are interpreted as 255 and <0 as 0.
def welle(color):
    up = color["up"]
    helligkeit = color["helligkeit"]
    if up:
        helligkeit += 3
    else:
        helligkeit -= 3
    if helligkeit >= 512:
        up = False
    if helligkeit <= -255:
        up = True
    return {"up": up, "helligkeit": helligkeit}
    
hideTurtle()

rot = {"up": False, "helligkeit": 512}
gruen = {"up": True, "helligkeit": 0}
blau = {"up": False, "helligkeit": 0}

repeat 1024:
    setPenColor(rot["helligkeit"], gruen["helligkeit"], blau["helligkeit"])
    showmandala(6,4,50)
    right(10)
    
    rot = welle(rot)
    gruen = welle(gruen)
    blau = welle(blau)
    
    
