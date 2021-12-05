a = 110
b = 300 

from dreiklaenge import chord
from dreiklaenge import button 
def setup(): 
     size (1100,500)
     background(255,255,255) 
    

def draw(): 
    image(loadImage("notenlinien.png"), 0, 101, 1048,160)

    chord(450, 171, 0)
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
    
    #Button1 
    if mouseX >= a and mouseX <= a + 80 and mouseY >= b and mouseY <= b + 80 and mousePressed == True:
        fill(255, 0, 0)
        chord(150, 198, 1)
        
    else:
        noFill() 
        button (110, 300, "I") 
        
    #Button2 
    if mouseX >= 210 and mouseX <= 210 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
        fill(255, 0, 0)
        chord(250, 189, 0)
        
    else:
        noFill() 
        button (210, 300, "I") 
    
    #Button3 
    if mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
        fill(255, 0, 0)
        chord(350, 180, 0)
        
    else:
        noFill() 
        button(310, 300, "I") 
         
