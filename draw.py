import pygame


class Artist:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.screen.fill([255, 255, 255])
        
    def placeImage(self, imageFile, coords):
        img = pygame.image.load(imageFile)
        self.screen.blit(img, coords)
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
                
        pygame.display.flip()
