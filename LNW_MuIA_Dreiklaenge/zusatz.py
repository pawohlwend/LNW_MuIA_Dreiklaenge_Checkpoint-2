#Diese Variablen werden verwendet um die Buttons zu platzieren bzw. anklickbar zu gestalten
a = 110
b = 300 

#der Tonartauswahlscreen wird definiert        
def screen_tonart(xPos, yPos):
    image(loadImage("notenlinien.png"), 0, 101, 1048,160)
    button(310, 300, "F") 
    button(410, 300, "C") 
    button(510, 300, "G")
    

#die Screens der einzelnen Tonarten werden definiert (sehr codeaufwendig, laesst sich ev. vereinfachen)
def screen_cdur(xPos, yPos):
       

       button(110, 300, "I")
       button(210, 300, "II") 
       button(310, 300, "III") 
       button(410, 300, "IV") 
       button(510, 300, "V") 
       button(610, 300, "VI") 
       button(710, 300, "VII") 
       button(800, 0, "Home")
    #Button Tonart C Stufe I
       if mouseX >= a and mouseX <= a + 80 and mouseY >= b and mouseY <= b + 80 and mousePressed == True:
           chord(150, 196, 1)
           
           fill(0, 0, 0)
           text("C", 142, 120)
        
        
    #Button Tonart C Stufe II 
       if mouseX >= 210 and mouseX <= 210 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(250, 187, 0)
           fill(0, 0, 0)
           text("Dm", 235, 120)
    
    #Button Tonart C Stufe III 
       if mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(350, 178, 0)
           
           fill(0, 0, 0)
           text("Em", 335, 120)
         
           
    #Button Tonart C Stufe IV
       if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(450, 169, 0)
            
            fill(0, 0, 0)
            text("F", 442, 120)

            
    #Button Tonart C Stufe V
       if mouseX >= 510 and mouseX <= 510 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(550, 160, 0)
            
            fill(0, 0, 0)
            text("G", 542, 120)

            
    #Button Tonart C Stufe VI
       if mouseX >= 610 and mouseX <= 610 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(650, 151, 0)
            
            fill(0, 0, 0)
            text("Am", 635, 120)

            
          #Button Tonart C Stufe VII
       if mouseX >= 710 and mouseX <= 710 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(750, 142, 0)
            
            fill(0, 0, 0)
            text("H-", 740, 120)

            
def screen_gdur(xPos, yPos):
       
       image(loadImage("sharp.png"), 85, 125, 18,30)
       button(110, 300, "I")
       button(210, 300, "II") 
       button(310, 300, "III") 
       button(410, 300, "IV") 
       button(510, 300, "V") 
       button(610, 300, "VI") 
       button(710, 300, "VII")
       button(800, 0, "Home") 
       
    #Button Tonart G Stufe 1
       if mouseX >= 110 and mouseX <= 110 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:                
            chord(150, 159, 0)
            
            fill(0, 0, 0)
            text("G", 142, 90)

        
    #Button Tonart G Stufe II 
       if mouseX >= 210 and mouseX <= 210 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(250, 150, 0)
           
           fill(0, 0, 0)
           text("Am", 235, 90)
       else: 
           button (210, 300, "II") 
    
    #Button Tonart G Stufe III 
       if mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(350, 141, 0)
        
           fill(0, 0, 0)
           text("Hm", 335, 90)

           
    #Button Tonart G Stufe IV
       if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(450, 132, 0)
            
            fill(0, 0, 0)
            text("C", 442, 90)

       
    #Button Tonart G Stufe V
       if mouseX >= 510 and mouseX <= 510 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(550, 123, 5)
            
            fill(0, 0, 0)
            text("D", 542, 90)
       else: 
            button(510, 300, "V")
    
    #Button Tonart G Stufe VI
       if mouseX >= 610 and mouseX <= 610 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(650, 114, 6)
            
            fill(0, 0, 0)
            text("Em", 635, 90)

    
        #Button Tonart G Stufe VII
       if mouseX >= 710 and mouseX <= 710 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(750, 105, 7)
            
            fill(0, 0, 0)
            text("Fis-", 730, 90)

def screen_fdur(xPos, yPos):
    
       #image(loadImage("flat.png"), 90, 159, 13,26) 
       button(110, 300, "I")
       button(210, 300, "II") 
       button(310, 300, "III") 
       button(410, 300, "IV") 
       button(510, 300, "V") 
       button(610, 300, "VI") 
       button(710, 300, "VII") 
       button(800, 0, "Home")
    #Button Tonart F Stufe I
       if mouseX >= a and mouseX <= a + 80 and mouseY >= b and mouseY <= b + 80 and mousePressed == True:
           chord(150, 168, 0)
           
           fill(0, 0, 0)
           text("F", 142, 100)
        
        
    #Button Tonart F Stufe II 
       if mouseX >= 210 and mouseX <= 210 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(250, 159, 0)
           fill(0, 0, 0)
           text("Gm", 235, 100)
    
    #Button Tonart F Stufe III 
       if mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           chord(350, 150, 0)
           
           fill(0, 0, 0)
           text("Am", 335, 100)
         
           
    #Button Tonart F Stufe IV
       if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(450, 141, 0)
            
            fill(0, 0, 0)
            text("Bb", 442, 100)

            
    #Button Tonart F Stufe V
       if mouseX >= 510 and mouseX <= 510 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(550, 132, 0)
            
            fill(0, 0, 0)
            text("C", 542, 100)

            
    #Button Tonart F Stufe VI
       if mouseX >= 610 and mouseX <= 610 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(650, 123, 5)
            
            fill(0, 0, 0)
            text("Dm", 635, 100)

            
          #Button Tonart F Stufe VII
       if mouseX >= 710 and mouseX <= 710 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
            chord(750, 114, 6)
            
            fill(0, 0, 0)
            text("E-", 740, 100)

                    
#die Definition der Chords, sprich Ellipsenpakete
#Legende Hilfslinien: 1-> 1 Hilfslinie unten, 2-> 1 Hilfslinie verschoben unten, 3 -> 2 Hilfslinien unten, 4-> 2 Hilfslinien verschoben unten
#5 -> 1 Hilfslinie oben, 6 -> 1 Hilfslinie verschoben oben, 7 -> 2 Hilfslinien oben, 8 -> 2 Hilfslinien verschoben oben
def chord(xPos, yPos, hilfslinie): 
    noFill()
    strokeWeight(2)
    ellipse(xPos, yPos, 20, 19)
    ellipse(xPos, yPos + 19, 20, 19)
    ellipse(xPos, yPos + 38, 20, 19)
    if hilfslinie == 1:
        line(xPos-12, yPos + 38, xPos + 12, yPos + 38)
    if hilfslinie == 2:
        line(xPos-12, yPos + 28.5, xPos + 12, yPos + 28.5)
    if hilfslinie == 3:
        line(xPos-12, yPos + 19, xPos + 12, yPos + 19)
        line(xPos-12, yPos + 38, xPos + 12, yPos + 38)
    if hilfslinie == 4:
        line(xPos-12, yPos + 28.5, xPos + 12, yPos + 28.5)
        line(xPos-12, yPos + 9.5, xPos + 12, yPos + 9.5)
    if hilfslinie == 5:
        line(xPos-12, yPos, xPos + 12, yPos)
    if hilfslinie == 6:
        line(xPos-12, yPos + 9.5, xPos + 12, yPos + 9.5)
    if hilfslinie == 7:
        line(xPos-12, yPos + 19, xPos + 12, yPos + 19)
        line(xPos-12, yPos, xPos + 12, yPos)
    if hilfslinie == 8:
        line(xPos-12, yPos + 9.5, xPos + 12, yPos + 9.5)
        line(xPos-12, yPos + 28.5, xPos + 12, yPos + 28.5)
        
#die Definition der Buttons
def button(xPos, yPos, Titel): 
    fill(0, 0, 0)
    strokeWeight(2)
    rect(xPos, yPos, 80, 80) 
    
    fill(255, 255, 255)
    textSize(20) 
    text(Titel, xPos + 10, yPos + 40) 
    
    #--------------------------------------------------------
    #--------------------------------------------------------
    #Verworfene Teilcodes
    #--------------------------------------------------------
    #--------------------------------------------------------
    
    #veraltete Variante fuer Chords mit Hilfslinien
#def chord2(xPos, yPos): 
 #   noFill()
  #  strokeWeight(2)
   # ellipse(xPos, yPos, 20, 18)
    #ellipse(xPos, yPos + 18, 20, 18)
    #ellipse(xPos, yPos + 36, 20, 18)
    
    
#Versuch Screenauswahl
    #def screen(screenauswahl):
    #if screen == 1:
    #    screen_cdur(0,0)
    #else: 
    #    screen_tonart(0,0)

     #button Tonart C --> ebenfalls WIP
   #  if mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
   #         screen(1)
