import pygame
from config import *
from fonts import FontManager

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.fonts = FontManager()
        self.selected_index = 0
        self.menu_items = [
            {"text": "LEVEL 1", "action": "level1"},
            {"text": "LEVEL 2", "action": "level2"},
            {"text": "EXIT", "action": "exit"}
        ]
        self.background = None  # Puedes cargar una imagen aquí

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected_index = (self.selected_index + 1) % len(self.menu_items)
                elif event.key == pygame.K_UP:
                    self.selected_index = (self.selected_index - 1) % len(self.menu_items)
                elif event.key == pygame.K_RETURN:
                    return self.menu_items[self.selected_index]["action"]
        return None

    def draw(self):
        # Fondo (opcional)
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill(BLACK)

        # Título
        title = self.fonts.render_text("ROAD FIGHTER", YELLOW, 48)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))

        # Items del menú
        for i, item in enumerate(self.menu_items):
            color = WHITE if i == self.selected_index else RED
            prefix = "► " if i == self.selected_index else "  "
            text = self.fonts.render_text(f"{prefix}{item['text']}", color)
            self.screen.blit(text, (WIDTH//2 - text.get_width()//2, 250 + i * 50))

        # Copyright
        copyright = self.fonts.render_text("© 1985 KONAMI", WHITE, 24)
        self.screen.blit(copyright, (WIDTH//2 - copyright.get_width()//2, 500))