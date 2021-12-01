def chord(xPos, yPos, hilfslinie):
    noFill()
    strokeWeight(2)
    ellipse(xPos, yPos, 20, 18)
    ellipse(xPos, yPos + 18, 20, 18)
    ellipse(xPos, yPos + 36, 20, 18)
    if hilfslinie == 1:
      line(xPos-12, yPos + 36, xPos + 12, yPos + 36)
        

#def chord2(xPos, yPos): 
 #   noFill()
  #  strokeWeight(2)
   # ellipse(xPos, yPos, 20, 18)
    #ellipse(xPos, yPos + 18, 20, 18)
    #ellipse(xPos, yPos + 36, 20, 18)
  

def button(xPos, yPos, Titel): 
    noFill()
    strokeWeight(2)
    rect(xPos, yPos, 80, 80) 
    textSize(20) 
    text(Titel, xPos + 10, yPos + 40) 
    fill(255, 0, 0) 
