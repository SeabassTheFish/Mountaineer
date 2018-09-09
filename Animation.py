class Animation:
    def __init__(self, imagePrefix, count, delay):
        self.imageCount = count
        self.frame = 0
        self.images = []
        self.delay = delay
        
        for i in range(self.imageCount):
            filename = str(imagePrefix) + "-" + str(i + 1) + ".png"
            self.images.append(loadImage(filename))
            
    def display(self, x, y, w, h):
        self.frame = (self.frame + 1) % (self.imageCount * self.delay)
        image(self.images[floor(self.frame / self.delay)], x - w/2, y - h/2, w, h)
