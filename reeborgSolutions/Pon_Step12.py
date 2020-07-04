#Pon Step 12
#November 14, 2019
#Robot will move(), to take() apples, move() and put() apples, then
#move to goal.
def turn_right():
    repeat 3:
        turn_left()
def turn_around():
    repeat 2:
        turn_left()
        
think (5)
turn_left()
repeat 2:
    move()
turn_right()
move()
while object_here():
    take()
turn_right()
repeat 3:
    move()
turn_left()
repeat 4:
    move()
turn_left()
repeat 4:
    move()
while carries_object():
    put()
turn_around()
repeat 4:
    move()
turn_right()
repeat 5:
    move()
turn_left()
repeat 2:
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