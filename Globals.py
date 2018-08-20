from Animation import *
from Button import *
from Menu import *
from Player import *
from Customize import *
from Levels import *
from Village import *
from ArrowChoiceBar import *

class Globals:
    def __init__(self, canvasWidth, canvasHeight):
        self.mode = "menu"
        self.player = Player()
        self.menu = Menu(canvasWidth, canvasHeight)
        self.customize = Customize(canvasWidth, canvasHeight, self.player)
        self.action = ""
        self.level = self.player.attributes["level"]
        self.village = Village(canvasWidth, canvasHeight)
        self.modeTime = 0
        self.testArrows = ArrowChoiceBar(canvasWidth*2/3, canvasHeight*2/3, canvasWidth/6, canvasHeight/6, True, False, False, False)
