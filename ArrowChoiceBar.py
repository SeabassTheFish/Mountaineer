class ArrowChoiceBar:
    def __init__(self, x, y, w, h, n, s, e, we):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.n = n
        self.s = s
        self.e = e
        self.we = we
        
    def display(self):
        if self.n:
            image(loadImage("ArrowUp.png"), self.x - self.w/8, self.y - self.h/2, self.w/4, self.h/3)
            
