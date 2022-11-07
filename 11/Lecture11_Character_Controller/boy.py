from pico2d import *


class IDLE:
    @staticmethod
    def enter(self, event): # RUN에서 event를 받으니까 상태간 원활한 전환을 위해 사용하지 않지만 event 인수를 받는다(함수를 똑같이 쓰니까 오류 안나게끔)
        print('Enter IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)



class RUN:
    @staticmethod
    def enter(self, event):
        print('Enter RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class SLEEP:
    @staticmethod
    def enter(self, event): # RUN에서 event를 받으니까 상태간 원활한 전환을 위해 사용하지 않지만 event 인수를 받는다(함수를 똑같이 쓰니까 오류 안나게끔)
        print('Enter SLEEP')

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8

    @staticmethod
    def draw(self):
        if self.face_dir == -1:  # 왼쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x, self.y-30, 100, 100)
        else:  # 오른쪽 눕기
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x, self.y-30, 100, 100)


class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print('Enter AUTO_RUN')
        if self.dir == 0:
            self.dir = self.face_dir


    @staticmethod
    def exit(self):
        print('EXIT AUTO_RUN')
        self.face_dir = self.dir
        self.dir = 0

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x == 0:
            self.dir += 2
        elif self.x == 800:
            self.dir -= 2


    @staticmethod
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y+30, 200, 200)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y+30, 200, 200)


#이벤트 정의
# RD, LD, RU, LU, TIMER, AD = 0, 1, 2, 3, 5, 6
RD, LD, RU, LU, TIMER, AD = range(6)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : AD
}


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    AUTO_RUN: {RU: AUTO_RUN, LU: AUTO_RUN, RD: RUN, LD: RUN, AD: IDLE}
}
class Boy:
    def __init__(self):
        self.x, self.y = 800//2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.timer = 1000

        self.event_que = [] # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter(self, None) # 초기 상태의 entry 액션 수행


    def update(self):
        self.cur_state.do(self) # 현재 상태의 do 액션 수행

        # 이벤트 확인해서(이벤트가 발생했으면), 이벤트가 있으면 이벤트  변환 처리
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self) # 현재의 상태에 나가야 하고
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
