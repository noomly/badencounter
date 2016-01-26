import os

import pygame
from pygame.locals import *

import consts as c
from game.level import Level
from game.mob.bobby import Bobby


class MainGame(object):
    def __init__(self):
        print("Initializing game...")

        self.screen = pygame.display.set_mode((c.WINDOW_WIDTH,
                                               c.WINDOW_HEIGHT))

        self.clock = pygame.time.Clock()

        self.graphics = {}
        self.__load_graphics()


    def game_loop(self):
        print("Entering game_loop")

        levels = Level(self.graphics, "home")

        bobby = Bobby(self.graphics)

        finalrender = pygame.Surface((levels.get_map_size()[0],
                                      levels.get_map_size()[1]))

        goon = True
        while goon:
            #print(self.clock.get_fps())

            #events
            for event in pygame.event.get():
                if event.type == QUIT:
                    goon = False

                levels.event(event)

                bobby.event(event, levels)

            # updates
            move = bobby.update(levels.get_map_size())

            levels.update(move, bobby)
            #print(levels.get_tile(1, 1))

            if finalrender.get_width() != levels.get_map_size()[0] or finalrender.get_height() != levels.get_map_size()[1]:
                finalrender = pygame.Surface((levels.get_map_size()[0],
                                              levels.get_map_size()[1]))

            # draws
            finalrender.blit(levels.draw(), (0, 0))

            b_x, b_y = bobby.get_pos()
            finalrender.blit(bobby.draw(), (b_x, b_y))

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
                    try:
                        self.graphics[item] = pygame.image.load(str(subdir) + "/" +
                                                                str(item)).convert_alpha()
                    except Exception as ex:
                        print("caught exception at __load_graphics():", ex)

