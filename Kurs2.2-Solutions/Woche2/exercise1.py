from random import randint

zufallszahl = randint(1,10)
print "Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht!"
print "Glaubst du, du kannst sie erraten?"
print "Du hast 3 Versuche."

repeat 3:
    zahl = input("Dein Versuch: ")
    if zahl == zufallszahl:
        print "Richtig geraten!"
        break
    else:
        print "Leider ist es nicht", zahl
        
print "Ich hatte mir", zufallszahl, "ausgedacht!"
