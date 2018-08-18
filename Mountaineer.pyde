# Mountaineer
from Globals import *
from Utilities import *

def setup():
    fullScreen()
    noSmooth()
    global globals
    globals = Globals(width, height)
    
def mousePressed():
    if globals.mode == "menu":
        globals.action = checkButtons(globals.menu.menuButtons, pmouseX, pmouseY)
        
        # Actions
        if globals.action == "customize":
            globals.mode = "customize"

    elif globals.mode == "customize":
        globals.action = checkButtons(globals.customize.customizeButtons, pmouseX, pmouseY)
        
        # Actions
        if globals.action == "menu":
            globals.mode = "menu"
            globals.player.readSaveFile(globals.player.saveFilename)
        elif globals.action == "toLad":
            globals.player.attributes["gender"] = "m"
        elif globals.action == "toLass":
            globals.player.attributes["gender"] = "f"
        elif globals.action == "saveCustomize":
            globals.player.writeSaveFile()
            globals.mode = "menu"

        if globals.customize.namePlate.xyOver(mouseX, mouseY):
            globals.customize.namePlate.state = "edit"
        
            
    globals.action = ""
    
def keyReleased():
    if globals.mode == "customize":
        if keyCode == 10:
            globals.player.attributes["name"] = globals.customize.namePlate.txt
            globals.customize.namePlate.state = "fixed"
        if keyCode == 8:
            globals.customize.namePlate.txt = globals.customize.namePlate.txt[:-1]
        elif globals.customize.namePlate.state == "edit" and keyCode >= 32 and keyCode <= 126:
            globals.customize.namePlate.txt = globals.customize.namePlate.txt + str(key)

def draw():
    background(255, 255, 255)
    if globals.mode == "menu":
        globals.menu.run()
    if globals.mode == "customize":
        globals.customize.run()
    if globals.mode == "game":
        if globals.level == 0:
            pass
