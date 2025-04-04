import pygame
import sys
from config import *
from menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.current_menu = Menu(self.screen)

    def run(self):
        while self.running:
            events = pygame.event.get()
            
            # Manejo de eventos del menú
            menu_result = self.current_menu.handle_events(events)
            if menu_result == "exit":
                self.running = False
            elif menu_result in ["level1", "level2"]:
                self.start_level(menu_result)

            # Renderizado
            self.current_menu.draw()
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

    def start_level(self, level):
        print(f"Iniciando {level}...")
        # Aquí iría la lógica para cambiar al juego

if __name__ == "__main__":
    game = Game()
    game.run()