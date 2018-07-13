yCoordinate = random (50, 200)
XCoordinate = random (50, 200)
ySpeed=5
xSpeed=2
ellipseSize= 40





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
    paddleBoundary = brickBoundary + 555


    
    if yCoordinate >= bottomBoundary or yCoordinate <= topBoundary:
        ySpeed = -ySpeed
        
    if XCoordinate >= rightBoundary or XCoordinate <= leftBoundary:
        xSpeed = -xSpeed
      
    if yCoordinate <= brickBoundary and XCoordinate >= brickBoundary:

        ySpeed = -ySpeed
    if xCoordinate <= 
   # if yCoordinate >= brickBoundary and XCoordinate >= brickBoundary:
      # ySpeed = -ySpeed         

    if mouseX and mouseY:
       fill(0)
       rect(mouseX, 580, 40, 20) 
    XCoordinate += xSpeed
    yCoordinate += ySpeed
    fill (255, 0, 255)
    ellipse(XCoordinate, yCoordinate, ellipseSize, ellipseSize)

    fill(0, 191, 255)
    rect(0, 0, 90, 25)   # blue brick
    
    fill(255, 128, 0)
    rect(90, 0, 90, 25)  # soft orange bick
    
    fill(255, 69, 0)
    rect(180, 0, 90, 25) # red orange brick
    
    fill(128, 0, 128)
    rect(270, 0, 90, 25 )# purple brick
    
    fill(255, 255, 0)
    rect(360, 0, 90, 25) # yellow brick
    
    fill(220, 220, 220)
    rect(450, 0, 90, 25) # blue lavender brick
    
    fill(0, 255, 0)
    rect(540, 0, 90, 25) # green brick


    
