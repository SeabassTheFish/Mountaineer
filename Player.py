import json
from Animation import *
from Utilities import *

class Player:
    def __init__(self):
        self.saveFilename = "saveData.txt"
        self.defaultsFilename = "defaultSave.txt"
        self.displayImage = ""
        self.pastX = 0
        self.pastY = 0
        try:
            self.readSaveFile(self.saveFilename)
        except:
            self.readSaveFile(self.defaultsFilename)
        self.updateImage()
            
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
                self.displayImage = Animation(str(self.attributes["gender"]) + "-" + self.attributes["facing"] + "o-still", 1, 1) 
            elif self.attributes["state"] == "mov":
                self.displayImage = Animation(str(self.attributes["gender"]) + "-" + self.attributes["facing"] + "o-mov", 4, 10)
                    
    def run(self):
        self.displayImage.display(self.attributes["x"], self.attributes["y"], self.attributes["w"], self.attributes["h"])
        
    def move(self, keycode):
        self.attributes["state"] = "mov"
        self.nextPixel = self.findNextPxl()
        self.pastX = self.attributes["x"]
        self.pastY = self.attributes["y"]
        if self.nextPixel != color(0, 0, 0):
            if keycode == 37:
                self.attributes["facing"] = "w"
                self.attributes["x"] -= self.attributes["speed"]
            if keycode == 38:
                self.attributes["facing"] = "n"
                self.attributes["y"] -= self.attributes["speed"]
            if keycode == 39:
                self.attributes["facing"] = "e"
                self.attributes["x"] += self.attributes["speed"]
            if keycode == 40:
                self.attributes["facing"] = "s"
                self.attributes["y"] += self.attributes["speed"]
        if self.nextPixel == color(0, 0, 0) or self.nextPixel == color(-1973791):
            if self.attributes["facing"] == "n":
                self.attributes["y"] += self.attributes["speed"] + 1
            if self.attributes["facing"] == "s":
                self.attributes["y"] -= self.attributes["speed"] + 1
            if self.attributes["facing"] == "e":
                self.attributes["x"] -= self.attributes["speed"] + 1
            if self.attributes["facing"] == "w":
                self.attributes["x"] += self.attributes["speed"] + 1
            
    def findNextPxl(self):
        if self.attributes["facing"] == "n":
            nextPxl = get(self.attributes["x"], self.attributes["y"] - 10)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"], self.attributes["y"] - 10, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "s":
            nextPxl = get(self.attributes["x"], self.attributes["y"] + 10)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"], self.attributes["y"] + 10, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "w":
            nextPxl = get(self.attributes["x"] - 10, self.attributes["y"])
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] - 10, self.attributes["y"], 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "e":
            nextPxl = get(self.attributes["x"] + 10, self.attributes["y"])
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] + 10, self.attributes["y"], 10, 10)
            return intToRGB(nextPxl)
