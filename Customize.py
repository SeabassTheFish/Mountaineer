from Animation import *
from Button import *
from Player import *
from TextBox import *

class Customize:
    def __init__(self, canvasWidth, canvasHeight, player):
        self.mountain = Animation("Mountain", 2, 15)
        self.lad = Animation("Lad-LU", 2, 10)
        self.lass = Animation("Lass-RU", 2, 10)
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.player = player
        self.customizeButtons = [Button(canvasWidth*9/20, canvasHeight*6/7, canvasWidth/10, canvasHeight/10, "Save\nChanges", "saveCustomize"), Button(canvasWidth*4/5, canvasHeight/3, canvasWidth/10, canvasHeight/5, "", "toLad"), Button(canvasWidth/10, canvasHeight/3, canvasWidth/10, canvasHeight/5, "", "toLass"), Button(canvasWidth/100, canvasHeight/100, canvasWidth/25, canvasHeight/25, "Back", "menu")]
        self.namePlate = TextBox(self.canvasWidth*2/5, self.canvasHeight*3/4, self.canvasWidth/5, self.canvasHeight/30, self.player.attributes["name"])
        
    def run(self, modeTime):
        self.mountain.display(self.canvasWidth/2, self.canvasHeight/2, self.canvasWidth, self.canvasHeight)
        fill(255, 0, 0)
        if self.player.attributes["gender"] == "m":
            stroke(255)
            strokeWeight(4)
        self.customizeButtons[1].run()
        stroke(0)
        strokeWeight(1)
        fill(0, 0, 255)
        if self.player.attributes["gender"] == "f":
            stroke(255)
            strokeWeight(4)
        self.customizeButtons[2].run()
        stroke(0)
        strokeWeight(1)
        self.lad.display(self.canvasWidth*4/5 + self.canvasWidth/20, self.canvasHeight/3 + self.canvasHeight/10, self.canvasWidth/10, self.canvasHeight/5)
        self.lass.display(self.canvasWidth/10 + self.canvasWidth/20, self.canvasHeight/3 + self.canvasHeight/10, self.canvasWidth/10, self.canvasHeight/5)
        fill(255)
        self.customizeButtons[0].run()
        fill(255)
        self.customizeButtons[3].run()
        self.namePlate.display(modeTime)
        
