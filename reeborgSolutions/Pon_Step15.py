#Pon Step 15
#November 24, 2019

#Robot will do a lap, look for windows, build_wall()s if 
#necessary, and finish at the goal.

def turn_right():
    repeat 3:
        turn_left()

def close_window():
    turn_right()
    build_wall()
    turn_left()
    

think (0)       
move()
turn_right()
move()
while not at_goal():
    if right_is_clear():
        close_window()
    elif front_is_clear():
        move()
    else:
        turn_left()      
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