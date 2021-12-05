#diese Variablen werden für das Wechseln zwischen den Screens verwendet
current_screen = 0
old_screen = 0
#aus dem Zusatzdokument werden die vordefinierten "Bausteine" importiert
from zusatz import chord
from zusatz import button 
from zusatz import screen_tonart
from zusatz import screen_cdur
from zusatz import screen_gdur
from zusatz import screen_fdur

#die verschiedenen Funktionen für die Screens werden in eine Liste gepackt
screens = [screen_tonart, screen_cdur, screen_gdur, screen_fdur]
#die allgemeingueltigen Einstellungen werden festgelegt
def setup(): 
     size (900,500)
     background(255,255,255) 
    
#die drawfunktion wird einmal pro frame ausgefuehrt
def draw():
    #die globalen Variablen muessen zuerst geladen werden
    global current_screen, old_screen
    #der Startbildschirm wird geladen
    screens[current_screen](0,0)
    #dieser macht den Screen jeweils wieder weiss, sobald der Screen gewechselt wird, damit sich nicht mehrere Screens 
    #ueberlagern (und laden jeweils einmalig das Notensystem)
    if old_screen != current_screen:
        background(255,255,255)
        image(loadImage("notenlinien.png"), 0, 101, 1048,160)    
    old_screen = current_screen
    #Programmieren der Buttons, damit sie die Tonarten laden
    if current_screen == 0 and mouseX >= 410 and mouseX <= 410 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           current_screen = 1
    if current_screen == 0 and mouseX >= 510 and mouseX <= 510 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           current_screen = 2
    if current_screen == 0 and mouseX >= 310 and mouseX <= 310 + 80 and mouseY >= 300 and mouseY <= 300 + 80 and mousePressed == True:
           current_screen = 3
    #HomeButton
    if 800<mouseX<880 and 0<mouseY<80 and mousePressed == True:
           current_screen = 0
    
