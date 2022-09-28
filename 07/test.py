from pico2d import *
open_canvas()
character = load_image('de8l5gy-a3fbb8b0-87b4-4758-87d7-7096bee6c492.png')

frame = 0

for x in range(0,16,1):
    clear_canvas()
    character.clip_draw(frame * 53 + 240, 1280, 53, 60, 400, y)
    update_canvas()
    frame = (frame+1)%4
    delay(0.15)
    get_events()

close_canvas()