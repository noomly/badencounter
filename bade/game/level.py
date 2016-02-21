import pygame

import configparser

import consts as c


class Level(object):
    def __init__(self, graphics, initialmap):
        self.graphics = graphics

        self.maps = {}
        self.currentmap = initialmap

        self.key = {}

        self.__load_file()


    def __load_file(self):
        parser = configparser.ConfigParser()
        parser.read("game/level.map")

        for section in parser.sections():
            if len(section) == 1:
                self.key[section] = dict(parser.items(section))
            else:
                self.maps[section] = dict(parser.items(section))
                self.maps[section]["map"] = str(self.maps[section]["map"]).split("\n")

                self.maps[section]["width"] = len(self.maps[section]["map"][0])*c.TILE_SIZE
                self.maps[section]["height"] = len(self.maps[section]["map"])*c.TILE_SIZE

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
            return self.key[char]

        except Exception as ex:
            print("caught exception at get_tile(" + str(x) + "," + str(y) + "):", ex)


    def get_bool(self, x, y, name):
        try:
            return self.get_tile(x, y)[name] == "true"
        except Exception as ex:
            print("caught exception at get_bool(" + str(x) + "," + str(y) + "," +  name + "):", ex)


    def is_blocking(self, x, y):
        map_size = self.get_map_size()

        if (x < 0 or x > (map_size[0]/c.TILE_SIZE)) or \
           (y < 0 or y > (map_size[1]/c.TILE_SIZE)):
            return False
        else:
            return self.get_bool(x, y, 'block')


    def event(self, event):
        pass


    def update(self, move, bobby):
        if move == "north":
            if "north" in self.maps[self.currentmap]:
                self.currentmap = self.maps[self.currentmap]["north"]
                bobby.update_pos(move, self.get_map_size())
            else:
                print("TRYING TO GET OUT OF THE WOOOOORLD")

        if move == "east":
            if "east" in self.maps[self.currentmap]:
                self.currentmap = self.maps[self.currentmap]["east"]
                bobby.update_pos(move, self.get_map_size())
            else:
                print("TRYING TO GET OUT OF THE WOOOOORLD")

        if move == "south":
            if "south" in self.maps[self.currentmap]:
                self.currentmap = self.maps[self.currentmap]["south"]
                bobby.update_pos(move, self.get_map_size())
            else:
                print("TRYING TO GET OUT OF THE WOOOOORLD")


        if move == "west":
            if "west" in self.maps[self.currentmap]:
                self.currentmap = self.maps[self.currentmap]["west"]
                bobby.update_pos(move, self.get_map_size())
            else:
                print("TRYING TO GET OUT OF THE WOOOOORLD")


    def draw(self):
        width, height = self.get_map_size()

        render = pygame.Surface((width, height))

        for y, line in enumerate(self.maps[self.currentmap]["map"]):
            for x, char in enumerate(line):
                render.blit(pygame.transform.scale(self.graphics[self.get_tile(x, y).get("file")],
                                                   (c.TILE_SIZE, c.TILE_SIZE)),
                                                   (x*c.TILE_SIZE, y*c.TILE_SIZE))

        return render

