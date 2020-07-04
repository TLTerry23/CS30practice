#Pon Step 13
#November 14, 2019
#Robot detect and jump_hurdles() until goal.
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
def jump_hurdles():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

think (100)

while not at_goal():
    if front_is_clear():
        move()
    else:
        jump_hurdles()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

def move2():
    repeat 2 :
        move()
    

def think_move():
    repeat 11 :
        if object_here():
            take()
        move()
        
def back_flag():
    turn_around()
    repeat 12 :
        move()
    drop_all()
    

def turn_around():
    turn_left()
    turn_left()    

def drop_all():
    repeat 9 :
        if carries_object():
            put()