class TriggerPlate:
    def __init__(self, x, y, w, h, action, entity):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.action = action
        self.entity = entity
        
    def over(self):
        return entity.x > self.x and entity.x < self.x + self.w and entity.y > self.y and entity.y < self.y + self.h
        
    def run(self):
        rect(self.x, self.y, self.w, self.h)
