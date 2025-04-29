import pygame
#import math
#import random
#import time
import sys


WIDTH = 600
HEIGHT = 600
PIXELS = 32
SQUARES = int(WIDTH/PIXELS)

BG1 = (156, 210, 54)
BG2 = (147, 203, 57)

class Background:

    def draw(self, surface):
        surface.fill(BG1)
        counter = 0
        for row in range(SQUARES):
            for col in range(SQUARES):
                if counter % 2 == 0:
                    pygame.draw.rect(surface, BG2, (col * PIXELS, row * PIXELS, PIXELS, PIXELS))
                if col != SQUARES - 1:
                   counter += 1


def main():
    pygame.init()
    screen = pygame.display.set_mode( (WIDTH, HEIGHT)   )
    pygame.display.set_caption("SNAKE")

    background = Background()

    while True:
        background.draw(screen)

        for events in pygame.event.get():
         if events.type == pygame.QUIT:
             sys.exit()


        pygame.display.update()



main()