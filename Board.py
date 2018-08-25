class Board:
    def __init__(self, canvasWidth, canvasHeight, imagePrefix, arrayWidth, arrayHeight):
        self.canvasWidth = canvasWidth
        self.canvasHeight = canvasHeight
        self.imagePrefix = imagePrefix
        self.arrayWidth = arrayWidth
        self.arrayHeight = arrayHeight
        self.images = []
        for i in range(arrayWidth*arrayHeight):
            self.images.append(loadImage(imagePrefix + "-" + str(i)))
