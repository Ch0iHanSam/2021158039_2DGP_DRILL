from pico2d import *
import play_state
import logo_state

start_state = logo_state  #모듈을 변수로 취급
open_canvas()

states = [logo_state, play_state]
for state in states:
    state.enter()
    while state. running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()

# finalization code
close_canvas()