from Animation import *
from Readout import *
from ArrowChoiceBar import *
from Board import *

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
        
    def leadUp(self, modeTime):
        self.pic.display(0, 0, self.canvasWidth, self.canvasHeight)
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
        self.player.attributes["x"] = self.canvasWidth*4/9
        self.player.attributes["y"] = self.canvasHeight*7/8
        self.player.attributes["w"] = 200
        self.player.attributes["h"] = 200
        self.player.attributes["state"] = "still"
        
    def run(self, modeTime):
        self.board.run()
        self.player.run()
