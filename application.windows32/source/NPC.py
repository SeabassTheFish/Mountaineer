import json
from Utilities import *
from Animation import *

class NPC: # Non-player characters. People to interact with in-game that are run by the computer
    def __init__(self, name):
        self.name = name # For display purposes and for finding the right save file
        self.savefilename = str(self.name) + "SaveFile.txt" # Saves general things like location, trades, and possessions
        self.defaultfile = "npcDefaultSave.txt" # In case the save file gets lost
        try:
            self.readSaveFile(self.savefilename)
        except:
            self.readSaveFile(self.defaultfile)
        self.displayImage = Animation(str(self.name) + "-" + "no-still", 1, 1) # "no-still" stands for  facing north, view overhead, standing still. I need that image generator
        self.moveLeft = 0 # How much is left in the move, not how much to move in the leftwards direction
        self.nextMove = round(random(300)) # To make it look like they're doing something important
        
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
        
    def updateImage(self): # Like the player
        if self.attributes["state"] == "still":
            self.displayImage = Animation(self.name + "-" + self.attributes["facing"] + self.attributes["view"] + "-still", 1, 1)
        elif self.attributes["state"] == "mov":
            self.displayImage = Animation(self.name + "-" + self.attributes["facing"] + self.attributes["view"] + "-mov", 4, 10)
                
    # TODO: Make this more modular
    
    def run(self):
        self.display()
        self.nextPixel = self.findNextPxl() # For finding boundries
        if self.nextMove <= 0:
            self.setMovePoint()
            self.nextMove = round(random(300))
        if self.moveLeft <= 0:
            self.attributes["state"] = "still"
            self.updateImage()
            self.nextMove -= 1
        if self.moveLeft > 0:
            self.move()
            if self.nextPixel == intToRGB(-3815995): # For running into a boundry. Not yet modular
                if self.attributes["facing"] == "n":
                    self.attributes["y"] += self.attributes["speed"] + 1
                if self.attributes["facing"] == "s":
                    self.attributes["y"] -= self.attributes["speed"] + 1
                if self.attributes["facing"] == "e":
                    self.attributes["x"] -= self.attributes["speed"] + 1
                if self.attributes["facing"] == "w":
                    self.attributes["x"] += self.attributes["speed"] + 1
                self.moveLeft = 0
            # TODO: Make this work with any color
        
    def display(self):
        self.displayImage.display(self.attributes["x"], self.attributes["y"], self.attributes["w"], self.attributes["h"])
        
    def move(self): # For moving based on direction faced
        self.attributes["state"] = "mov"
        self.nextPixel = self.findNextPxl()
        self.pastX = self.attributes["x"]
        self.pastY = self.attributes["y"]
        if self.attributes["view"] == "o":
            if self.attributes["facing"] == "n":
                self.attributes["y"] -= self.attributes["speed"]
            if self.attributes["facing"] == "s":
                self.attributes["y"] += self.attributes["speed"]
            if self.attributes["facing"] == "e":
                self.attributes["x"] += self.attributes["speed"]
            if self.attributes["facing"] == "w":
                self.attributes["x"] -= self.attributes["speed"]
        self.moveLeft -= self.attributes["speed"]
                    
    def setMovePoint(self): # Deciding which direction to go
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
        
    def findNextPxl(self): # For finding color
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
