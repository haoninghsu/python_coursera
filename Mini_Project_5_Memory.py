# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck, exposed, state, Card1, Card2, Turn
    state = 0
    Card1 = -1
    Card2 = -1
    Turn = 0
    deck = [ x for x in range(8)]*2
    random.shuffle(deck)
    exposed = [False]*16
     
# define event handlers
def mouseclick(pos):
    global state, Turn, Card1, Card2    
    index = pos[0]//50
    
    # Zero Card Open
    if state == 0:
        if exposed[index] == False:
            # Mark this position as exposed, so that "draw" reveals the number
            exposed[index] = True
            # Remember the index of the first exposed card
            Card1 = index
            # Move the state to 1, to prepare for next state
            state = 1
        
    # One Card Open      
    elif state == 1:
        if exposed[index] == False:
            # Mark this position as exposed, so that "draw" reveals the number
            exposed[index] = True
            # Remember the index of the second exposed card
            Card2 = index
            # Move state to 2, prepare for the next state
            state = 2
            Turn += 1

    else:
        # If card1 and card2 are different
        if deck[Card1] != deck[Card2]:
            # Mark exposed of those two as False, so draw knows to do its work and color them
            exposed[Card1], exposed[Card2] = False, False
            # Reset the two positions of the cards
            Card1 = -1
            Card2 = -1
            label.set_text("Turns = " + str(Turn))
        else:
            exposed[Card1], exposed[Card2] = True, True
        # No matter the cards are the same or different, you wanna draw one card
        if exposed[index] == False:
            exposed[index] = True
            Card1 = index
            state = 1
                        
# cards are logically 50x100 pixels in size

# "draw" scans for the exposed array repeatedly to see if it needs to do work
# Hence, you manipulate the exposed array to let "draw" know when it should work
def draw(canvas):
    for i in range(16):
        if exposed[i]:
            canvas.draw_polygon(([i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]),1,"Black","White")
            canvas.draw_text(str(deck[i]),[i*50+11,70],60,"Black")
        else:
            # print "B"
            canvas.draw_polygon(([i*50,0],[(i+1)*50,0],[(i+1)*50,100],[i*50,100]),1,"Black","Green")
        label.set_text("Turn = " + str(Turn))

new_game()
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = "+ str(Turn))

# get things rolling

frame.start()


# Always remember to review the grading rubric
# Pelase use CodeSculptor to run the program: http://www.codeskulptor.org
