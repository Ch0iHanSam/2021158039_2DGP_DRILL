from pico2d import *
open_canvas()
character = load_image('de8l5gy-a3fbb8b0-87b4-4758-87d7-7096bee6c492.png')

frame = 0

#달리기
for x in range(0, 4*8, 1):  # 4프레임 짜리를 n번 반복
    clear_canvas()
    character.clip_draw(frame * 48 + 48, 1285, 48, 55, 400, 90)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.1)
    get_events()

#점프
for x in range(0,4*4,1):
    clear_canvas()
    if frame == 0:      #점프 높이 구현
        y=90
    if frame == 1 or frame == 3:
        y=90+20
    if frame == 2:
        y=90+40
    character.clip_draw(frame * 53 + 240, 1280, 53, 60, 400, y)
    update_canvas()
    frame = (frame+1)%4
    delay(0.15)
    get_events()


close_canvas()