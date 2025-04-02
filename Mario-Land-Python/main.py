import pygame
import sys
from config import *
from menu import *
#from sprites import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.title = pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
    def newGame(self):
        self.menu = Menu(self)
        self.sprites = Char(self)
        
    def update(self):
        #self.menu.update()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.update()
        
        
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        
    def Run(self):
        while True:
            self.events()
            self.update()
            
            
if __name__ == '__main__':
    game = Game()
    game.Run()