import pygame
import pygame.locals

import configparser

class Level(object):
    def __init__(self, graphics, initialmap):
        self.graphics = graphics

        self.maps = {}
        self.currentmap = initialmap

        self.key = {}

        self.__load_file()
pass

    def __load_file(self):
        parser = configparser.ConfigParser()
        parser.read("game/level.map")

        for section in parser.sections():
            if len(section) == 1:
                self.key[section] = dict(parser.items(section))
            else:
                self.maps[section] = dict(parser.items(section))
                self.maps[section]["map"] = str(self.maps[section]["map"]).split("\n")

                self.maps[section]["width"] = len(self.maps[section]["map"][0])
                self.maps[section]["height"] = len(self.maps[section]["map"])

            #try:
            #    assert len(self.maps[section]["map"]) == 6
            #except Exception:
            #    print("ERROR: map size isn't respectful")


    def get_map_size(self):
        return (self.maps[self.currentmap]["width"],
                self.maps[self.currentmap]["height"])


    def get_tile(self, x, y):
        try:
            char = self.maps[self.currentmap]["map"][y][x]
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


    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("moving north")

            if event.key == pygame.K_RIGHT:
                print("moving east")

            if event.key == pygame.K_DOWN:
                print("moving south")

            if event.key == pygame.K_LEFT:
                print("moving west")

    def draw(self):
        width, height = self.get_map_size()

        render = pygame.Surface((width*16, height*16))

        for y, line in enumerate(self.maps[self.currentmap]["map"]):
            for x, char in enumerate(line):
                render.blit(self.graphics[self.get_tile(x, y).get("file")],
                            (x*16, y*16))

        return render

