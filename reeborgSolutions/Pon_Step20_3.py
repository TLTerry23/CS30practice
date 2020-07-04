#Pon Step 20
#November 19, 2019
#Robot will use while, if, elif, and else to complete
#a lap, locate window openings and build_wall().
def turn_right():
    repeat 3:
        turn_left()

def turn_around():
    turn_left()
    turn_left()



def navigate():
    while not at_goal():
        if right_is_clear(): #sensing an opening on the right
            move() #taking an extra step differentiates
                   #window squares from move()able squares
                
            if not wall_on_right():#move()able square, continue hugging wall               
                turn_around()#next 5 steps returns robot to the wall
                move()
                turn_left()
                move()
                #navigate()

            else:#window square
                turn_around()#next 6 steps build the wall
                move()
                turn_left()
                build_wall()
                turn_left()
                move()
                
        elif not wall_in_front():#no gap in wall, move()
            move()


        else: #robot in corner, turn_left()
            turn_left()
            move()
            navigate()
think (100)

repeat 3: #position robot to starting point
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