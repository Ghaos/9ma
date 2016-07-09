#setup function
def setup():
    size(400, 400)
    background(255, 255, 255)

#variables
x=50
flg=0
y=300
v=0
value = 1

#draw function
def draw():
    
    #declare global variables
    global x
    global y
    global v
    global flg
    
    #draw a robot
    background(255, 255, 255)
    stroke(0, 0, 255)
    draw_robot(x, y)
    
    #when flg==0, move right
    if(flg == 0):
        x = x+value
    #else, move left
    else:
        x = x-value
        
    #when reach the end, turn back
    if(x >= 350):
        flg = 1
    if(x <= 50):
        flg = 0
    
    #decide y
    #defualt: y=300
    #when initial velocity v is given, add the velocity
    #velocity decreases with the gravity
    if(v > -30):
        v = v - 3
    y = min(300, y - v)

#when mouse pressed
def mousePressed():
    
    #speed up in the x direction
    global value
    value = value + 1
    
    #initial velocity in the y direction is given
    global v
    v=30

#function to draw a rectangle
def draw_rect(x, y, w, h):
    line(x-w/2, y-h/2, x-w/2, y+h/2)
    line(x-w/2, y+h/2, x+w/2, y+h/2)
    line(x+w/2, y+h/2, x+w/2, y-h/2)
    line(x-w/2, y-h/2, x+w/2, y-h/2)

#function to draw a robot
def draw_robot(x,y):
    draw_rect(x, y, 100, 80)
    draw_rect(x-25, y-70, 25, 60)
    draw_rect(x+25, y-70, 25, 60)
    ellipse(x-25, y+55, 30, 30)
    ellipse(x+25, y+55, 30, 30)