import os
import pygame
from pygame.locals import *
import sys

WINDOW_LEFT = 1500
WINDOW_TOP = 100
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 1200
FPS = 30
BACKGROUND_COLOR = (200, 250, 230)
CIRCLE_COLOR = (230, 180, 180)

os.environ['SDL_VIDEO_WINDOW_POS'] = f'{WINDOW_LEFT},{WINDOW_TOP}'
pygame.init()
fps_clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((1200, 1200))


def draw():
    pygame.draw.circle(display_surface, CIRCLE_COLOR, (200, 200), 50)
    pygame.draw.circle(display_surface, CIRCLE_COLOR, (400, 600), 130)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill(BACKGROUND_COLOR)
    draw()
    pygame.display.update()
    fps_clock.tick(FPS)
