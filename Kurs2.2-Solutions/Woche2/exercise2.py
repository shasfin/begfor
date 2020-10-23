from random import randint

def muenze_runde():
    zufallszahl = randint(1,2)
    print "Die Münze wurde geworfen."
    print "Glaubst du, du kannst die Zahl erraten?"


    zahl = input("Dein Versuch:")
    if zahl == zufallszahl:
        print "Richtig geraten!"
        return 1
    else:
        print "Leider ist es nicht", zahl
        print "Es war", zufallszahl, "!"
        return 0

richtig = 0
total = 0  
while(True):
    richtig += muenze_runde()
    total += 1
    weiter = input("Möchtest du weiterspielen?")
    if weiter != "ja" and weiter != "Ja" and weiter != "j":
        break

print "Richtig geraten:", richtig, "über", total
