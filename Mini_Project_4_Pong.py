# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
ball_vel = [0,1]
ball_pos = [WIDTH/2, HEIGHT/2]
paddle1_pos = 150
paddle2_pos = 150
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5

# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_vel = [random.randrange(120,240)/100,random.randrange(60,180)/100]
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == False:
        ball_vel[0] *= -1
    
    # define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(0)
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, "White","White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel>0) or (paddle1_pos >= 0 and paddle1_vel<0):
        paddle1_pos += paddle1_vel
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel>0) or (paddle2_pos >= 0 and paddle2_vel<0):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos), (PAD_WIDTH, paddle1_pos), (PAD_WIDTH, paddle1_pos+PAD_HEIGHT), 
                         (0,paddle1_pos+PAD_HEIGHT)],10,"Yellow","Yellow")
    canvas.draw_polygon([(600,paddle2_pos), (WIDTH-PAD_WIDTH, paddle2_pos), 
                         (WIDTH-PAD_WIDTH, paddle2_pos+PAD_HEIGHT), (600,paddle2_pos+PAD_HEIGHT)],10,"Yellow","Yellow")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= 28 or ball_pos[0] >=572:
        ball_vel[0] = -ball_vel[0]
        
        if ball_pos[0] < WIDTH/2:
            if ball_pos[1] <= paddle1_pos or ball_pos[1] >= paddle1_pos+PAD_HEIGHT:
                score2 += 1
                spawn_ball(RIGHT)
            else:
                ball_vel[0] += 1.1*ball_vel[0]
        
        if ball_pos[0] > WIDTH/2:
            if ball_pos[1] <= paddle2_pos or ball_pos[1] >= paddle2_pos+PAD_HEIGHT:
                score1 += 1
                spawn_ball(LEFT)
            else:
                ball_vel[0] += 1.1*ball_vel[0]
            
    if ball_pos[1] >= 380 or ball_pos[1] <= 20:
        ball_vel[1] = -ball_vel[1]
        
    # draw scores
    canvas.draw_text (str(score1),(200,100), 40, 'White', 'serif')
    canvas.draw_text (str(score2),(400,100), 40, 'White', 'serif')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel

    #p1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel
    elif key == simplegui.KEY_MAP ["s"]:
        paddle1_vel = paddle_vel        
    
    #p2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
    elif key == simplegui.KEY_MAP ["down"]:
        paddle2_vel = paddle_vel  
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel

    #p1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP ["s"]:
        paddle1_vel = 0      
    
    #p2
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP ["down"]:
        paddle2_vel = 0 

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()

#Please use CodeSculptor to run this program:http://www.codeskulptor.org