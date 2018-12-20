# Mountaineer
from Globals import *
from Utilities import *

def setup():
    fullScreen()
    
    # Keeps images from going blurry
    noSmooth()
    
    # Where I store everything accessed by draw()
    global globals
    globals = Globals(width, height)
    
    # Part of the init for the player
    globals.player.readSaveFile("saveData.txt")
    
def mousePressed():
    println(get(mouseX, mouseY))
    
    # See Utilities tab, I put all the actions in there. When something needs to change, I make it an action
    doActions(globals)
    
def keyPressed():
    # I seperate them into modes first
    if globals.mode == "customize":
        if keyCode == 10: # Enter
            globals.player.attributes["name"] = globals.customize.namePlate.txt
            globals.customize.namePlate.state = "fixed"
        if keyCode == 8: # Delete
            globals.customize.namePlate.txt = globals.customize.namePlate.txt[:-1]
        elif globals.customize.namePlate.state == "edit" and keyCode >= 32 and keyCode <= 126: # Any character
            globals.customize.namePlate.txt = globals.customize.namePlate.txt + str(key)
    
    elif globals.mode == "play":
        # This is the lead-up to the Village level
        if globals.level == 0:
            if keyCode == 38:
                globals.action = "initVillage"
        if globals.level == 1: # The village itself
            if globals.popup == "": # Keeps the player from moving while the inventory is open
                if keyCode == 38 or keyCode == 37 or keyCode == 39 or keyCode == 40: # Up down left right that sort of thing
                    globals.player.move(keyCode)
                    if globals.pressTime <= 2:
                        globals.player.updateImage() # So the player shows whether it's moving or still
                        
        if keyCode == 69: # E
            globals.popup = "inventory"
                        
    if globals.popup != "": # This is for plates where it activates when the player is on it. If they player just closed a menu, it won't open again
        if keyCode == 81:
            globals.popup = ""
                            
    globals.pressTime += 1 # Just tracking, only use it occasionally
                
def keyReleased():
    println(str(globals.player.attributes["x"]) + " " + str(width) + " " + str(globals.player.attributes["y"]) + " " + str(height))
    
    if keyCode == 38 or keyCode == 37 or keyCode == 39 or keyCode == 40:
        globals.player.attributes["state"] = "still"
    
    if keyCode != 81:
        doActions(globals) # See above
    
    # Housekeeping
    globals.player.updateImage()
    
    globals.previousKey = keyCode # Not sure if I've used this anywhere yet
    globals.pressTime = 0

def draw():
    background(255, 255, 255) # So it doesn't show previous frames

    # Seperated by mode
    if globals.mode == "menu":
        globals.menu.run()
    if globals.mode == "customize":
        globals.customize.run(globals.modeTime)
    if globals.mode == "play":
        # Seperated by level
        if globals.level == 0:
            globals.village.leadUp(globals.modeTime)
        elif globals.level == 1:
            globals.village.run(globals.modeTime, globals.screen, globals.popup)
        
        # Checking whether player is onscreen
        if checkOutside(globals.player, 0, 0, width, height) == "l":
            globals.action = "charLeft"
        if checkOutside(globals.player, 0, 0, width, height) == "r":
            globals.action = "charRight"
        if checkOutside(globals.player, 0, 0, width, height) == "d":
            globals.action = "charDown"
        if checkOutside(globals.player, 0, 0, width, height) == "u":
            globals.action == "charUp"

        # Popups
        if globals.popup == "inventory":
            globals.player.inventoryPopup.run()
    
    # For tracking, very useful
    globals.modeTime += 1
