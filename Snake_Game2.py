'''

 Game with Simple graphics and a,s,d,w controls.
 Module "classes" to be included with the main file on the folder, Error free.
 _Allen.

'''

import pygame, sys, os
from pygame.locals import *
from classes import *
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
    pygame.init()
    pygame.display.set_caption('Snake Game')

    window = pygame.display.set_mode((560, 560))
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 20)

    game = SnakeGame(window, screen, clock, font)

    while game.run(pygame.event.get()):
        pass

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
