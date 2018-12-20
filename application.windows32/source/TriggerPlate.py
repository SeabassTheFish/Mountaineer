class TriggerPlate: # Triggered when the player is standing on top of it
    def __init__(self, x, y, w, h, action, entity):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.action = action
        self.entity = entity
        
    def over(self):
        return self.entity.attributes["x"] > self.x and self.entity.attributes["x"] < self.x + self.w and self.entity.attributes["y"] > self.y and self.entity.attributes["y"] < self.y + self.h
        
    def run(self):
        noFill()
        noStroke()
        rect(self.x, self.y, self.w, self.h)
        if self.over():
            return True
        else:
            return False
            
