x = 0
y = 310
z = 100
a = 65
b = 55
c = 95
d = 115
e = 550
f = 0

def setup():
    size(640, 480)
    frameRate(80)

def draw():
    global x
    global y
    global z
    global a
    global b
    global c
    global d
    global e
    global f
    
    background(44, 5, 84)
    noStroke()
    
    if x == 1:
        background(139, 0, 0)
        
    #moon
    fill(255, 255,255)
    ellipse(e, 150, 250, 250)
    
    #moon glow
    fill(255, 255, 255, 50)
    ellipse(e, 150, 270, 270)   
    
    
    if x == 1:
        e -= 1
        if e <= 100:
            e = 0

    fill(255, 140, 0)
    ellipse(e, 150, 250, 250)
    fill(255, 255, 255, 50)
    ellipse(e, 150, 270, 270)
    
    #Crosses
    
    fill(105, 105, 105)
    rect(240, 250, 20, 175)
    rect(200, 280, 100, 20)
    
    fill(0, 0, 0, 200)
    rect(100, 230, 20, 175)
    rect(60, 260, 100, 20)
    
    fill(175, 175, 175, 250)
    rect(140, 240, 20, 175)
    rect(100, 290, 100, 20)
    
    fill(255, 255, 255, 300)
    rect(180, 280, 20, 175)
    rect(140, 320, 100, 20)
    
    #rip sign
    fill(100, 100, 100)
    rect(10, 300, 80, 100)
    ellipse(50, 300, 80, 80)
    fill(255, 255, 255)
    textSize(20)
    text("R.I.P", 28, 300)
    
    #pumpkin
    ellipse(120, 380, 80, 60)
    fill(255, 165, 0)
    triangle(95, 370, 110, 370, 95, 360)
    triangle(120, 370, 140, 370, 140, 360)
    arc(115, 380, 40, 40, 0, PI, CHORD)
    fill(0, 0, 0)
    triangle(125, 380, 130, 380, 127, 385)
    triangle(100, 380, 105, 380, 103, 385)
    rect(115, 340, 10, 20)
    
    
    if x == 1:
        z += 8
        
    if z >= 640:
        z = 0
        
    if x == 1:
        a += 8
    if a >= 640:
        a = 0
    
    if x == 1:
        b += 8
    if b >= 640:
        b = 0
        
    if x == 1:
        c += 8
    if c >= 640:
        c = 0
        
    if x == 1:
        d += 8
    if d >= 640:
        d = 0
    
    #ghost glow
    fill(250, 250, 250, 30)
    ellipse(z, 100, 90, 90)
    rect(b, 110, 90, 40)
    
    #ghost
    fill(255, 255, 255)
    ellipse(z, 100, 70, 70)
    rect(a, 100, 70, 50)
    fill(0, 0, 0)
    ellipse(c, 100, 10, 30)
    ellipse(d, 100, 10, 30)
    fill(44, 5, 84)
    
    #landscape
    fill(0 ,0 ,0)
    ellipse(550, 400, 500, 300)
    rect(0, 400, 640, 200)
    
    #big pumpkin
    
    if f == 0:
        y = 310
    y += 1
    
    fill(191, 97, 0)
    triangle(360, 320, 400, 370, 450, 320)
    triangle(600, 320, 600, 340, 500, 320)
    fill(0, 0, 0)
    rect(0, 400, 640, 200)
    fill(0, 0, 0)
    rect(360, y, 400, 80)
    
    if y == 400:
        y = 400
    
def mousePressed():
    global x
    global f
    x += 1
    f += 1
    if x == 2 and f == 2:
        x = 0
        f = 0
