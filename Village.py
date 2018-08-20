from Animation import *
from Readout import *

class Village:
    def __init__(self, canvasWidth, canvasHeight):
        self.pic = Animation("Village Entrance", 2, 15)
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.font = createFont("zx_spectrum-7.ttf", 96)
        self.testBox = Readout(0, canvasHeight*4/5, canvasWidth, canvasHeight/5, "Ayup...It's Harvest Time.")
        
    def run(self, modeTime):
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
