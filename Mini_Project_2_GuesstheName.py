# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0,100)
    global count
    count = 0
    global limit
    limit = 7
    global is100
    is100 = True
    global is1000
    is1000 = False
#    secret_number = random.randrange(0,100)
#    return int(secret_number)



# define event handlers for control panel
def range100():
    new_game()
    
    global is100
    is100 = True
    return int(secret_number)


def range1000():
    new_game()
    global secret_number
    secret_number = random.randrange(0,1000)
    
    global limit
    limit = 10
    global is100
    is100 = False
    global is1000
    is1000 = True
    
    return int(secret_number)    

    
def input_guess(guess):
    global the_guess
    #global secret_number
    the_guess = int(guess)
    global count
    global limit
    count += 1
    
    if count == limit and is100 and the_guess != secret_number:
        print("Exceeded guess limits, game restarting")
        range100()
       
    elif count == limit and is1000 and the_guess != secret_number:
        print("Exceeded guess limits, game restarting")
        range1000()
    
    else:

        print "Guess was "+ guess
        print "Number of remaining guesses is "+ str(limit-count)
        if the_guess > secret_number:
            print "Lower!"
        elif the_guess < secret_number:
            print "Higher!"
        elif the_guess == secret_number:
            print "Correct!"
            if is100:
                range100()
            elif is1000:
                range1000()
        else:
            print "Please enter a valid number"

# create frame
frame=simplegui.create_frame("input guess",200, 200)

# register event handlers for control elements and start frame
frame.add_input("Guess the number",input_guess, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)

# call new_game 
new_game()



# always remember to check your completed program against the grading rubric
# Please use CodeSculptor to run the program: http://www.codeskulptor.org
