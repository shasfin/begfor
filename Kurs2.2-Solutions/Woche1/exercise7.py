from gturtle import *

makeTurtle()

setPenWidth(20)

penUp()
left(90)
forward(500)
right(180)
penDown()

rot = 255
gruen = 0
blau = 0

phase = 1

repeat 1024:
    setPenColor(rot, gruen, blau)
    forward(1)
    if (phase == 1):
        gruen += 1
    if (phase == 2):
        rot -= 1
    if (phase == 3):
        blau += 1
    if phase == 4:
        gruen -= 1
    if gruen >= 255 and phase == 1:
        phase = 2
    if rot <= 0 and phase == 2:
        phase = 3
    if blau >= 255 and phase == 3:
        phase = 4
        
        
# Variante zwei:


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

setPenWidth(20)

penUp()
left(90)
forward(500)
right(180)
penDown()

rot = 255
gruen = 0
blau = 0

phase = 1

repeat 1020:
    setPenColor(rot, gruen, blau)
    forward(1)
    
    rot = nextRot(phase, rot)
    gruen = nextGruen(phase, gruen)
    blau = nextBlau(phase, blau)
    phase = nextPhase(phase, rot, gruen, blau)
    
    
