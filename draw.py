import pygame
import time
import settings


class Artist:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(settings.screenSize)
        self.white = [255, 255, 255]
        self.screen.fill(self.white)
        self.digging = False
        self.diggingStep = 0
        self.placed = False

    def getNearestCoord(self, mousePos):
        if mousePos[0] % 8 >= 0.5:
            x = (mousePos[0] // 8) * 8
        elif mousePos[0] % 8 < 5:
            x = (mousePos[0] // 8 - 1) * 8
        if mousePos[1] % 8 >= 0.5:
            y = (mousePos[1] // 8) * 8
        elif mousePos[1] % 8 < 5:
            y = (mousePos[1] // 8 - 1) * 8
        return (x, y)

    def placeImage(self, imageFile, coords):
        img = pygame.image.load(imageFile)
        img = pygame.transform.scale(img, (settings.imageSize, settings.imageSize))
        self.screen.blit(img, coords)
        
    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if not pygame.mouse.get_pressed()[0] and self.digging:
                    self.digging = False
                    self.diggingStep = 0
                if not pygame.mouse.get_pressed()[2] and self.placed:
                    self.placed = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and not self.digging:
                    self.digging = True
                if pygame.mouse.get_pressed()[2] and not self.placed:
                    self.placed = True
                    self.placeImage("textures/default_dirt.png", self.getNearestCoord(event.pos))
                
                
    def update(self):
        self.handleEvents()
        if self.digging:
            if self.diggingStep < 5:
                self.diggingStep += 1
                time.sleep(0.1)
            else:
                self.diggingStep = 0
                self.placeImage("textures/default_air.png", self.getNearestCoord(pygame.mouse.get_pos()))
        pygame.display.flip()
