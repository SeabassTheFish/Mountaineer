# Mountaineer
from Globals import *
from Utilities import *

def setup():
    fullScreen()
    noSmooth()
    global globals
    globals = Globals(width, height)
    globals.player.readSaveFile("saveData.txt")
    
def mousePressed():
    if globals.mode == "menu":
        globals.action = checkButtons(globals.menu.menuButtons, pmouseX, pmouseY)
        
        # Actions
        if globals.action == "customize":
            globals.mode = "customize"
            globals.modeTime = 0
        elif globals.action == "play":
            globals.mode = "play"
            globals.modeTime = 0

    elif globals.mode == "customize":
        globals.action = checkButtons(globals.customize.customizeButtons, pmouseX, pmouseY)
        
        # Actions
        if globals.action == "menu":
            globals.mode = "menu"
            globals.modeTime = 0
            globals.player.readSaveFile(globals.player.saveFilename)
        elif globals.action == "toLad":
            globals.player.attributes["gender"] = "m"
        elif globals.action == "toLass":
            globals.player.attributes["gender"] = "f"
        elif globals.action == "saveCustomize":
            globals.player.writeSaveFile()
            globals.mode = "menu"
            globals.modeTime = 0

        if globals.customize.namePlate.xyOver(mouseX, mouseY):
            globals.customize.namePlate.state = "edit"
        
            
    globals.action = ""
    
def keyPressed():
    if globals.mode == "customize":
        if keyCode == 10:
            globals.player.attributes["name"] = globals.customize.namePlate.txt
            globals.customize.namePlate.state = "fixed"
        if keyCode == 8:
            globals.customize.namePlate.txt = globals.customize.namePlate.txt[:-1]
        elif globals.customize.namePlate.state == "edit" and keyCode >= 32 and keyCode <= 126:
            globals.customize.namePlate.txt = globals.customize.namePlate.txt + str(key)
    elif globals.mode == "play":
        if globals.level == 0:
            if keyCode == 38:
                globals.level = 1
                globals.modeTime = 0
        if globals.level == 1:
            if keyCode == 38 or keyCode == 37 or keyCode == 39 or keyCode == 40:
                globals.player.move(keyCode)
                if keyCode != globals.previousKey:
                    globals.player.updateImage()
                
def keyReleased():
    globals.player.attributes["state"] = "still"
    globals.player.updateImage()
    globals.previousKey = keyCode

def draw():
    background(255, 255, 255)
    if globals.mode == "menu":
        globals.menu.run()
    if globals.mode == "customize":
        globals.customize.run(globals.modeTime)
    if globals.mode == "play":
        if globals.level == 0:
            globals.village.leadUp(globals.modeTime)
        elif globals.level == 1:
            globals.village.run(globals.modeTime)
    globals.modeTime += 1