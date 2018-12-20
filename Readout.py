class Readout: # Succinct little script for a typing readout at the bottom of the screen
    def __init__(self, x, y, w, h, txt):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.txt = txt
        self.displayLength = 0
        
    def display(self, modeTime, txtFill):
        strokeWeight(5)
        rect(self.x, self.y, self.w, self.h, 50)
        
        if self.displayLength < len(self.txt):
                if modeTime%2 == 0:
                    self.displayLength += 1
        textAlign(LEFT, TOP)
        fill(txtFill)
        text(self.txt[:self.displayLength], self.x + 10, self.y)
