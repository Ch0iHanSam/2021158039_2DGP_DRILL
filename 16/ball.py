from pico2d import *
import random
from background import FixedBackground as Background

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, Background.w-50), random.randint(50, Background.h - 50)
        self.image = load_image('ball21x21.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x,self.y)