import pygame

from pygame.locals import *

import consts as c

class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

class Dialog:
    #def __init__(self, graphics, char_name, text):
    #    self.graphics = graphics

    #    self.big_head = graphics["char_name.png"]

    #    self.text = text

    def __init__(self):
        pass

    def render_textrect(self, string, font, rect, text_color, background_color, justification=0):
        """Returns a surface containing the passed text string, reformatted
        to fit within the given rect, word-wrapping as necessary. The text
        will be anti-aliased.

        Takes the following arguments:

        string - the text you wish to render. \n begins a new line.
        font - a Font object
        rect - a rectstyle giving the size of the surface requested.
        text_color - a three-byte tuple of the rgb value of the
                    text color. ex (0, 0, 0) = BLACK
        background_color - a three-byte tuple of the rgb value of the surface.
        justification - 0 (default) left-justified
                        1 horizontally centered
                        2 right-justified

        Returns the following values:

        Success - a surface object with the text rendered onto it.
        Failure - raises a TextRectException if the text won't fit onto the surface.
        """

        rectwidth_adjust = 200

        final_lines = []

        requested_lines = string.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width-rectwidth_adjust:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width-rectwidth_adjust:
                        print("ERROR")
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.
                    if font.size(test_line)[0] < rect.width-rectwidth_adjust:
                        accumulated_line = test_line
                    else:
                        final_lines.append(accumulated_line)
                        accumulated_line = word + " "
                final_lines.append(accumulated_line)
            else:
                final_lines.append(requested_line)

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        surface.fill(background_color)

        accumulated_height = 0
        for line in final_lines:
            if accumulated_height + font.size(line)[1] >= rect.height:
                print("ERROR")
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (rectwidth_adjust, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width+rectwidth_adjust - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width+rectwidth_adjust - tempsurface.get_width(), accumulated_height))
                else:
                    print("ERROR")
            accumulated_height += font.size(line)[1]

        return surface


    def event(self):
        pass


    def update(self):
        pass


    def draw(self):
        pass


