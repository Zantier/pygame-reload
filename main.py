import os
import pygame
from pygame.locals import *
import sys

WINDOW_LEFT = 800
WINDOW_TOP = 50
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
FPS = 30
BACKGROUND_COLOR = (200, 250, 230)

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_LEFT},{WINDOW_TOP}'
pygame.init()
fps_clock = pygame.time.Clock()
# The display surface
surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    surf.fill(BACKGROUND_COLOR)
    pygame.draw.circle(surf, 'red', (200, 100), 50)
    pygame.draw.circle(surf, 'blue', (300, 400), 130)

    pygame.display.update()
    fps_clock.tick(FPS)
