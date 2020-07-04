import turtle



sides=int(input("Number of sides: "))
degree_turn=360/sides
alex=turtle.Turtle()
window=turtle.Screen()
sides_drawn=sides

for c in range (sides_drawn):
    alex.forward(50)
    alex.left(degree_turn)
