def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    if wall_in_front():
        jump()
    else:
        turn_right()
        while not wall_in_front():
            move()
        turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
# hurdle 4 code
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not is_facing_north():
    turn_left()
turn_right()
while not at_goal():
    if wall_in_front():
        turn_left()
    else:
        move()
    if not wall_on_right():
        turn_right()

# maze code 
