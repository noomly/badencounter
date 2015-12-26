import pygame
import pygame.locals

import configparser

class Level(object):
    def __init__(self, graphics, levelname):
        self.graphics = graphics
        self.levelname = levelname

        self.map = []

        self.map_width = -1
        self.map_height = -1

        self.key = {}

        self.__load_file()


    def __load_file(self):
        parser = configparser.ConfigParser()
        parser.read(self.levelname + ".map")

        self.map = str(parser.get("level", "map")).split("\n")

        self.map_width = len(self.map[0])
        self.map_height = len(self.map)

        for section in parser.sections():
            if len(section) == 1:
                self.key[section] = dict(parser.items(section))


    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError as ex:
            print(ex)

        try:
            return self.key[char]
        except KeyError as ex:
            print(ex)


    def get_bool(self, x, y, name):
        value = self.get_tile(x, y).get(name)

        return value is True


    def is_blocking(self, x, y):
        if not 0 <= x < self.map_width or not 0 <= y < self.map_height:
            return True
        else:
            return self.get_bool(x, y, 'block')


    def draw(self):
        render = pygame.Surface((self.map_width*16, self.map_height*16))

        for y, line in enumerate(self.map):
            for x, char in enumerate(line):
                render.blit(self.graphics[self.get_tile(x, y).get("tile")],
                            (x*16, y*16))

        return render

