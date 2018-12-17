from Animation import *
from Button import *
from Menu import *
from Player import *
from Customize import *
from Levels import *
from Village import *
from ArrowChoiceBar import *
import json
from Utilities import *

class Globals:
    def __init__(self, canvasWidth, canvasHeight):
        self.mode = "play"
        self.screen = ""
        self.player = Player()
        self.menu = Menu(canvasWidth, canvasHeight)
        self.customize = Customize(canvasWidth, canvasHeight, self.player)
        self.action = ""
        self.level = 0
        self.village = Village(canvasWidth, canvasHeight, self.player)
        self.modeTime = 0
        self.previousKey = 0
        self.pressTime = 0
        self.popup = ""
