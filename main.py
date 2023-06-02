import pygame as pg
from random import randrange as rnd

from ball import Ball
from block import Block
from paddle import Paddle


class Game:
    def __init__(self, window_size):
        pg.init()
        self.screen_width = window_size[0]
        self.screen_height = window_size[1]
        self.screen = pg.display.set_mode(window_size)
        self.clock = pg.time.Clock()
        self.running = True
        self.background_image = pg.transform.scale(pg.image.load('images/bg.jpg'), window_size).convert()

        # Init Paddle
        self.paddle = Paddle(0, 0, self.screen)
        self.paddle.set_x(window_size[0] // 2 - self.paddle.width // 2)
        self.paddle.set_y(window_size[1] - self.paddle.height - 10)

        # Init ball
        self.ball = Ball(100, 100, self.screen)

        # Init blocks
        self.num_blocks_horizontal = 10
        self.num_blocks_vertical = 5
        self.block_spacing = 10

        self.block_width = (self.screen_width - self.num_blocks_horizontal*self.block_spacing - self.block_spacing * 2) // self.num_blocks_horizontal
        self.block_height = 30
        self.blocks = [Block(
            self.block_spacing*i+self.block_width*i,
            self.block_spacing*j+self.block_height*j,
            self.screen,
            self.block_width,
            self.block_height,
            (rnd(30, 256), rnd(30, 256), rnd(30, 256))) for i in range(1, self.num_blocks_horizontal) for j in range(1, 5)
        ]
        self.blocks_rects = [block.form for block in self.blocks]

        self.main_loop()

    def detect_collision(self, ball, block):
        if ball.dx > 0:
            delta_x = ball.form.right - block.left
        else:
            delta_x = block.right - ball.form.left

        if ball.dy > 0:
            delta_y = ball.form.bottom - block.top
        else:
            delta_y = block.bottom - ball.form.top

        if abs(delta_x - delta_y) < 10:
            ball.dx, ball.dy = -ball.dx, -ball.dy
        elif delta_x > delta_y:
            ball.dy = -ball.dy
        elif delta_x < delta_y:
            ball.dx = -ball.dx
        return ball.dx, ball.dy

    def main_loop(self):

        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            key = pg.key.get_pressed()
            if key[pg.K_LEFT] and self.paddle.form.left > 0:
                self.paddle.form.x -= 1 * self.paddle.velocity
            if key[pg.K_RIGHT] and self.paddle.form.right < self.screen_width:
                self.paddle.form.x += 1 * self.paddle.velocity

            # Draw Background
            self.screen.blit(self.background_image, [0, 0])

            # Draw paddle
            self.paddle.draw_paddle()

            # Draw ball
            self.ball.form.x += self.ball.speed * self.ball.dx
            self.ball.form.y += self.ball.speed * self.ball.dy

            # Wall collision
            if self.ball.form.centerx - self.ball.radius < 0:
                self.ball.dx = 1
            if self.ball.form.centerx + self.ball.radius > self.screen_width:
                self.ball.dx = -1
            if self.ball.form.centery - self.ball.radius < 0:
                self.ball.dy = -self.ball.dy
            # Paddle collision
            if self.ball.form.colliderect(self.paddle.form) and self.ball.dy > 0:
                self.ball.dy = -self.ball.dy

            # Block collision
            hit_index = self.ball.form.collidelist(self.blocks_rects)
            if hit_index != -1:
                hit_rect = self.blocks_rects.pop(hit_index)
                self.blocks.pop(hit_index)
                self.ball.dx, self.ball.dy = self.detect_collision(self.ball, hit_rect)

                # Special Effects
                hit_rect.inflate_ip(self.ball.form.width * 2, self.ball.form.height * 2)
                pg.draw.rect(self.screen, pg.Color('red'), hit_rect)

                # Increase ball speed
                self.ball.speed += 0.05

            self.ball.draw()

            # Draw blocks
            for block in self.blocks:
                block.draw()

            if self.ball.form.bottom > self.screen_height:
                print('GAME OVER!')
                self.running = False
            elif not len(self.blocks):
                print('You WIN!!!')
                self.running = False

            pg.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pg.quit()


if __name__ == '__main__':
    app = Game((800, 600))
