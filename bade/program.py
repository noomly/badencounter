# NUMERO DE GROUPE : 3
import pygame

from game.maingame import MainGame


def main():
    print("Welcome to our super project \"Bad Encounter\"!")

    pygame.init()

    game = MainGame()
    game.main_loop()


if __name__ == '__main__':
    main()
