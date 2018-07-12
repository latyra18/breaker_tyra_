yCoordinate = random (50, 200)
XCoordinate = random (50, 200)
ySpeed=5
xSpeed=2
ellipseSize= 80



def setup():
    size(600, 600)
    
        
                                                  
def draw():
    background(255)
    global XCoordinate, yCoordinate, ySpeed, xSpeed, ellipseSize
    topBoundary = ellipseSize /2
    bottomBoundary = 600 - ellipseSize / 2
    brickBoundary = topBoundary + 25
    leftBoundary = ellipseSize /2
    rightBoundary = 600 - ellipseSize / 2
    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        ySpeed = -ySpeed
        
    if XCoordinate >= rightBoundary or XCoordinate <= leftBoundary:
        xSpeed = -xSpeed
      
    if yCoordinate <= brickBoundary and XCoordinate >= brickBoundary:
        ySpeed = -ySpeed  
    
    XCoordinate += xSpeed
    yCoordinate += ySpeed
    
    fill (255, 0, 255)
    ellipse(XCoordinate, yCoordinate, ellipseSize, ellipseSize)

    fill(0, 191, 255)
    rect(0, 0, 90, 25)
    
    fill(238, 203, 173)
    rect(90, 0, 90, 25)
    
    fill(255, 69, 0)
    rect(180, 0, 90, 25)
    
    fill(205, 92, 92)
    rect(270, 0, 90, 25)
    
    fill(255, 255, 0)
    rect(360, 0, 90, 25)
    
    fill(220, 220, 220)
    rect(450, 0, 90, 25)
    
    fill(0, 255, 0)
    rect(540, 0, 90, 25)

def mouseDragged(): 
    rect(0,0,30,15)

    
