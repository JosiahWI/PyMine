class BlockManager:

    def __init__(self):
        self.registeredObjects = {}
        
    def registerBlock(name, imageFile, onLeftClick, onRightClick):
        self.registeredObjects[name] = BlockDefinition(name, imageFile, onleftClick, onRightClick, data)
        
    def getDefinition(self):
        if name in self.registeredObjects:
            return self.registeredObjects[name]
        else:
            raise StandardError("Block %s has not been registered." % name)
        
    def place(self, name, pos):
        definition = self.getDefinition(name)
        definition.createBlock(pos)

            
    def remove(self, name, pos):
        definition = self.getDefinition(name)
        definition.removeBlock(pos)
        

class BlockDefinition:

    def __init__(self, name, imageFile, onLeftClick, onRightClick, data):
        self.name = name
        self.imageFile = imageFile
        self.onLeftClick = onLeftClick
        self.onRightClick = onRightClick
        self.data = data
        self.blockList = {}
        
        
    def createBlock(self, pos):
        obj = Object(self.name, pos)
        self.blockList[pos] = obj
        return obj
        
    def removeBlock(self, pos):
        raise StandardError("removeBlock hasn't been implemented yet.")
        
class Block:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
