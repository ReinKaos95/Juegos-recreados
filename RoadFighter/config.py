# config.py
import os

# Sistema de ventana
TITLE = "Road Fighter PyGame"
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colores (paleta NES)
BLACK = (0, 0, 0)
RED = (208, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (248, 248, 0)

# Rutas (usando os.path para compatibilidad)
RESOURCES_DIR = os.path.join('Resources')
SPRITES_DIR = os.path.join(RESOURCES_DIR, 'Sprites')