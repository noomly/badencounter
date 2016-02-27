import pygame

from pygame.locals import *


class Character:
    def __init__(self, graphics, character_name):
        self.graphics = graphics

        self.bobby_img = pygame.transform.scale(self.graphics[character_name+".png"], (c.TILE_SIZE, c.TILE_SIZE))

        self.pos = [1*c.TILE_SIZE, 1*c.TILE_SIZE]

        self.looking_at = ""
        self.looking_atH = "right"

        self.state_to_return = ""


    def get_pos(self):
        return self.pos


    def get_state_to_return(self):
        return self.state_to_return


    def update_pos(self, move, map_size):
        if move == "north":
            self.pos[1] = map_size[1] - c.TILE_SIZE

        if move == "east":
            self.pos[0] = 0

        if move == "south":
            self.pos[1] = 0

        if move == "west":
            self.pos[0] = map_size[0] - c.TILE_SIZE


    def event(self, event, levels):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_to_return = "MENU" # TODO: MAKE IT POSSIBLE TO CHANGE THE STATE

            if event.key == pygame.K_UP and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE), int(self.pos[1]/c.TILE_SIZE-1)):
                self.pos[1] -= c.TILE_SIZE
                self.looking_at = "up"

            if event.key == pygame.K_RIGHT and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE+1), int(self.pos[1]/c.TILE_SIZE)):
                self.pos[0] += c.TILE_SIZE
                self.looking_at = "right"

            if event.key == pygame.K_DOWN and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE), int(self.pos[1]/c.TILE_SIZE+1)):
                self.pos[1] += c.TILE_SIZE
                self.looking_at = "down"

            if event.key == pygame.K_LEFT and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE-1), int(self.pos[1]/c.TILE_SIZE)):
                self.pos[0] -= c.TILE_SIZE
                self.looking_at = "left"


    def update(self, map_size):
        if self.pos[1] < 0:
            print("move north")
            return "north"

        if self.pos[0] > map_size[0] - c.TILE_SIZE:
            print("move east")
            return "east"

        if self.pos[1] > map_size[1] - c.TILE_SIZE:
            print("move south")
            return "south"

        if self.pos[0] < 0:
            print("move west")
            return "west"


    def draw(self):
        render = pygame.Surface((c.TILE_SIZE, c.TILE_SIZE), pygame.SRCALPHA)

        if self.looking_at == "up":
            pass

        if self.looking_at == "right":
            if self.looking_atH == "left":
                self.bobby_img = pygame.transform.flip(self.bobby_img, True, False)

            self.looking_atH = "right"

        if self.looking_at == "down":
            #sprite = pygame.transform.flip(sprite, False, True)
            pass

        if self.looking_at == "left":
            if self.looking_atH == "right":
                self.bobby_img = pygame.transform.flip(self.bobby_img, True, False)

            self.looking_atH = "left"

        self.looking_at = ""

        render.blit(self.bobby_img, (0, 0))


        return render

    def __init__(self, is_player, image_little, image_big):
        # Manage if character is the player

        # Else, what png to load
        self.image_little = image_little
        self.image_big = image_big


    def event(self, event):
        pass


    def update():
        pass


    def draw(self, graphics):
        pass

