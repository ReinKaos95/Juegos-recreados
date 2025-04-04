import pygame, sys
from fonts import Font
from config import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(Res)
        self.title = pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()
        self.font = Font()
        self.menu_option = ['LEVEL 1, LEVEL 2, EXIT']
        self.select = 0
        self.running = True
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.select = (self.select + 1) % len(self.menu_option)
                elif event.key == pygame.K_UP:
                    self.select = (self.select - 1) % len(self.menu_option)
                elif event.key == pygame.K_RETURN:
                    if self.select == 2:
                        self.running = False
                    else:
                        print(f"Iniciando: {self.menu_option[self.select]}")
    
    def draw_menu(self):
        self.screen.fill(Black)
        self.font.render_text("ROAD FIGHTER", Yellow, 0, 150, self.screen)
        for i, option in enumerate(self.menu_option):
            color = White if i == self.select else Red
            prefix = "►" if i == self.select else " "
            self.font.render_text(f"{prefix} {option}", color, 0, 250 + i * 50, self.screen)
        self.font.render_text("© 1985 KONAMI", White, 0, 500, self.screen)
    

    def update(self):
        self.delta_time = self.clock.tick(FPS)
        pygame.display.update()
   
    def run(self):
        while self.running:
            self.handle_events()
            self.draw_menu()
            self.update()
        pygame.quit()
        sys.exit()
            
if __name__ == '__main__':
    game=Game()
    game.run()