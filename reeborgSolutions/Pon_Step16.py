#Pon Step 16
#November 19, 2019
#Robot will use while, if, elif, and else to complete the race
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()


def navigate():
    repeat 8:
        move()
        if object_here():
            take()
    turn_right()
    move()
    turn_right()
    repeat 8:
        move()
        if object_here():
            take()
    turn_left()
    move()
    turn_left()
            
            
think (50)
repeat 2:
    move()
turn_left()

repeat 3:
    navigate()
while carries_object():
    put()

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