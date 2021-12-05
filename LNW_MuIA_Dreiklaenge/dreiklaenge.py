a = 110
b = 300 

#Versuch Screenauswahl
    #def screen(screenauswahl):
    #if screen == 1:
    #    screen_cdur(0,0)
    #else: 
    #    screen_tonart(0,0)
        
def screen_tonart(xPos, yPos):
    image(loadImage("notenlinien.png"), 0, 101, 1048,160)
    button(310, 300, "F") 
    button(410, 300, "C") 
    button(510, 300, "G")
    
 #button Tonart C --> ebenfalls WIP
  #  if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
   #         screen(1)

def screen_cdur(xPos, yPos):
       image(loadImage("notenlinien.png"), 0, 101, 1048,160)

       chord(550, 162, 0)
       chord(650, 143, 0)
       chord(750, 134, 0)
       button(110, 300, "I")
       button(210, 300, "II") 
       button(310, 300, "III") 
       button(410, 300, "IV") 
       button(510, 300, "V") 
       button(610, 300, "VI") 
       button(710, 300, "VII") 
    
    #Button Tonart C Stufe I
       if mouseX >= a and mouseX <= a + 80 and mouseY >= b and mouseY <= b + 80 and mousePressed == True:
           fill(255, 0, 0)
           chord(150, 198, 1)
           text("C", 145, 120)
        
       else:
           noFill() 
           button (110, 300, "I") 
        
    #Button Tonart C Stufe II 
       if mouseX >= 210 and mouseX <= 210 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           fill(255, 0, 0)
           chord(250, 189, 0)
        
       else:
           noFill() 
           button (210, 300, "II") 
    
    #Button Tonart C Stufe III 
       if mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           fill(255, 0, 0)
           chord(350, 180, 0)
        
       else:
           noFill() 
           button(310, 300, "III") 
    #Button Tonart C Stufe IV
       if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            fill(255, 0, 0)
            chord(450, 171, 0)
       else: 
            noFill ()
            button(410, 300, "IV")
       
    
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
