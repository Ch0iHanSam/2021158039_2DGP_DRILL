from pico2d import *
import game_world
import time
import game_framework

#Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 20.0
FLY_SPEED_MPM = FLY_SPEED_KMPH * 1000.0 / 60.0
FLY_SPEED_MPS = FLY_SPEED_MPM / 60.0
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

#Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

#1 : 이벤트 정의
RD, LD, RU, LU = range(4)
event_name = ['RD', 'LD', 'RU', 'LU']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의


class FLY:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    def exit(self, event):
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.dir == -1:
            if self.frame < 5:
                self.image.clip_composite_draw(int(self.frame)*180, 300, 180, 180, 0, 'h', self.x, self.y, 100, 100)
            elif 5 <= self.frame < 10:
                self.image.clip_composite_draw(int(self.frame)*180, 150, 180, 180, 0, 'h', self.x, self.y, 100, 100)
            elif 10 <= self.frame < 14:
                self.image.clip_composite_draw(int(self.frame)*180, 0, 180, 180,0, 'h', self.x, self.y, 100, 100)
        elif self.dir == 1:
            if self.frame < 5:
                self.image.clip_draw(int(self.frame)*180, 300, 180, 180, self.x, self.y, 100, 100)
            elif 5 <= self.frame < 10:
                self.image.clip_draw(int(self.frame)*180, 150, 180, 180, self.x, self.y, 100, 100)
            elif 10 <= self.frame < 14:
                self.image.clip_draw(int(self.frame)*180, 0, 180, 180, self.x, self.y, 100, 100)
        elif self.dir == 0:
            if self.face_dir == 1:
                if self.frame < 5:
                    self.image.clip_draw(int(self.frame) * 180, 300, 180, 180, self.x, self.y, 100, 100)
                elif 5 <= self.frame < 10:
                    self.image.clip_draw(int(self.frame) * 180, 150, 180, 180, self.x, self.y, 100, 100)
                elif 10 <= self.frame < 14:
                    self.image.clip_draw(int(self.frame) * 180, 0, 180, 180, self.x, self.y, 100, 100)
            elif self.face_dir == -1:
                if self.frame < 5:
                    self.image.clip_composite_draw(int(self.frame) * 180, 300, 180, 180, 0, 'h', self.x, self.y, 100,
                                                   100)
                elif 5 <= self.frame < 10:
                    self.image.clip_composite_draw(int(self.frame) * 180, 150, 180, 180, 0, 'h', self.x, self.y, 100,
                                                   100)
                elif 10 <= self.frame < 14:
                    self.image.clip_composite_draw(int(self.frame) * 180, 0, 180, 180, 0, 'h', self.x, self.y, 100, 100)

#3. 상태 변환 구현

next_state = {
    FLY:  {RU: FLY,  LU: FLY,  RD: FLY,  LD: FLY},
}




class Bird:

    def __init__(self, x = 100, y = 100):
        self.x, self.y = x, 7y
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)


        self.timer = 100

        self.event_que = []
        self.cur_state = FLY
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
