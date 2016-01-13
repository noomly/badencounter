import os

import pygame
from pygame.locals import *

import consts as c
from game.level import Level


class MainGame(object):
    def __init__(self):
        print("MainGame initializing...")

        self.screen = pygame.display.set_mode((c.WINDOW_WIDTH,
                                               c.WINDOW_HEIGHT))

        self.clock = pygame.time.Clock()

        self.graphics = {}
        self.__load_graphics()
        print(self.graphics)

        print("MainGame initialized")


    def game_loop(self):
        print("Entering game_loop")

        level1 = Level(self.graphics, "game/level")

        finalrender = pygame.Surface((level1.get_map_size()[0] * c.TILE_SIZE,
                                      level1.get_map_size()[1] * c.TILE_SIZE))

        goon = True
        while goon:
            print(self.clock.get_fps())

            for event in pygame.event.get():
                if event.type == QUIT:
                    goon = False

            # events

            # updates

            # draws
            finalrender.blit(level1.draw(), (0, 0))

            self.screen.blit(pygame.transform.scale(finalrender,
                                                    (c.WINDOW_WIDTH,
                                                     c.WINDOW_HEIGHT)),
                             (0, 0))

            pygame.display.flip()

            self.clock.tick(15)

        print("Exiting game_loop")


    def __load_graphics(self):
        for subdir, dirs, files in os.walk("res"):
            for item in files:
                if item.lower().endswith('.png'):
                    self.graphics[item] = pygame.image.load(str(subdir) + "/" +
                                                            str(item)).convert()

