class ObjectDefinition:

    def __init__(self, name, imageFile, biomeData, onLeftClick, onRightClick):
        self.name = name
        self.imageFile = imageFile
        self.biomeData = biomeData
        self.onLeftClick = onLeftClick
        self.onRightClick = onRightClick
        self.objectList = {}
        
        
    def create_obj(self, x, y):
        obj = Object(self, x, y)
        self.objectList[(x, y)] = obj
        return obj
        
class Object:

    def __init__(self, objectDefinition, x, y):
        self.obj = objectDefinition
        self.x = x
        self.y = y
