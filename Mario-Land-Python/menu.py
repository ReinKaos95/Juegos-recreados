import pygame
from config import *

class Menu:
    def __init__(self):
        self.menu = menu
        self.screen = screen
        self.getMenu()
        
    def getMenu(self):
        image = pygame.image.load(SPRITE_PATH + 'Daisies/TitleScreen.png')
        screen = RES
        screen.blit(image, (0, 0))
        pygame.display.update()

    def update(self):
        self.getMenu()
