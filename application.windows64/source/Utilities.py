from Board import *

# This is where I keep all the important functions

def makeFont(fontSize): # Helpful
    return createFont("zx_spectrum-7.ttf", fontSize)

def checkButtons(buttonList, x, y):
    for btn in buttonList:
        if btn.xyOver(x, y):
            btn.showClicked()
            return btn.actionTo
    return ""

def checkPlates(plateList, entity): # Could eventually be consolidated with checkButtons
    for plate in plateList:
        if plate.run():
            return plate.action
    return ""

def intToRGB(input): # Converting base10 to binary to RGB, but I don't use it much because color() takes ints as well
    return color(input >> 16 & 255, input >> 8 & 255, input & 255, input >> 24 & 255)

def limCoords(entity, xmin, ymin, xmax, ymax): # Keeps the entity within the box
    if entity.attributes["x"] < xmin:
        entity.attributes["x"] = xmin
    if entity.attributes["y"] < ymin:
        entity.attributes["y"] = ymin
    if entity.attributes["x"] > xmax:
        entity.attributes["x"] = xmax
    if entity.attributes["y"] > ymax:
        entity.attributes["y"] = ymax
        
def checkOutside(entity, xmin, ymin, xmax, ymax): # Checks if the entity is outside the box (does nothing to stop it)
    if entity.attributes["x"] > xmax:
        return "r"
    if entity.attributes["x"] < xmin:
        return "l"
    if entity.attributes["y"] > ymax:
        return "d"
    if entity.attributes["y"] < ymin:
        return "u"
        
def doActions(dataSet): # All the different actions
    if dataSet.mode == "menu":
        dataSet.action = checkButtons(dataSet.menu.menuButtons, pmouseX, pmouseY)
        
        # Actions
        if dataSet.action == "customize":
            dataSet.mode = "customize"
            dataSet.modeTime = 0
        elif dataSet.action == "play":
            dataSet.mode = "play"
            dataSet.modeTime = 0

    elif dataSet.mode == "customize":
        dataSet.action = checkButtons(dataSet.customize.customizeButtons, pmouseX, pmouseY)
        
        # Actions
        if dataSet.action == "menu":
            dataSet.mode = "menu"
            dataSet.modeTime = 0
            dataSet.player.readSaveFile(dataSet.player.saveFilename)
        elif dataSet.action == "toLad":
            dataSet.player.attributes["gender"] = "m"
        elif dataSet.action == "toLass":
            dataSet.player.attributes["gender"] = "f"
        elif dataSet.action == "saveCustomize":
            dataSet.player.writeSaveFile()
            dataSet.mode = "menu"
            dataSet.modeTime = 0

        if dataSet.customize.namePlate.xyOver(mouseX, mouseY):
            dataSet.customize.namePlate.state = "edit"
            
    elif dataSet.mode == "play":
        
        if dataSet.level == 0:
            if dataSet.action == "initVillage":
                dataSet.level = 1
                dataSet.screen = "village"
                dataSet.modeTime = 0
        elif dataSet.level == 1:
            dataSet.action = checkPlates(dataSet.village.villagePlates, dataSet.player)
            if dataSet.action == "apothe":
                dataSet.screen = "apothecary"
                dataSet.modeTime = 0
            elif dataSet.action == "talkToApothe":
                dataSet.popup = "talkToApothe"
            elif dataSet.action == "yeet": # For debugging
                println("YEET")
            elif dataSet.action == "village-2":
                dataSet.screen = "village"
                dataSet.village.board = Board(dataSet.village.canvasWidth, dataSet.village.canvasHeight, "Village", 2, 2, 1)
                dataSet.modeTime = 0
                dataSet.player.attributes["view"] = "o"
                dataSet.player.attributes["facing"] = "s"
                dataSet.player.attributes["x"] = dataSet.village.canvasWidth*4/5
                dataSet.player.attributes["y"] = dataSet.village.canvasHeight/2
                dataSet.player.attributes["w"] = dataSet.village.canvasWidth/10
                dataSet.player.attributes["h"] = dataSet.village.canvasHeight/10
                dataSet.player.attributes["state"] = "still"
                dataSet.player.attributes["speed"] = 5
         
        if dataSet.action == "inventory":
            dataSet.popup = "inventory"       
                
    if dataSet.action != "":
        println(dataSet.action) # For debugging
    dataSet.action = "" # Getting ready for the next go-around
