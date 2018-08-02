import block
import draw
import settings
import mod
import random
import sys

blockManager = block.BlockManager()
artist = draw.Artist(blockManager)
for blockName in mod.blocks:
    blockDef = mod.blocks[blockName]
    blockManager.registerBlock(blockName, blockDef["imageFile"], blockDef["onLeftClick"], blockDef["onRightClick"], blockDef["data"])
    
    
while artist.update() != "quit":
    pass
