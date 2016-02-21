import pygame

from pygame.locals import *

import consts as c


class Bobby:
    def __init__(self, graphics):
        self.graphics = graphics

        self.bobby_img = pygame.transform.scale(self.graphics["mario_right.png"], (c.TILE_SIZE, c.TILE_SIZE))

        self.pos = [1*c.TILE_SIZE, 1*c.TILE_SIZE]

        self.speed = 0.50
        self.speed_state = 0

        self.moving_x = 0
        self.moving_y = 0

        self.reset_x = False
        self.reset_y = False

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


    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.state_to_return = "MENU" # TODO: MAKE IT POSSIBLE TO CHANGE THE STATE

            if event.key == pygame.K_UP:
                self.moving_y = -1

            if event.key == pygame.K_RIGHT:
                self.moving_x = 1

            if event.key == pygame.K_DOWN:
                self.moving_y = 1

            if event.key == pygame.K_LEFT:
                self.moving_x = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                self.reset_x = True

            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.reset_y = True


    def update(self, deltatime, map_size, levels):
        self.speed_state += self.speed * deltatime

        if self.speed_state > 1:
            self.speed_state = 0

            if self.moving_x > 0 and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE+1), int(self.pos[1]/c.TILE_SIZE)):
                self.pos[0] += c.TILE_SIZE
                self.looking_at = "right"

            if self.moving_x < 0 and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE-1), int(self.pos[1]/c.TILE_SIZE)):
                self.pos[0] -= c.TILE_SIZE
                self.looking_at = "left"

            if self.moving_y > 0 and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE), int(self.pos[1]/c.TILE_SIZE+1)):
                self.pos[1] += c.TILE_SIZE
                self.looking_at = "down"

            if self.moving_y < 0 and \
            not levels.is_blocking(int(self.pos[0]/c.TILE_SIZE), int(self.pos[1]/c.TILE_SIZE-1)):
                self.pos[1] -= c.TILE_SIZE
                self.looking_at = "up"

            if self.reset_x:
                self.reset_x = False
                self.moving_x = 0

            if self.reset_y:
                self.reset_y = False
                self.moving_y = 0

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

