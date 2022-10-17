from pico2d import *
import game_framework
import logo_state
import title_state
import item_state
import plusminus_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.bigball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 2
        if self.x > 800:
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)
        elif self.item == 'BigBall':
            self.bigball_image.draw(self.x+10, self.y+50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(plusminus_state)



boy = None
grass = None
# running = True

#초기화
def enter():
    global boy
    global grass
    global running
    boy = [Boy() for i in range(1)]
    grass = Grass()
    running = True

def plus():
    boy.append(Boy())

def minus():
    boy.pop(0)

#종료
def exit():
    global boy, grass
    del boy
    del grass

#월드에 존재하는 객체들을 업데이트
def update():
    for character in boy:
        character.update()
    delay(0.001)
    #grass 는 update 필요없으니 생략

#월드를 그린다
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for character in boy:
        character.draw()


def pause():
    pass

def resume():
    pass