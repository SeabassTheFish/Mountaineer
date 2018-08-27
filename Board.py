class Board:
    def __init__(self, canvasWidth, canvasHeight, imagePrefix, arrayWidth, arrayHeight, firstImage):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.imagePrefix = imagePrefix
        self.arrayWidth = arrayWidth
        self.arrayHeight = arrayHeight
        self.images = []
        for i in range(arrayWidth*arrayHeight):
            self.images.append(loadImage(imagePrefix + "-" + str(i + 1) + ".png"))
        self.currentImage = firstImage
        self.action = ""
            
    def run(self):
        self.display()
        if self.action == "l":
            if self.currentImage%self.arrayWidth != 0:
                self.currentImage -= 1
            self.action = ""
        if self.action == "r":
            if self.currentImage%self.arrayWidth - 1 == 0:
                self.currentImage += 1
            self.action = ""
        if self.action == "u":
            if floor(self.currentImage/self.arrayWidth) != 0:
                self.currentImage -= self.arrayWidth
            self.action = ""
        if self.action == "d":
            if floor(self.currentImage/self.arrayWidth) != self.arrayHeight - 1:
                self.currentImage += self.arrayWidth
            self.action = ""
            
    def display(self):
        background(0, 100, 0)
        image(self.images[self.currentImage], 0, 0, self.canvasWidth, self.canvasHeight)
            
