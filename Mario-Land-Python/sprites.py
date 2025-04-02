import pygame
from config import *

class Char(pygame.sprite.Sprite):
    
    def __init__(self, color="red", width=16, height=16):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        """
        self.spriteSheet = pygame.image.load(SPRITE_PATH + "Main/Mario.png").convert_alpha()
        self.image = pygame.transform.scale(self.spriteSheet.subsurface(0,0,200,420),(100,200))
        self.rect = pygame.image.get_rect()
        """
    def update():
        pass