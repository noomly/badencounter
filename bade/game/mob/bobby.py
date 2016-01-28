import pygame

from pygame.locals import *

import consts as c


class Bobby:
    def __init__(self, graphics):
        self.graphics = graphics

        self.pos = [1*c.TILE_SIZE, 1*c.TILE_SIZE]

        self.looking_at = "right"


    def get_pos(self):
        return self.pos


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

        sprite = pygame.transform.scale(self.graphics["mario_right.png"], (c.TILE_SIZE, c.TILE_SIZE))

        if self.looking_at == "up":
            pass

        if self.looking_at == "right":
            pass

        if self.looking_at == "down":
            sprite = pygame.transform.flip(sprite, False, True)

        if self.looking_at == "left":
            sprite = pygame.transform.flip(sprite, True, False)

        render.blit(sprite, (0, 0))


        return render

