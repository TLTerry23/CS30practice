import turtle
import random
window=turtle.Screen()
window.bgcolor('lightblue')
alex=turtle.Turtle()
alex.color('blue')
billy=turtle.Turtle()
billy.color('red')
referee=turtle.Turtle()
referee.penup()
referee.goto(150,200)
referee.right(90)
referee.pendown()
referee.forward(300)



billy.penup()
alex.penup()
alex.goto(-10,100)
billy.goto(-10,0)
#finishline is at 150

while alex.xcor()<150 and billy.xcor()<150:
    alex.forward(random.randrange(2,10))
    billy.forward(random.randrange(2,10))
