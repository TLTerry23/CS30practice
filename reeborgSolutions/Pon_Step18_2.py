#Pon Step 18
#November 20, 2019
#Robot will use while, if, elif, and else to complete the race
#Robot will move to north_west() corner to begin
#Robot will sweep_1() south, sense and take() all carrots,
#sense for wall

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
#head south, sense and take() carrots   
    while front_is_clear():
        while object_here():
            take()
        move()
    while object_here(): #robot needs additional detection arghh
        take()    
    
#detecting East wall (end of south pass)
    turn_left()#determines if sweep_1 continues North
    if front_is_clear():#no wall, go North
        move()
        turn_left()
    else:#finds wall, begin sweep_finish()
        turn_left()
        sweep_finish()
        
#head north, sense and take() carrots        
    while front_is_clear(): #North sweep
        while object_here():
            take()
        move()
        while object_here():#robot needs additional detection arghh
            take()
            
#detecting East wall (end of north pass)           
    if right_is_clear(): #no wall, loop sweep_1() again
        turn_right()
        move()
        turn_right()
        sweep_1() 
    else:#finds wall, begin sweep_finish()
        sweep_finish()

def sweep_finish():
    while front_is_clear(): #begins sweep IF at SE corner
        while object_here():
            take()
        move()
    while carries_object():#drops carrots
        put()
    turn_around()#turn south
    while front_is_clear():#go to SE corner
        move()
    turn_right()#turn west
    while front_is_clear():#go to SW corner and goal
        move()
    done() #at_goal
    
think (0)
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