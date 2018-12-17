import json
from Animation import *

class Popup:
    def __init__(self, paramsFile, player, canvasWidth, canvasHeight):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.readSaveFile(paramsFile)
        self.characterDisplay = Animation(str(player.attributes["gender"]) + "-LU", 2, 10)
            
    def readSaveFile(self, filename):
        file = open(filename, "r")
        saveData = " ".join(file.readlines())
        self.params = json.loads(saveData)
        file.close()
            
    def main(self):
        # Types of Main Panels:
        # Trading (t), Map (m)
        
        mainKey = self.params["main"].split(" ")
        
        if mainKey[0] == "t":
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            rect(self.canvasWidth/5, self.canvasHeight/15, self.canvasWidth*3/5, self.canvasHeight*3/5, self.canvasWidth/20)
        elif mainKey[0] == "m":
            pass
    
    def inventory(self):
        # Types of Inventory Panels:
        # Standard (s)
        
        inventoryKey = self.params["inventory"].split(" ")
        
        if inventoryKey[0] == "s":
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            rect(self.canvasWidth - self.canvasWidth/6, 0, self.canvasWidth/6, self.canvasHeight, self.canvasWidth/20)
            
    def character(self):
        
        characterKey = self.params["character"].split(" ")
        
        if characterKey != "":
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            rect(0, 0, self.canvasWidth/6, self.canvasHeight, self.canvasWidth/20)
            self.characterDisplay.display(self.canvasWidth/10, self.canvasHeight/5, self.canvasWidth/10, self.canvasHeight/5)
                    
    def readout(self):
        # Types of Readout Panels:
        # Dialogue (d), Monologue (m)
        
        readoutKey = self.params["readout"].split(" ")
        
        if readoutKey != "":
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            rect(self.canvasWidth/6, self.canvasHeight*2/3, self.canvasWidth*2/3, self.canvasHeight/3, self.canvasWidth/20)
            
    def run(self):
        self.main()
        self.inventory()
        self.character()
        self.readout()
            
