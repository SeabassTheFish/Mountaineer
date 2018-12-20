class Board: # Used for places with more than one area onscreen, like the village
    def __init__(self, canvasWidth, canvasHeight, imagePrefix, arrayWidth, arrayHeight, firstImage):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.imagePrefix = imagePrefix
        self.arrayWidth = arrayWidth
        self.arrayHeight = arrayHeight
        self.images = []
        for i in range(arrayWidth*arrayHeight): # Finding all the images
            self.images.append(loadImage(imagePrefix + "-" + str(i + 1) + ".png"))
        self.currentImage = firstImage
        self.action = ""
            
    def run(self): 
        self.display()
        
        # When the player moves offscreen to a different zone. I should probably make it pan, but this is the best I got (TODO)
        if self.action == "l":
            if self.currentImage%self.arrayWidth != 0:
                self.currentImage -= 1
        if self.action == "r":
            if self.currentImage%self.arrayWidth - 1 == 0:
                self.currentImage += 1
        if self.action == "u":
            if floor(self.currentImage/self.arrayWidth) != 0:
                self.currentImage -= self.arrayWidth
        if self.action == "d":
            if floor(self.currentImage/self.arrayWidth) != self.arrayHeight - 1:
                self.currentImage += self.arrayWidth
        
        self.action = ""
            
    def display(self):
        #background(0, 100, 0)
        image(self.images[self.currentImage], 0, 0, self.canvasWidth, self.canvasHeight)
