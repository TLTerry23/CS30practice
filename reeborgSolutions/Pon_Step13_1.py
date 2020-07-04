#Pon Step 13.1
#November 18, 2019
#Robot will use if, elif, and else to complete the race
def turn_right():
    repeat 3:
        turn_left()

def jump_hurdles():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

think (5)

repeat 46:
    if at_goal():
        done()
    elif wall_in_front():
        jump_hurdles()
    else:
        move()
    
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