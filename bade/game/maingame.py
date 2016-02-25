import os

import pygame
from pygame.locals import *

import consts as c
from game.level import Level
from game.menu import Menu
from game.mob.bobby import Bobby
from game.dialog import Dialog

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

        menu = Menu(self.graphics, ("play", "exit"))

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

        in_dial = False
        pnj_name = "null"
        dial_count = 1

        state_to_return = "EXIT"
        goon = True
        while goon:
            #print(self.clock.get_fps())
            deltatime = self.clock.tick(30) / 100.0

            #events
            for event in pygame.event.get():
                if event.type == QUIT:
                    goon = False

                if in_dial:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RETURN:
                            dial_count += 1

                            try:
                                levels.chars[pnj_name]["dials"][str(dial_count)]
                            except Exception as ex:
                                in_dial = False
                                pnj_name = "null"
                                dial_count = 1
                else:
                    levels.event(event)

                    bobby.event(event)

            # updates
            bob_value = bobby.update(deltatime, levels.get_map_size(), levels)

            if bobby.get_state_to_return() == "MENU":
                state_to_return = "MENU"
                goon = False

            levels.update(bob_value, bobby)

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

            if bob_value.split(' ')[0] == "pnj" and not in_dial: # or in_dial
                in_dial = True
                pnj_name = bob_value.split(' ')[1]

            elif in_dial:
                my_font = pygame.font.Font("res/ubuntumono-r.ttf", 22)
                my_string = levels.chars[pnj_name]["dials"][str(dial_count)]
                my_rect = pygame.Rect((0, 0, c.WINDOW_WIDTH, c.WINDOW_HEIGHT/4))
                rendered_text = Dialog().render_textrect(my_string, my_font, my_rect, (216, 216, 216), (0, 0, 20, 175), 0)
                self.screen.blit(rendered_text, (0, c.WINDOW_HEIGHT - rendered_text.get_height()))

                # TODO: Change head if ":" or "*"
                head = pygame.transform.scale(self.graphics["mario_head.png"], (200, rendered_text.get_height()))
                self.screen.blit(head, (0, c.WINDOW_HEIGHT - rendered_text.get_height()))

                continue_font = my_font
                continue_font.set_italic(True)
                continue_font_rendered = continue_font.render("Press enter to continue...", 1, (150, 150, 150))
                self.screen.blit(continue_font_rendered, (c.WINDOW_WIDTH-continue_font_rendered.get_width(), c.WINDOW_HEIGHT - continue_font_rendered.get_height()))
            pygame.display.flip()

        print("exiting __game")

        return state_to_return


    def __load_graphics(self):
        for subdir, dirs, files in os.walk("res"):
            for item in files:
                if item.lower().endswith('.png') or item.lower().endswith('.jpg'):
                    try:
                        self.graphics[item] = pygame.image.load(str(subdir) + "/" +
                                                                str(item)).convert_alpha()
                    except Exception as ex:
                        print("caught exception at __load_graphics():", ex)

