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
        self.north = loadImage("ArrowUp.png")
        self.south = loadImage("ArrowDown.png")
        self.west = loadImage("ArrowLeft.png")
        self.east = loadImage("ArrowRight.png")
        
    def display(self): # Displays what arrow keys the user can press to do something
        if self.n:
            image(self.north, self.x - self.w/8, self.y - self.h/2, self.w/4, self.h/3)
        if self.s:
            image(self.south, self.x - self.w/8, self.y, self.w/4, self.h/3)
        if self.we:
            image(self.west, self.x - self.w/4, self.y - self.h/4, self.w/4, self.h/3)
        if self.e:
            image(self.east, self.x, self.y - self.h/4, self.w/4, self.h/3)
            
