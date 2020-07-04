#Pon_Step2(Revisited)
#November 1/19
#Robot will move from left to right,
#if flower is present, take(), else move()
#after taking() flowers, robot will put() all of them, 
#then move() to finish

from library import draw_one, turn_right, turn_around, draw_zero, reposition_one, reposition_zero
think(50)

#3 moves to set up
move()
turn_left()
move()

#draw_one robot puts and moves
draw_one()

#reposition_one() after drawing a one, resets robot to draw next figure
reposition_one()

#draw_zero uses draw_one function, move, put to draw a zero
draw_zero()

#reposition_zero() after drawing a zero, resets robot to draw next figure
reposition_zero()
draw_zero()
reposition_zero()
draw_one()
reposition_one()
draw_zero()
reposition_zero()

#finish
turn_around()
move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def draw_one(): #robot will draw a number one
    put()
    move()
    put()
    move()
    put()
    move()
    put()
    move()
    put()
    
def reposition_one():    
    turn_around()
    move()
    move()
    move()
    move()
    turn_left()
    move()
    move()
    turn_left()
    
def draw_zero(): #robot will draw a number zero
    draw_one()
    turn_right()
    move()
    put()
    move()
    turn_right()
    draw_one()
    turn_right()
    move()
    put()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_around():
    turn_left()
    turn_left()

def reposition_zero():
    turn_around()
    move()
    move()
    move()
    turn_left()
    
