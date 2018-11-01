import random 
import time


x = 0
y = 0

def setup():
    size(640, 480)

def draw():
    global x
    global y
    
    #Placement of crosshair
    smooth()
    background(255)
    fill(255, 0, 0)
    ellipse(320, 240, 30, 30)
    
    #targets
    noStroke()
    fill(0, 255, 0)
    cursor(CROSS)
    
    #target 1
    fill(x) 
    rect(100, 100, 30, 30)
    
    '''
    if mousePressed and mouseX >= 100 and mouseX <= 130 and mouseY >= 100 and mouseY <= 130:
        fill(255) 
        rect(100, 100, 30, 30)
    '''
        
    print(mouseX, mouseY)

def mouseClicked():
    global x
    x = 250
    fill(x)
    rect(100, 100, 30, 30)
    if x == 250:
        x = 0

    
