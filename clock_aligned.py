# Copy and Paste this code in http://www.codeskulptor.org/
import simplegui, math

sec_angle = 270		# seconds Hand points @ 12
min_angle = 270		# minutes Hand points @ 12
hour_angle = 270	# hours Hand points @ 12

r = 85		# Length of the second hand
s = 75		# Length of the minute hand
h = 55		# Length of the hour hand
# Tick Styles
tickLen = 10  # short tick
medTickLen = 20  # at 5-minute intervals
longTickLen = 30 # at the quarters

# This two line code gives the co-ordinates of the outer point
# The co-ordinates change such that, the point revolves around the centre
x = r * math.sin(math.radians(sec_angle))
y = r * math.sin(math.radians(90 - sec_angle))

# Similar code for the minute hand
xmin = s * math.sin(math.radians(min_angle))
ymin = s * math.sin(math.radians(90 - min_angle))

# Similar code for the hour hand
xhour = h * math.sin(math.radians(hour_angle))
yhour = h * math.sin(math.radians(90 - hour_angle))


time = 0
flag = True # If flag is True, timer is stopped and Lap and Split will not work
count = 0	# Counter for lap or split times

# Uses global variable time, returns in format H:MM:SS.m
def format():
    global time
    h = str(int(time / 36000))
    m = str(int((time % 36000)/600))
    if (int(m) < 10):
        m = '0' + m
    ss = str(int((time % 600)/10))
    if (int(ss) < 10):
        ss = '0' + ss
    mi = str(int(time % 10))    
    return h+":"+m+":"+ss+"."+mi

def draw_handler(canvas):
    global tickLen, medTickLen, longTickLen
    # Draws second hand
    canvas.draw_line((150, 150), (y + 150, x + 150), 2, 'Green')
    # Draws minute hand
    canvas.draw_line((150, 150), (ymin + 150, xmin + 150), 4, 'Green')
    # Draws hour hand
    canvas.draw_line((150, 150), (yhour + 150, xhour + 150), 6, 'Green')
    # Draws timer border
    canvas.draw_circle((150, 150), 100, 5, 'Green')
    # Draws the center (pin) of the timer
    canvas.draw_circle((150, 150), 4, 3, 'Black', 'Green')
    # Draws the MM:SS.m
    canvas.draw_text(format(), (125, 275), 20, 'Green') 
    
    # Draws ticks
    # canvas.draw_line((startX, startY), (endX, endY), LineWidth, LineColor)
    for i in range(0, 60):
        len = tickLen        
        if ( i % 5 == 0 ):
            # Medium ticks on the '5's (every 5 ticks)
            len = medTickLen
        if ( i % 15 == 0 ):
            # Longest tick on quarters (every 15 ticks)
            len = longTickLen

        fi = float(i)	# tick num as float for easier math

        # Get the angle from 12 O'Clock to this tick (radians)
        angleFrom12 = fi/60.0*2.0*math.pi

        # Get the angle from 3 O'Clock to this tick
        # Note: 3 O'Clock corresponds with zero angle in unit circle
        # Makes it easier to do the math.
        angleFrom3 = math.pi/2.0-angleFrom12

        canvas.draw_line((150+math.cos(angleFrom3)*100,150-math.sin(angleFrom3)*100), (150+math.cos(angleFrom3)*(100-len),150-math.sin(angleFrom3)*(100-len)), 3, 'Green')
        
        
    
    
# Gives value of the co-ordinates of the points of the needle
# to respective global variables    
def pos():
    global x, y, xmin, ymin, xhour, yhour
    x = r * math.sin(math.radians(sec_angle))    
    y = r * math.sin(math.radians(90 - sec_angle))
    xmin = s * math.sin(math.radians(min_angle))
    ymin = s * math.sin(math.radians(90 - min_angle))
    xhour = h * math.sin(math.radians(hour_angle))
    yhour = h * math.sin(math.radians(90 - hour_angle))
    
# Time handler    
def tick():
    global sec_angle, min_angle, hour_angle, time
    checkAlignment()
    if (int(time / 36000) == 6):
       stop()
       exit
    time += 1
    sec_angle += 0.6#2*(math.pi)/10    
    min_angle += 0.01#2*(math.pi)/60    
    hour_angle += (0.01/12)#2*(math.pi)/3600    
    if (sec_angle > 360.00):
        sec_angle -= 360
    if (min_angle > 360.00):
        min_angle -= 360
    if (hour_angle > 360.00):
        hour_angle -= 360    
    pos()
  
# Starts the timer    
def start():
    global flag    
    timer.start()
    flag = False
    
# Stops the timer    
def stop():
    global flag, sec_angle, min_angle, hour_angle
    timer.stop()
    sa = round(sec_angle)
    ma = round(min_angle)
    ha = round(hour_angle)
    #frame.add_label("s:m:h=" + str(sa) + ":" + str(ma) + ":" + str(ha))
    flag = True

# Resets the timer, hands go back to initial positions
def reset():
    global time, sec_angle, min_angle, hour_angle, x, y , xmin, ymin, xhour, yhour, flag, count
    timer.stop()
    time = 0
    sec_angle = 270
    min_angle = 270
    hour_angle = 270
    x = r * math.sin(math.radians(sec_angle))
    y = r * math.sin(math.radians(90 - sec_angle))
    xmin = s * math.sin(math.radians(min_angle))
    ymin = s * math.sin(math.radians(90 - min_angle))
    xhour = h * math.sin(math.radians(hour_angle))
    yhour = h * math.sin(math.radians(90 - hour_angle))
    flag = True
    count = 0
    
# When pressed, shows the lap number and lap time    
def lap():
    global count
    if (flag == False):
        count += 1
        frame.add_label(str(count) + ". " + format())
        
# When pressed, shows the split number and split time, also resets the timer        
def split():
    global count, flag
    temp = count
    if (flag == False):
        temp += 1
        frame.add_label(str(temp) + ". " + format())
        reset()
        count = temp # Does not reset count to 0
        flag = False
        timer.start()
        
# Clears the lap times and split times by reset everything
# and creating a new frame
def clear():
    reset()
    init()

# Checking if all 3 hands are in one streight line    
def checkAlignment():  
    global sec_angle, min_angle, hour_angle
    sa = round(sec_angle)
    ma = round(min_angle)
    ha = round(hour_angle)
    if ((sa == ma or sa + 180 == ma or sa - 180 == ma)and(sa == ha or sa + 180 == ha or sa - 180 == ha)):        
            lap()                        
            
timer = simplegui.create_timer(1, tick)

# Function to create frame, function has been used for re-usability
# Especially for 'Clear' button
def init():
    global frame
    frame = simplegui.create_frame('Timer', 300, 300, 100)
    frame.set_draw_handler(draw_handler)
    frame.start()

    frame.add_button('Start', start, 50)
    frame.add_button('Stop', stop, 50)
#    frame.add_button('Reset', reset, 50)
#    frame.add_button('Lap', lap, 50)
#    frame.add_button('Split', split, 50)
    frame.add_button('Clear', clear, 50)    
    
init()
