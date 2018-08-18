class TextBox:
    def __init__(self, x, y, w, h):
        self.x = x;
        self.y = y
        self.w = w
        self.h = h
        self.state = "fixed"
        self.txt = ""
        self.font = createFont("zx_spectrum-7.ttf", self.h*2)
    
    def display(self, displayText):
        fill(150)
        stroke(0)
        strokeWeight(3)
        rect(self.x, self.y, self.w, self.h)
        textAlign(LEFT, CENTER)
        textFont(self.font)
        fill(255)
        if self.state == "fixed":
            text(displayText, self.x, self.y)
        elif self.state == "edit":
            if floor(frameCount/15)%2 == 0:
                text(self.txt + "|", self.x, self.y)
            else:
                text(self.txt, self.x, self.y)
        
    def run(self):
        self.display()
        
    def xyOver(self, x, y):
        return x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h
