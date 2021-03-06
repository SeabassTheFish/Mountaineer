from Animation import *
from Button import *

class Menu: # For the menu screen when the game starts
    def __init__(self, canvasWidth, canvasHeight):
        self.mountain = Animation("Mountain", 2, 15) # Very proud with how this came out
        self.logo = loadImage("mountaineerLogo.png") # Eventally I'll replace this with something cool looking. For now, just text
        self.openerStage = 0 # Stages of the menu loading
        self.width = canvasWidth
        self.height = canvasHeight
        self.menuButtons = [Button(self.width/4, self.height*4/5, width/10, height/10, "Play", "play"), Button(self.width*3/5, self.height*4/5, width/10, height/10, "Customize", "customize")]
        self.bigFont = createFont("zx_spectrum-7.ttf", 96)
        self.smallFont = createFont("zx_spectrum-7.ttf", 48)
    
    def run(self):
        self.mountain.display(self.width/2, self.height/2, self.width, self.height) # This is the background
        if self.openerStage == 0: # When the black fades away
            if 4*(frameCount) < 256:
                fill(0, 0, 0, 255 - (frameCount)*4)
                rect(0, 0, self.width, self.height)
            else:
                self.openerStage = 1
        if self.openerStage == 1: # Logo appears
            if 4*(frameCount) < 462:
                tint(255, 4*(frameCount - 50))
                image(self.logo, 0, 0, self.width, self.height)
                noTint()
            else:
                self.openerStage = 2
        if self.openerStage == 2: # Buttons pop up
            image(self.logo, 0, 0, self.width, self.height)
            for i in range(len(self.menuButtons)):
                if i == 0:
                    textFont(self.bigFont)
                if i == 1:
                    textFont(self.smallFont)
                self.menuButtons[i].run()
            
