from gturtle import *
makeTurtle()

colors = ["dark red", "red", "orange red", "orange", "gold", "yellow", "lime", "green", "teal", "blue", "purple", "medium purple", "deep pink", "magenta"]

def makeStar(color, size):
    setPenColor(color)
    repeat 6:
        repeat 6:
            forward(size)
            right(60)
        right(60)
        
def showStar(color, size):
    makeStar(color, size)
    delay(10)
    clear("black")
            
hideTurtle()
speed(-1)

repeat 100:
    i = 0
    size = 10
    repeat 14:
        showStar(colors[i], size)
        right(20)
        size = size + 0.25*size
        i = i + 1
        
    i = i - 1
    repeat 14:
        showStar(colors[i], size)
        left(20)
        size = size - 0.25*size
        i = i - 1
