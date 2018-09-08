import json
from Animation import *

class Player:
    def __init__(self):
        self.saveFilename = "saveData.txt"
        self.defaultsFilename = "defaultSave.txt"
        self.displayImage = ""
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
        if keycode == 37:
            self.attributes["facing"] = "w"
            self.attributes["x"] -= 5
        if keycode == 38:
            self.attributes["facing"] = "n"
            self.attributes["y"] -= 5
        if keycode == 39:
            self.attributes["facing"] = "e"
            self.attributes["x"] += 5
        if keycode == 40:
            self.attributes["facing"] = "s"
            self.attributes["y"] += 5
            
    def findNextPxl(self):
        if self.attributes["facing"] == "n":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"]/3)
            return color(nextPxl >> 16 & 255, nextPxl >> 8 & 255, nextPxl >> 0 & 255)
        if self.attributes["facing"] == "s":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/2, self.attributes["y"]*2/3)
            return color(nextPxl >> 16 & 255, nextPxl >> 8 & 255, nextPxl >> 0 & 255)
        if self.attributes["facing"] == "w":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]/3, self.attributes["y"]/2)
            return color(nextPxl >> 16 & 255, nextPxl >> 8 & 255, nextPxl >> 0 & 255)
        if self.attributes["facing"] == "e":
            nextPxl = get(self.attributes["x"] + self.attributes["w"]*2/3, self.attributes["y"]/2)
            return color(nextPxl >> 16 & 255, nextPxl >> 8 & 255, nextPxl >> 0 & 255)
            
        
