import draw
import random
import settings

textures = ['textures/default_acacia_leaves.png', 'textures/default_acacia_tree.png', 'textures/default_acacia_wood.png', 'textures/default_aspen_leaves.png', 'textures/default_aspen_tree.png', 'textures/default_aspen_wood.png', 'textures/default_bookshelf.png', 'textures/default_brick.png', 'textures/default_bronze_block.png', 'textures/default_cactus_side.png', 'textures/default_chest_front.png', 'textures/default_chest_lock.png', 'textures/default_clay.png', 'textures/default_coal_block.png', 'textures/default_cobble.png', 'textures/default_copper_block.png', 'textures/default_diamond_block.png', 'textures/default_dirt.png']

artist = draw.Artist()

for i in range(settings.screenSize[0]/(settings.imageSize/2) - 1):
    for ii in range(settings.screenSize[1]/(settings.imageSize/2) - 1):
        texture = random.choice(textures)
        artist.placeImage(texture, (i*settings.imageSize, ii*settings.imageSize))

while artist.update() != "Quit":
    pass
