import pygame

from pygame.locals import *

import consts as c


class Menu:
    def __init__(self, graphics, buttons_txt):
        self.graphics = graphics

        self.buttons = []

        for i in range(0, len(buttons_txt), 1):
            self.buttons.append(Button(self.graphics, buttons_txt[i], c.WINDOW_WIDTH / 2, 100 + i * 100))

        #self.background_img = pygame.image.load("res/background_menu.png").convert_alpha()
        #self.background_img = pygame.transform.scale(self.background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))

        self.clicked_button_txt = "NONE"


    def event(self, event):
        for button in self.buttons:
            button.event(event)
            if button.get_button_state() == "CLICKED":
                self.clicked_button_txt = button.get_button_txt()


    def update(self):
        for button in self.buttons:
            button.update()


    def draw(self):
        render = pygame.Surface((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        #window.blit(self.background_img, (0, 0))

        for button in self.buttons:
            button.draw(render)

        return render


    def get_clicked_button_txt(self):
        return self.clicked_button_txt


    def set_clicked_button_to_blank(self):
        self.clicked_button_txt = ""


class Button:
    def __init__(self, graphics, caption, x, y):
        self.graphics = graphics

        self.caption = caption

        self.button_img = self.graphics["button.png"]
        self.button_img = pygame.transform.scale(self.button_img, (330, 70))
        self.button_rect = Rect((x - self.button_img.get_width() / 2, y - self.button_img.get_height() / 2), (self.button_img.get_width(), self.button_img.get_height()))

        self.button_state = "OUT"  # OUT, IN, CLICK

        self.font = pygame.font.Font("res/8bitwonder.ttf", 36)
        self.text = self.font.render(self.caption, 1, (10, 10, 10))
        self.text_rect = self.text.get_rect(center=(self.button_img.get_width() / 2 + self.button_rect[0], self.button_img.get_height() / 2 + self.button_rect[1]))

    def event(self, event):
        if event.type == MOUSEMOTION:
            if self.button_state != "CLICK":
                if self.button_rect.collidepoint(event.pos[0], event.pos[1]):
                    self.button_state = "IN"
                else:
                    self.button_state = "OUT"

        if event.type == MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos[0], event.pos[1]):
                self.button_state = "CLICK"

        if event.type == MOUSEBUTTONUP:
            if self.button_rect.collidepoint(event.pos[0], event.pos[1]):
                self.button_state = "IN"
            else:
                self.button_state = "OUT"

    def update(self):
        pass

    def draw(self, menu_render):
        menu_render.blit(self.button_img, self.button_rect)
        menu_render.blit(self.text, self.text_rect)

    def get_button_state(self):
        return self.button_state

    def get_button_txt(self):
        return self.button_txt
