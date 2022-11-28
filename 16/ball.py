from pico2d import *
import random
import game_world

class Ball:
    def __init__(self, Background):
        self.x, self.y = random.randint(50, Background.w - 50), random.randint(50, Background.h - 50)
        self.background = Background
        self.image = load_image('ball21x21.png')
        self.first = True
        self.window_x, self.window_y = None, None

    def update(self):
        self.window_x = self.x - self.background.window_left
        self.window_y = self.y - self.background.window_bottom

    def draw(self):
        self.image.draw(self.window_x, self.window_y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, a, group):
        a.score += 1
