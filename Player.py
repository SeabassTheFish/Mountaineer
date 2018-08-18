import json

class Player:
    def __init__(self):
        self.saveFilename = "saveData.txt"
        self.defaultsFilename = "defaultSave.txt"
        try:
            self.readSaveFile(self.saveFilename)
        except:
            self.readSaveFile(self.defaultsFilename)
    
    def readSaveFile(self, filename):
        file = open(filename, "r")
        saveData = " ".join(file.readlines())
        self.attributes = json.loads(saveData)
        file.close()
            
    def writeSaveFile(self):
        newSaveFile = open(self.saveFilename, "w")
        newSaveFile.write(json.dumps(self.attributes))
        newSaveFile.close()
        
