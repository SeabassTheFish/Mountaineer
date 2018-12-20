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

class Globals: # The master variable object. Globals are bad, so I just put all the global things I would need into one global
    def __init__(self, canvasWidth, canvasHeight):
        self.mode = "play"
        self.screen = ""
        self.player = Player(canvasWidth, canvasHeight)
        self.menu = Menu(canvasWidth, canvasHeight)
        self.customize = Customize(canvasWidth, canvasHeight, self.player)
        self.action = ""
        self.level = 0
        self.village = Village(canvasWidth, canvasHeight, self.player)
        self.village.board = Board(canvasWidth, canvasHeight, "Village", 2, 2, 1)
        self.modeTime = 0
        self.previousKey = 0
        self.pressTime = 0
        self.popup = ""
