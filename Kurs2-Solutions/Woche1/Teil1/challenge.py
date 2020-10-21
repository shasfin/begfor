from gturtle import *
makeTurtle()

# Start Dreieck 1
setPenColor("dark green")
right(30)
forward(100)
right(120)
forward(50) # halbe Seite

# Quadrat
setPenColor("orange")
left(60)

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

left(30)


# Continue Dreieck 1
setPenColor("dark green")
forward(50) # halbe Seite

left(120)

# Dreiek 2 and finish Dreieck 1
forward(100)
right(120)
forward(100)
right(120)
forward(200) # Basis von Dreieck 1 und Dreieck2
