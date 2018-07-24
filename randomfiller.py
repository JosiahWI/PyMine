import draw
import random

textures = ['textures/default_acacia_leaves.png', 'textures/default_acacia_tree.png', 'textures/default_acacia_wood.png', 'textures/default_aspen_leaves.png', 'textures/default_aspen_tree.png', 'textures/default_aspen_wood.png', 'textures/default_bookshelf.png', 'textures/default_brick.png', 'textures/default_bronze_block.png', 'textures/default_cactus_side.png', 'textures/default_chest_front.png', 'textures/default_chest_lock.png', 'textures/default_clay.png', 'textures/default_coal_block.png', 'textures/default_cobble.png', 'textures/default_copper_block.png', 'textures/default_diamond_block.png', 'textures/default_dirt.png']

artist = draw.Artist()

for i in range(99):
    for ii in range(99):
        texture = random.choice(textures)
        artist.placeImage(texture, (i*8, ii*8))

while artist.update() != "Quit":
    pass
