add_library('video')
from Animation import *
from Button import *
from Menu import *
from Player import *
from Customize import *
from Levels import *
import processing.video

class Globals:
    def __init__(self, canvasWidth, canvasHeight):
        self.mode = "customize"
        self.player = Player()
        self.menu = Menu(canvasWidth, canvasHeight)
        self.customize = Customize(canvasWidth, canvasHeight, self.player)
        self.action = ""
        self.level = self.player.attributes["level"]
        self.levelRunner = Levels()
