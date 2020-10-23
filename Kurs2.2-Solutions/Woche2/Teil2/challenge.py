from gturtle import *
makeTurtle()
hideTurtle()

def gehege_aufteilen(groessen, groessere, kleinere):
    for elem in groessen:
        if elem >= 70:
            groessere.append(elem)
        else:
            kleinere.append(elem)
            
def quadrat(seite):
    repeat 4:
        forward(seite)
        right(90)
        
def strasse(liste):
    strecke = 0
    for elem in liste:
        quadrat(elem)
        right(90)
        forward(elem)
        strecke += elem
        left(90)
    right(90)
    back(strecke)
    left(90)
    
def zoo(liste):
    small_cages = []
    big_cages = []
    gehege_aufteilen(liste, big_cages, small_cages)
    
    forward(70)
    strasse(small_cages)
    
    forward(100)
    strasse(big_cages)
    
cages = [40,90,30,50,80,20,40,30,60,100,30]
zoo(cages)
    
