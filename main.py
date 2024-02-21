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
CIRCLE_COLOR = (230, 180, 180)

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_LEFT},{WINDOW_TOP}'
pygame.init()
fps_clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill(BACKGROUND_COLOR)
    pygame.draw.circle(display_surface, CIRCLE_COLOR, (200, 100), 50)
    pygame.draw.circle(display_surface, CIRCLE_COLOR, (300, 400), 130)

    pygame.display.update()
    fps_clock.tick(FPS)
