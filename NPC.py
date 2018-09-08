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
                self.displayImage = Animation(self.attributes["name"] + "-" + self.attributes["facing"] + "o-still", 1, 1) 
            elif self.attributes["state"] == "mov":
                self.displayImage = Animation(self.attributes["name"] + "-" + self.attributes["facing"] + "o-mov", 4, 10)
                
    def run(self):
        self.displayImage.display(self.attributes["x"], self.attributes["y"], self.attributes["w"], self.attributes["h"])
        self.nextPixel = self.findNextPxl()
        
    def move(self, keycode):
        self.attributes["state"] = "mov"
        self.nextPixel = self.findNextPxl()
        self.pastX = self.attributes["x"]
        self.pastY = self.attributes["y"]
        if self.nextPixel == color(0, 0, 0):
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
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"] + self.attributes["h"]/3)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"] + self.attributes["h"]/3, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "s":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"] + self.attributes["h"]*2/3)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"] + self.attributes["h"]*2/3, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "w":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/3, self.attributes["y"] + self.attributes["h"]/2)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] + self.attributes["w"]/3, self.attributes["y"] + self.attributes["h"]/2, 10, 10)
            return intToRGB(nextPxl)
        if self.attributes["facing"] == "e":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]*2/3, self.attributes["y"] + self.attributes["h"]/2)
            fill(255, 0, 0)
            #ellipse(self.attributes["x"] + self.attributes["w"]*2/3, self.attributes["y"] + self.attributes["h"]/2, 10, 10)
            return intToRGB(nextPxl)
