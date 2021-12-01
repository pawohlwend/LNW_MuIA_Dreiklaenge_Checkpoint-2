def chord(xPos, yPos):
    noFill()
    strokeWeight(2)
    ellipse(xPos, yPos, 20, 18)
    ellipse(xPos, yPos + 18, 20, 18)
    ellipse(xPos, yPos + 36, 20, 18)
    
def chord2(xPos, yPos): 
    noFill()
    strokeWeight(2)
    ellipse(xPos, yPos, 20, 18)
    ellipse(xPos, yPos + 18, 20, 18)
    ellipse(xPos, yPos + 36, 20, 18)
    line(xPos-12, yPos + 36, xPos + 12, yPos + 36)

def button(xPos, yPos): 
    noFill()
    strokeWeight(2)
    rect(xPos, yPos, 80, 80) 
    textSize(20) 
    text("button", xPos + 10, yPos + 40) 
    fill(255, 0, 0) 
