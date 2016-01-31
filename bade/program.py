# NUMERO DE GROUPE : 3
import sys
import os

import pygame

from game.maingame import MainGame


def main():
    print("Welcome to our super project \"Bad Encounter\"!")

    pygame.display.init()
    pygame.font.init()

    game = MainGame()
    game.main_loop()


if __name__ == '__main__':
    print("entering program")

    main()

    print("exiting program")

    pygame.quit()
    sys.exit()
