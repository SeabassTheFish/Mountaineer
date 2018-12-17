from Animation import *
from Readout import *
from ArrowChoiceBar import *
from Board import *
from NPC import *
from TriggerPlate import *
from Popup import *

class Village:
    def __init__(self, canvasWidth, canvasHeight, player):
        self.pic = Animation("Village Entrance", 2, 15)
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.font = createFont("zx_spectrum-7.ttf", 96)
        self.player = player
        self.testBox = Readout(0, canvasHeight*4/5, canvasWidth, canvasHeight/5, "Ayup...It's Harvest Time.")
        self.enterArrows = ArrowChoiceBar(canvasWidth*19/20, canvasHeight*19/20, canvasWidth/5, canvasHeight/5, True, False, False, False)
        self.board = Board(canvasWidth, canvasHeight, "Village", 2, 2, 1)
        self.pharmacist = NPC("cody")
        self.apothePlate = TriggerPlate(canvasWidth*4/5 - canvasWidth/50, canvasHeight*2/5, canvasWidth/20, canvasHeight/20, "apothe", self.player)
        self.talkToApothePlate = TriggerPlate(self.canvasWidth/2 - self.canvasWidth/40, self.canvasHeight/2 + self.canvasHeight/10, self.canvasWidth/20, self.canvasHeight/20, "talkToApothe", self.player)
        self.villagePlates = [self.apothePlate, self.talkToApothePlate]
        self.apothePopup = Popup("apotheTrade.txt", player, canvasWidth, canvasHeight)
        
    def leadUp(self, modeTime):
        self.pic.display(self.canvasWidth/2, self.canvasHeight/2, self.canvasWidth, self.canvasHeight)
        if modeTime < 256:
            fill(0, 355 - 2*modeTime)
            rect(0, 0, self.canvasWidth, self.canvasHeight)
            fill(255, 255 - 2*modeTime)
            stroke(0, 255 - 2*modeTime)
            textFont(self.font)
            textAlign(CENTER)
            text("The Village", self.canvasWidth/2, self.canvasHeight/2)
            fill(0, 255 - 2*modeTime)
        self.enterArrows.display()
        self.player.attributes["view"] = "o"
        self.player.attributes["facing"] = "n"
        self.player.attributes["x"] = self.canvasWidth/2
        self.player.attributes["y"] = self.canvasHeight*7/8
        self.player.attributes["w"] = self.canvasWidth/10
        self.player.attributes["h"] = self.canvasHeight/10
        self.player.attributes["state"] = "still"
        
    def run(self, modeTime, screen, popup):
        self.board.run()
        if screen == "village":
            if modeTime < 3:
                self.board = Board(self.canvasWidth, self.canvasHeight, "Village", 2, 2, 1)
        if screen == "apothecary":
            if modeTime < 3:
                self.player.attributes["x"] = self.canvasWidth/2
                self.player.attributes["y"] = self.canvasHeight*4/5
                self.player.attributes["w"] = self.canvasWidth/5
                self.player.attributes["h"] = self.canvasHeight/5
                self.player.attributes["speed"] = 10
                self.pharmacist.attributes["x"] = self.canvasWidth/2
                self.pharmacist.attributes["y"] = self.canvasHeight*3/8
                self.pharmacist.attributes["w"] = self.canvasWidth/5
                self.pharmacist.attributes["h"] = self.canvasHeight/5
                self.pharmacist.attributes["speed"] = 10
                self.pharmacist.attributes["facing"] = "s"
                self.pharmacist.updateImage()
                self.board = Board(self.canvasWidth, self.canvasHeight, "Apothecary", 1, 1, 0)
            fill(255)
            noStroke()
            rect(self.canvasWidth/2 - self.canvasWidth/40, self.canvasHeight/2 + self.canvasHeight/10, self.canvasWidth/20, self.canvasHeight/20, 5)
            self.pharmacist.run()
        self.player.run()
        if popup == "talkToApothe":
                self.apothePopup.run()
