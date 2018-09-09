import json
from Utilities import *
from Animation import *

class NPC:
    def __init__(self, name):
        self.name = name
        self.savefilename = str(self.name) + "SaveFile.txt"
        self.defaultfile = "npcDefaultSave.txt"
        try:
            self.readSaveFile(self.savefilename)
        except:
            self.readSaveFile(self.defaultfile)
        self.displayImage = Animation(str(self.name) + "-" + "no-still", 1, 1)
        self.moveLeft = 0 
        self.nextMove = round(random(300))
        
    def readSaveFile(self, filename):
        file = open(filename, "r")
        saveData = " ".join(file.readlines())
        self.attributes = json.loads(saveData)
        file.close()
            
    def writeSaveFile(self):
        newSaveFile = open(self.saveFilename, "w")
        newSaveFile.write(json.dumps(self.attributes))
        newSaveFile.close()
        self.updateImage()
        
    def updateImage(self):
        if self.attributes["view"] == "o":
            if self.attributes["state"] == "still":
                self.displayImage = Animation(self.name + "-" + self.attributes["facing"] + "o-still", 1, 1)
            elif self.attributes["state"] == "mov":
                self.displayImage = Animation(self.name + "-" + self.attributes["facing"] + "o-mov", 4, 10)
                
    def run(self):
        self.display()
        self.nextPixel = self.findNextPxl()
        if self.nextMove <= 0:
            self.setMovePoint()
            self.nextMove = round(random(300))
        if self.moveLeft <= 0:
            self.attributes["state"] = "still"
            self.updateImage()
            self.nextMove -= 1
        if self.moveLeft > 0:
            self.move()
            if self.nextPixel == intToRGB(-1973791):
                if self.attributes["facing"] == "n":
                    self.attributes["y"] += self.attributes["speed"] + 1
                if self.attributes["facing"] == "s":
                    self.attributes["y"] -= self.attributes["speed"] + 1
                if self.attributes["facing"] == "e":
                    self.attributes["x"] -= self.attributes["speed"] + 1
                if self.attributes["facing"] == "w":
                    self.attributes["x"] += self.attributes["speed"] + 1
        
    def display(self):
        self.displayImage.display(self.attributes["x"], self.attributes["y"], self.attributes["w"], self.attributes["h"])
        
    def move(self):
        self.attributes["state"] = "mov"
        self.nextPixel = self.findNextPxl()
        self.pastX = self.attributes["x"]
        self.pastY = self.attributes["y"]
        if self.attributes["facing"] == "n":
            self.attributes["y"] -= self.attributes["speed"]
        if self.attributes["facing"] == "s":
            self.attributes["y"] += self.attributes["speed"]
        if self.attributes["facing"] == "e":
            self.attributes["x"] += self.attributes["speed"]
        if self.attributes["facing"] == "w":
            self.attributes["x"] -= self.attributes["speed"]
        self.moveLeft -= self.attributes["speed"]
                    
    def setMovePoint(self):
        orientation = floor(random(3.99))
        if orientation == 0:
            self.attributes["facing"] = "n"
        if orientation == 1:
            self.attributes["facing"] = "s"
        if orientation == 2:
            self.attributes["facing"] = "e"
        if orientation == 3:
            self.attributes["facing"] = "w"
        self.updateImage()
        self.moveLeft = random(300)
        
    def findNextPxl(self):
        if self.attributes["facing"] == "n":
            nextPxl = get(self.attributes["x"], self.attributes["y"] - 10)
            fill(255, 0, 0)
            ellipse(self.attributes["x"], self.attributes["y"] - 10, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "s":
            nextPxl = get(self.attributes["x"], self.attributes["y"] + 10)
            fill(255, 0, 0)
            ellipse(self.attributes["x"], self.attributes["y"] + 10, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "w":
            nextPxl = get(self.attributes["x"] - 10, self.attributes["y"])
            fill(255, 0, 0)
            ellipse(self.attributes["x"] - 10, self.attributes["y"], 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "e":
            nextPxl = get(self.attributes["x"] + 10, self.attributes["y"])
            fill(255, 0, 0)
            ellipse(self.attributes["x"] + 10, self.attributes["y"], 10, 10)
            return intToRGB(nextPxl)
