from pico2d import *
import random
import game_world

class Ball:
    def __init__(self, Background):
        self.x, self.y = random.randint(50, Background.w-50), random.randint(50, Background.h-50)
        self.background = Background
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x = self.background.h - self.background.canvas_width-1

    def draw(self):
        if self.background.window_left < self.x < self.background.window_left + self.background.canvas_width-1 and self.background.window_bottom < self.y < self.background.window_bottom + self.background.canvas_height-1:
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, a, group):
        a.score += 1
