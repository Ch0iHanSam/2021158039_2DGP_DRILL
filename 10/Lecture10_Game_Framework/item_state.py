from pico2d import *
import game_framework
import play_state
import title_state

# fill here
# running = True
image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('item_select.png')

def exit():
    # fill here
    global image
    del image
    pass

def update():
    play_state.update()
    pass


def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state() # 이전 상태인 play_state로 복귀
                case pico2d.SDLK_1:
                    for i in range(len(play_state.boy)):
                        play_state.boy[i].item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    for i in range(len(play_state.boy)):
                        play_state.boy[i].item = 'BigBall'
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    for i in range(len(play_state.boy)):
                        play_state.boy[i].item = None
                    game_framework.pop_state()





