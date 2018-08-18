from Animation import *

class Village:
    def __init__(self, canvasWidth, canvasHeight):
        self.pic = Animation("Village Entrance", 2, 15)
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.font = createFont("zx_spectrum-7.ttf", 96)
    def run(self, modeTime):
        self.pic.display(0, 0, self.canvasWidth, self.canvasHeight)
        if modeTime < 256:
            fill(0, 355 - 2*modeTime)
            rect(0, 0, self.canvasWidth, self.canvasHeight)
            fill(255, 255 - 2*modeTime)
            textFont(self.font)
            textAlign(CENTER)
            text("The Village", self.canvasWidth/2, self.canvasHeight/2)
