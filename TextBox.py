class TextBox: # An interactive text box the user can use
    def __init__(self, x, y, w, h, txt):
        self.x = x;
        self.y = y
        self.w = w
        self.h = h
        self.state = "fixed"
        self.txt = txt
        self.font = createFont("zx_spectrum-7.ttf", self.h*2)
        self.displayLength = 0
    
    def display(self, modeTime):
        fill(150)
        stroke(0)
        strokeWeight(3)
        rect(self.x, self.y, self.w, self.h)
        textAlign(LEFT, CENTER)
        textFont(self.font)
        fill(255)
        if self.state == "fixed":
            text(self.txt, self.x, self.y)
        elif self.state == "edit":
            if floor(modeTime/15)%2 == 0:
                text(self.txt + "|", self.x, self.y)
            else:
                text(self.txt, self.x, self.y)

    def xyOver(self, x, y): # Like a button, the user can only type in it when clicked
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h
