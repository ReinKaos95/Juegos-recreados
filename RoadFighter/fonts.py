# fonts.py
import pygame
from config import *

class FontManager:
    def __init__(self):
        pygame.font.init()
        self.default_font = pygame.font.SysFont("Arial", 36, bold=True)
        
    def render_text(self, text, color, size=36, bold=True):
        """Devuelve una superficie de texto renderizado"""
        font = pygame.font.SysFont("Arial", size, bold)
        return font.render(text, True, color)