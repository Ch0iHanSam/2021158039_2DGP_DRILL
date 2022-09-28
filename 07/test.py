from pico2d import *
open_canvas()
character = load_image('de8l5gy-a3fbb8b0-87b4-4758-87d7-7096bee6c492.png')

frame = 0
for x in range(0,4,1):
    for x in range(0,10,1):
        clear_canvas()
        character.clip_draw(frame * 58, 1218, 58, 55, 400+(x+1*3), 90)
        update_canvas()
        frame = (frame+1)%10
        delay(0.1)
        get_events()

    for x in range(0, 8, 1):
        clear_canvas()
        character.clip_draw(frame * 67 + 590, 1218, 67, 55, 433+(x+1)*5, 90)
        update_canvas()
        frame = (frame+1)%8
        delay(0.1)
        get_events()

close_canvas()