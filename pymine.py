import block
import draw
import settings
import mod
import random
import sys

blockManager = block.BlockManager()
artist = draw.Artist(blockManager)
for blockDef in mod.blocks:
    blockManager.registerBlock(blockDef)
    
    
while artist.update() != "quit":
    pass
