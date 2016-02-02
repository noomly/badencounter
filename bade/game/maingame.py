import os

import pygame
from pygame.locals import *

import consts as c
from game.level import Level
from game.menu import Menu
from game.mob.bobby import Bobby


class MainGame(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((c.WINDOW_WIDTH,
                                               c.WINDOW_HEIGHT))

        self.clock = pygame.time.Clock()

        self.graphics = {}
        self.__load_graphics()


    def main_loop(self):
        print("entering main_loop")

        state = "MENU" # MENU, GAME, EXIT

        while state != "EXIT":
            if state == "MENU":
                state = self.__menu()

            if state == "GAME":
                state = self.__game()

        print("exiting main_loop")


    def __menu(self):
        print("entering __menu")

        menu = Menu(self.graphics, ("Bad Encounter", "play", "exit"))

        state_to_return = "EXIT"
        goon = True
        while goon:
            # events
            for event in pygame.event.get():
                if event.type == QUIT:
                    goon = False

                menu.event(event)

            # updates
            menu.update()

            choice = menu.get_clicked_button_txt()

            if choice == "play":
                state_to_return = "GAME"
                goon = False

            if choice == "exit":
                state_to_return = "EXIT"
                goon = False

            # draws
            finalrender = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))

            finalrender.blit(menu.draw(), (0, 0))

            self.screen.blit(pygame.transform.scale(finalrender,
                                                    (c.WINDOW_WIDTH,
                                                     c.WINDOW_HEIGHT)),
                             (0, 0))

            pygame.display.flip()

            self.clock.tick(60)

        print("exiting __menu")

        return state_to_return


    def __game(self):
        print("entering __game")

        levels = Level(self.graphics, "home")

        bobby = Bobby(self.graphics)

        finalrender = pygame.Surface((levels.get_map_size()[0],
                                      levels.get_map_size()[1]))

        state_to_return = "EXIT"
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

            if bobby.get_state_to_return() == "MENU":
                state_to_return = "MENU"
                goon = False

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

        print("exiting __game")

        return state_to_return


    def __load_graphics(self):
        for subdir, dirs, files in os.walk("res"):
            for item in files:
                if item.lower().endswith('.png'):
                    try:
                        self.graphics[item] = pygame.image.load(str(subdir) + "/" +
                                                                str(item)).convert_alpha()
                    except Exception as ex:
                        print("caught exception at __load_graphics():", ex)

