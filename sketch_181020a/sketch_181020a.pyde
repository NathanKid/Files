import random

def setup():
    size(640, 480)
    frameRate(60)
    
x = 0
y = 0
z = 0
bird_size = random.randint(10, 32)
bird_height = random.randint(50, 200)

def draw():
    global x
    global y
    global z
    
    if x >= 640:
        x = 0
    x += 3
    
    if y >= 640:
        y = 0
    y += 5
    
    if z >= 640:
        z  = 0
    z += 8
    
    background(175, 12, 12)
    noStroke()        

    fill(0, 0 , 0, 75)
    rect(0, 0, 640, 75)
    
    fill(0, 0, 0, 50)
    rect(0, 75, 640, 100)
    
    fill(0, 0, 0, 25)
    rect(0, 175, 640, 75)

    #bird/text
    
    for b in range(0, 15):
        fill(0, 0, 0)
        textSize(bird_size)
        text('V', x, bird_height)

    #clouds
    fill(0, 0, 0)
    ellipse(z + 30, 40, 50, 50)
    ellipse(z + 50, 40, 50, 50)
    ellipse(z + 70, 40, 50, 50)
    ellipse(z + 10, 40 + 20, 50, 50)
    ellipse(z + 30, 40 + 20, 50, 50)
    ellipse(z + 50, 40 + 20, 50, 50)
    ellipse(z + 70, 40 + 20, 50, 50)
    ellipse(z + 90, 40 + 20, 50, 50)
    
    ellipse(y, 150, 60, 60)
    ellipse(y + 30, 150, 60, 60)
    ellipse(y + 50, 150, 60, 60)
    ellipse(y + 30, 150 - 20, 60, 60)
    
    ellipse(x, height/2, 50, 50)
    ellipse(x+30, height/2, 50, 50)
    ellipse(x+10, height/2-20, 50, 50)
    
    #sun
    fill(255, 255, 0)
    stroke(150, 6, 6, 200)
    strokeWeight(5)
    ellipse(320, 320, 100, 100)
    
    noStroke()
    
    #flare around the sun
    fill(255, 255, 0, 50)
    ellipse(320, 320, 150, 150)
    
    #ground
    fill(0, 0, 0)
    rect(0, 350, 640, 200)
    
    #mountians
    fill(8, 8, 8)
    triangle(25, 450, 150, 175, 420, 450) 
    
    fill(5, 5, 5)
    triangle(100, 400, 200, 260, 250, 400)
    
    fill(5, 5, 5)
    triangle(150, 440, 280, 300, 340, 440)
    
    fill(0, 0, 0)
    triangle(30, 100, -100, 480, 250, 480)
    
    #mountains to the right
    fill(0, 0, 0)
    triangle(510, 380, 550, 300, 580, 380)
    
    fill(0, 0, 0)
    triangle(540, 480, 630, 200, 700, 480)
    
    #stream
    fill(10, 10, 10)
    rect(450, 350, 20, 200)  
    
    #trees
    fill(10, 10, 10)
    rect(300, 435, 10, 38)
    triangle(290, 445, 320, 445, 305, 420)
    triangle(285, 455, 325, 455, 305, 430)
    
    rect(420, 425, 10, 30)
    triangle(410, 435, 440, 435, 425, 415)
    triangle(405, 445, 445, 445, 425, 425)
    
    rect(530, 400, 10, 20)
    triangle(520, 410, 550, 410, 535, 385)
    triangle(405, 445, 445, 445, 425, 425)
