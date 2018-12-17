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
    println(get(mouseX, mouseY))
    doActions(globals)
    
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
                globals.action = "initVillage"
        if globals.level == 1:
            if globals.popup == "":
                if keyCode == 38 or keyCode == 37 or keyCode == 39 or keyCode == 40:
                    globals.player.move(keyCode)
                    if globals.pressTime <= 2:
                        globals.player.updateImage()
                            
    globals.pressTime += 1
                
def keyReleased():
    globals.player.attributes["state"] = "still"
    doActions(globals)
    globals.player.updateImage()
    globals.previousKey = keyCode
    globals.pressTime = 0

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
            globals.village.run(globals.modeTime, globals.screen, globals.popup)
            limCoords(globals.player, 0, width, 0, height)
    globals.modeTime += 1
