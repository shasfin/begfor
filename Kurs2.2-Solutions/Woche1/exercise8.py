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
    delay(50)
    clear()
  
def nextRot(phase, rot):
    if phase == 2:
        return rot - 1
    else:
        return rot 
    
def nextGruen(phase, gruen):
    if phase == 1:
        return gruen + 1
    elif phase == 4:
        return gruen - 1
    else:
        return gruen 
    
def nextBlau(phase, blau):
    if phase == 3:
        return blau + 1
    else:
        return blau
    
def nextPhase(phase, rot, gruen, blau):
    if gruen >= 255 and phase == 1:
        return 2
    if rot <= 0 and phase == 2:
        return 3
    if blau >= 255 and phase == 3:
        return 4
    else:
        return phase
    
hideTurtle()

rot = 255
gruen = 0
blau = 0

phase = 1

repeat 1024:
    setPenColor(rot, gruen, blau)
    showmandala(6,4,50)
    right(10)
    
    rot = nextRot(phase, rot)
    gruen = nextGruen(phase, gruen)
    blau = nextBlau(phase, blau)
    phase = nextPhase(phase, rot, gruen, blau)
    
    
