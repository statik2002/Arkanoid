import pygame as pg


class Paddle:
    def __init__(self, x, y, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 150
        self.height = 20
        self.speed = 25
        self.color = pg.Color('darkorange')
        self.form = pg.Rect(x, y, self.width, self.height)
        self.velocity = 5

    def draw_paddle(self):
        pg.draw.rect(self.screen, self.color, self.form)

    def set_x(self, x):
        self.x = x
        self.form = pg.Rect(self.x, self.y, self.width, self.height)

    def set_y(self, y):
        self.y = y
        self.form = pg.Rect(self.x, self.y, self.width, self.height)

