import pygame as pg
import random as rnd


class Ball:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.color = pg.Color('red')
        self.radius = 20.0
        self.dx = 1
        self.dy = -1
        self.speed = 2
        self.rect = int(self.radius * 2 ** 0.5)
        self.form = pg.Rect(self.x, self.y, self.rect, self.rect)
        self.image = pg.transform.scale(pg.image.load('images/ball.png'), (self.rect, self.rect)).convert_alpha()

    def draw(self):
        pg.draw.circle(self.screen, self.color, self.form.center, self.radius)
        self.screen.blit(self.image, [self.form.x, self.form.y])
