#Pon Step 19
#November 19, 2019
#Robot will use while, if, elif, and else to complete lap of
#lake. Starting point is a fruit.
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()



def navigate(): #robot follows right side of lake until finish
    while not object_here():#program ends at fruit
        if right_is_clear():#sensing right wall
            turn_right()
            move()
        elif front_is_clear():#sensing front wall
            move()
        else: #last choice turn_left()
            turn_left()

            
            
think (50)
put()#drop fruit as starting point
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