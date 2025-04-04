import pygame, os
from config import *

class Font:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        font_path = os.path.join(SPRITE_PATH, "NES - Road Fighter JPN - Font.png")
        if os.path.exists(font_path):
            try:
                self.font = pygame.font.Font(font_path, 24)
                if custom_font:
                    self.font = custom_font
            except:
                self.font = pygame.font.SysFont("Arial", 36, bold=True)
            
    def render_text(self, text, color, x, y, screen, centered=True):
        if self.font is None:
            self.font = pygame.font.SysFont("Arial", 36, bold=True)
        text_surface = self.font.render(text, True, color)
        if centered:
            x = (Width // 2) - (text_surface.get_width() // 2)
        screen.blit(text_surface, (x,y))
        