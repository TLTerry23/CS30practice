#Pon Step 11
#November 14, 2019
#Robot will walk to each corner, take() flowers, and return home.

        
think (5)

repeat 23:
    if 
        
#repeat 23:
    #if not front_is_clear():
        
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