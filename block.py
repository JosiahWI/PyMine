class BlockManager:

    def __init__(self):
        self.registeredBlocks = {}
        
    def registerBlock(self, name, imageFile, onLeftClick, onRightClick, data):
        self.registeredBlocks[name] = BlockDefinition(name, imageFile, onLeftClick, onRightClick, data)
        
    def getDefinition(self, name):
        if name in self.registeredBlocks:
            return self.registeredBlocks[name]
        else:
            raise StandardError("Block %s has not been registered." % name)
        
    def place(self, name, pos):
        definition = self.getDefinition(name)
        block = definition.createBlock(pos)
        return block
        

class BlockDefinition:

    def __init__(self, name, imageFile, onLeftClick, onRightClick, data):
        self.name = name
        self.imageFile = imageFile
        self.onLeftClick = onLeftClick
        self.onRightClick = onRightClick
        self.data = data
        self.blockList = {}
        
        
    def createBlock(self, pos):
        block = Block(self.name, pos)
        self.blockList[pos] = block
        return block
        
class Block:

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
