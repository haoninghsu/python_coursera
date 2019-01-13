# template for "Stopwatch: The Game"
import simplegui

# define global variables
time = 0
width = 200
height = 200
success = 0
count = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    second = int(time*.1)
    minute = time / 600
    second_td = int((time * .1) - (60 * minute)) // 10
    second_d = second % 10
    milisec = time % 10
    return str(minute) + ":"+ str(second_td) + str(second_d)+"."+ str(milisec)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()

def stop():
    timer.stop()
    global count
    global success
    count +=1
    if time % 10 == 0:
        success +=1
    
def reset():
    global time
    global count
    global success    
    time = 0
    count = 0
    success = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time +=1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time), [width/2-30, height/2],30,"White")
    canvas.draw_text ("Success :"+str(success)+" "+"Count :"+str(count), [100, 20], 12, "White" )

        
# create frame
frame = simplegui.create_frame("timer", width, height) 


# register event handlers
timer = simplegui.create_timer( 100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button("start", start, 200)
frame.add_button("stop", stop, 200)
frame.add_button("reset", reset, 200)

# start frame
frame.start()
timer.stop()

# Please remember to review the grading rubric
# Please use CodeSculptor to run the code: http://www.codeskulptor.org
