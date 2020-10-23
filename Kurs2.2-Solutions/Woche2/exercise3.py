from random import randint

def wuerfel_runde():
    zufallszahl = randint(1,6)
    print "Der Würfel wurde geworfen."
    print "Glaubst du, du kannst die Zahl erraten?"


    zahl = input("Dein Versuch:")
    if zahl == zufallszahl:
        print "Richtig geraten!"
    else:
        print "Leider ist es nicht", zahl
        print "Ich hatte", zufallszahl, "gewürfelt!"
        
while(True):
    wuerfel_runde()
    weiter = input("Möchtest du weiterspielen?")
    if weiter != "ja" and weiter != "Ja" and weiter != "j":
        break

