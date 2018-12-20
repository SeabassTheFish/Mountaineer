import json
from Animation import *
from Utilities import *

class Popup: # This came out really well
    def __init__(self, paramsFile, player, canvasWidth, canvasHeight):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.readSaveFile(paramsFile) # I'll have different files for different popup windows throughout the game
        self.characterDisplay = Animation(str(player.attributes["gender"]) + "-LU", 2, 10)
        self.player = player
        self.activePanel = "" # WIP
            
    def readSaveFile(self, filename): # Like in other files
        file = open(filename, "r")
        saveData = " ".join(file.readlines())
        self.params = json.loads(saveData)
        file.close()
            
    def main(self): # Shows up in the middle of the screen. Occupied when trading or looking at a map, otherwise not there
        # Types of Main Panels:
        # Trading (t), Map (m)
        
        mainKey = self.params["main"].split(" ")
        
        if self.activePanel == "main":
            stroke(230)
            strokeWeight(7)
            fill(0, 0, 0, 200)
        else:
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
        rect(self.canvasWidth/5, self.canvasHeight/15, self.canvasWidth*3/5, self.canvasHeight*3/5, self.canvasWidth/20)
        
        if mainKey[0] == "t":
            pass
        elif mainKey[0] == "m":
            pass
    
    def inventory(self): # On the right side of the screen, shows items
        # Types of Inventory Panels:
        # Standard (s)
        
        inventoryKey = self.params["inventory"].split(" ")
        
        if self.activePanel == "inventory":
            stroke(230)
            strokeWeight(7)
            fill(0, 0, 0, 200)
        else:
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            
        rect(self.canvasWidth - self.canvasWidth/6, 0, self.canvasWidth/6, self.canvasHeight, self.canvasWidth/20)
        
        if inventoryKey[0] == "s":
            pass
            
    def character(self): # On the left side of the screen, shows character stats and levels
        
        characterKey = self.params["character"].split(" ")
        
        if self.activePanel == "character":
            stroke(230)
            strokeWeight(7)
            fill(0, 0, 0, 200)
        else:
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            
        rect(0, 0, self.canvasWidth/6, self.canvasHeight, self.canvasWidth/20)
        
        if characterKey != "":
            self.characterDisplay.display(self.canvasWidth/9, self.canvasHeight/5, self.canvasWidth/10, self.canvasHeight/5)
            fill(255)
            textFont(makeFont(30))
            textAlign(CENTER)
            text("Health:" + str(self.player.attributes["health"]) + "\nXP:" + str(self.player.attributes["xp"]) + "\nArmor:" + str(self.player.attributes["armor"]) + "\nLevel:" + str(self.player.attributes["level"]), self.canvasWidth/30, self.canvasHeight/7)
            self.writeSubcat(self.canvasWidth/30, self.canvasHeight/2, 50, 500, self.player.attributes["magic"], "Magic")
            self.writeSubcat(self.canvasWidth/30, self.canvasHeight/2 + 20*(len(self.player.attributes["magic"]) + 1), 50, 500, self.player.attributes["physical"], "Physical")
            self.writeSubcat(self.canvasWidth/30, self.canvasHeight/2 + 20*(len(self.player.attributes["magic"]) + 1) + 20*(len(self.player.attributes["physical"]) + 1), 50, 500, self.player.attributes["mental"], "Mental")
    
    def writeSubcat(self, x, y, w, h, ref, refName): # For displaying experience in different fields (think Skyrim)
        textAlign(LEFT)
        text(refName, x, y)
        deltaY = 20
        thingy = deltaY
        for i in ref:
            text(str(i) + ":" + str(ref[str(i)]), x + 40, y + thingy)
            thingy += deltaY
    
    def readout(self): # The readout panel would appear at the bottom of the screen, beneath the main but not encroaching on inventory or character.
        # Types of Readout Panels:
        # Dialogue (d), Monologue (m)
        
        readoutKey = self.params["readout"].split(" ")
        
        if self.activePanel == "readout":
            stroke(230)
            strokeWeight(7)
            fill(0, 0, 0, 200)
        else:
            fill(0, 0, 0, 150)
            stroke(200)
            strokeWeight(5)
            
        rect(self.canvasWidth/6, self.canvasHeight*2/3, self.canvasWidth*2/3, self.canvasHeight/3, self.canvasWidth/20)
        
        if readoutKey != "":
            pass
            
    def run(self): # Putting it all together
        self.main()
        self.inventory()
        self.character()
        self.readout()
        # I may add more panels eventually
            
