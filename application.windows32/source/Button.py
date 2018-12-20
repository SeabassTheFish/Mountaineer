class Button: # Incredibly useful and versatile
    def __init__(self, x, y, w, h, txt, actionTo):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = txt
        self.shadowSize = 10 # To give it that nice "click" effect
        self.actionTo = actionTo
        
    def display(self):
        textAlign(LEFT, CENTER)
        for i in range(self.shadowSize):
            rect(self.x - i + self.shadowSize, self.y - i + self.shadowSize, self.w, self.h)
        fill(0)
        textFont(createFont("zx_spectrum-7.ttf", 48))
        textAlign(CENTER, CENTER)
        text(self.txt, self.x + self.w/2, self.y + self.h/3)
        fill(255)
        
    def run(self):
        self.display()
        if self.xyOver(mouseX, mouseY): # A clever thing by my dad. My main checks for mouseClicked anyway, so it checks all the buttons only when that happens.
            self.shadowSize = 5
        else:
            self.shadowSize = 10
        
    def xyOver(self, x, y):
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h
    
    def showClicked(self):
        self.shadowSize = 1
