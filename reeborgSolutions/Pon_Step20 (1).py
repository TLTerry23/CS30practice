#Pon Step 20
#November 19, 2019
#Robot will use while, if, elif, and else to complete the race
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()

think (100)

def navigate():
    while not at_goal():
        if right_is_clear():
            move()
            if not wall_on_right():                
                turn_around()
                move()
                turn_left()
                move()
                navigate()

            else:
                turn_around()
                move()
                turn_left()
                build_wall()
                turn_left()
                move()
        elif not wall_in_front():
            move()


        else:
            turn_left()
            move()
            navigate()

repeat 3:
    move()
turn_right()
move()    
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