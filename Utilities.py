def makeFont(fontSize):
    return createFont("zx_spectrum-7.ttf", fontSize)

def checkButtons(buttonList, x, y):
    for btn in buttonList:
        if btn.xyOver(x, y):
            btn.showClicked()
            return btn.actionTo
    return ""

def checkPlates(plateList, entity):
    for plate in plateList:
        if plate.run():
            return plate.action
    return ""

def intToRGB(input):
    return color(input >> 16 & 255, input >> 8 & 255, input & 255, input >> 24 & 255)

def limCoords(entity, xmin, xmax, ymin, ymax):
    if entity.attributes["x"] < xmin:
        entity.attributes["x"] = xmin
    if entity.attributes["y"] < ymin:
        entity.attributes["y"] = ymin
    if entity.attributes["x"] > xmax:
        entity.attributes["x"] = xmax
    if entity.attributes["y"] > ymax:
        entity.attributes["y"] = ymax
        
def doActions(dataSet):
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
            pass
        elif dataSet.level == 1:
            dataSet.action = checkPlates(dataSet.village.villagePlates, dataSet.player)
            if dataSet.action == "apothe":
                dataSet.mode = "apothecary"
                dataSet.modeTime = 0
            elif dataSet.action == "yeet":
                println("YEET")
        
            
    dataSet.action = ""
