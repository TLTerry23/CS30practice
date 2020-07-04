#Pon Step 15
#November 19, 2019
#Robot will use while, if, elif, and else to complete the race
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()

think (50)

def navigate():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif not wall_in_front():
            move()
        else:
            turn_left()
            navigate()
navigate()
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