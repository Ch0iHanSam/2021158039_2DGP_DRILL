from pico2d import *
open_canvas()
character = load_image('de8l5gy-a3fbb8b0-87b4-4758-87d7-7096bee6c492.png')

"""
크기 같을 경우
frame = 0
for x in range(0, 프레임수*3, 1):
    clear_canvas()
    character.clip_draw(frame * 가로 + 시작x, 1340-시작y, 가로, 세로, 400, 90)
    update_canvas()
    frame = (frame + 1) % 프레임수
    delay(0.1)
    get_events()

크기 다를 경우
(하다보니까 이렇게 됐는데 실제로 쓸 때에는 함수는 하나만 만드는게 메모리 절약에 훨씬 도움 될듯 하다. 형태 똑같은데 함수를 너무 많이 만들었다.)
def 함수이름(start_x, start_y, width, height, x, y):
    clear_canvas()
    character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
    update_canvas()
    delay(0.1)
    get_events()
    return


for x in range(원하는 횟수):
    for start_x, start_y, width, height, x, y in [(맞춰서 적기)]:
        함수이름(start_x, start_y, width, height, x, y)
"""





close_canvas()