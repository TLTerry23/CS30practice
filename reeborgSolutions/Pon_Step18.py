#Pon Step 18
#November 20, 2019
#Robot will use while, if, elif, and else to complete the race
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()


def north_west(): #relocates robot to northwest corner
    while not is_facing_north():
        turn_left()
    while not wall_in_front():
        move()
    turn_left()
    while not wall_in_front() and wall_on_right():
        move()
    turn_left()
    
def sweep_1():#robot will head south, turn head north
    while front_is_clear():
        while object_here():
            take()
        move()
    turn_left()
    if front_is_clear():
        move()
        turn_left()
    else:
        sweep_finish()
    while front_is_clear():
        while object_here():
            take()
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        sweep_1()
    else:
        sweep_finish()

def sweep_finish():
    while front_is_clear():
        while object_here():
            take()
        move()
    while carries_object():
        put()
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
north_west()

sweep_1()
   
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