#Pon Step 16
#November 19, 2019
#Robot will use while, if, elif, and else to clear the field
#of carrots. The navigate() function will be used 3 times.

def turn_right():#robot turns right
    repeat 3:
        turn_left()

def turn_around():#robot turns around
    turn_left()
    turn_left()


def navigate():
    repeat 8:#moves from S to N and picks along the way
        move()
        if object_here():
            take()
            
    turn_right()#next 3 lines reposition 
    move()
    turn_right()
    
    repeat 8:#moves from N to S and picks along the way
        move()
        if object_here():
            take()
            
    turn_left()#next 3 lines reposition 
    move()
    turn_left()
            
            
think (50)

repeat 2:#next 3 lines position robot to begin
    move()
turn_left()

repeat 3:# three passes of the function clears the field
    navigate()
    
while carries_object(): #drop all carrots
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