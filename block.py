import pygame as pg
import random as rnd


class Block:
    def __init__(self, x, y, screen, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.color = color

        self.form = pg.Rect(x, y, self.width, self.height)
        self.image = pg.transform.scale(pg.image.load('images/brick.jpg'), (self.form.width, self.form.height)).convert_alpha()

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.form)
        self.screen.blit(self.image, [self.form.x, self.form.y])
