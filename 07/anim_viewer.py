from pico2d import *
open_canvas()
character = load_image('de8l5gy-a3fbb8b0-87b4-4758-87d7-7096bee6c492.png')
frame = 0
def run():
    frame = 0
    for x in range(0, 4 * 4, 1):  # 4프레임 짜리를 n번 반복
        clear_canvas()
        character.clip_draw(frame * 48 + 48, 1285, 48, 55, 400, 90)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.1)
        get_events()
def jump():
    frame = 0

    for x in range(0, 4, 1):
        clear_canvas()
        if frame == 0:  # 점프 높이 구현
            y = 90
        if frame == 1 or frame == 3:
            y = 90 + 20
        if frame == 2:
            y = 90 + 40
        character.clip_draw(frame * 53 + 240, 1280, 53, 60, 400, y)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.15)
        get_events()
def hurted():
    frame = 0
    for x in range(0, 4, 1):
        clear_canvas()
        character.clip_draw(frame * 65 + 670, 1285, 65, 55, 400, 90)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.15)
        get_events()
def hurted2():
    frame = 0
    for x in range(0, 1, 1):
        for x in range(0, 10, 1):
            clear_canvas()
            character.clip_draw(frame * 58, 1218, 58, 55, 400 + (x + 1) * 3, 90)
            update_canvas()
            frame = (frame + 1) % 10
            delay(0.1)
            get_events()

        for x in range(0, 8, 1):
            clear_canvas()
            character.clip_draw(frame * 67 + 590, 1218, 67, 55, 433 + (x + 1) * 5, 80)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.1)
            get_events()
def run2():
    frame = 0
    for x in range(0, 4 * 4, 1):
        clear_canvas()
        character.clip_draw(frame * 48 + 1849, 962, 48, 53, 473 - (x + 1) * 4.5, 90)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.1)
        get_events()
def cossack():
    frame = 0
    for x in range(0, 3, 1):
        for x in range(0, 6, 1):
            clear_canvas()
            character.clip_draw(frame * 49 + 1448, 895, 49, 60, 400, 90)
            update_canvas()
            frame = (frame + 1) % 6
            delay(0.1)
            get_events()
        for x in range(4, 0, -1):
            clear_canvas()
            character.clip_draw(x * 49 + 1448, 895, 49, 60, 400, 90)
            update_canvas()
            delay(0.1)
            get_events()
def gun_spin():
    frame = 0
    for x in (0, 1, 1):
        clear_canvas()
        character.clip_draw(1869, 770, 74, 53, 400, 90)
        update_canvas()
        delay(0.08)
        get_events()
        for x in range(0, 3, 1):
            clear_canvas()
            character.clip_draw(frame * 65 + 1943, 770, 65, 53, 400, 90)
            update_canvas()
            frame = (frame + 1) % 3
            delay(0.08)
            get_events()
def gun_shoot():
    def shoot_gun(start_x, start_y, width, height, x, y):
        clear_canvas()
        character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
        update_canvas()
        delay(0.1)
        get_events()
        return

    for x in range(0, 2, 1):
        for start_x, start_y, width, height, x, y in [(1791, 444, 80, 54, 400, 90), (1871, 444, 93, 54, 382, 90),
                                                      (1964, 444, 100, 54, 382, 90), (2064, 444, 63, 54, 400, 90),
                                                      (2132, 444, 64, 54, 400, 90), (2205, 444, 81, 54, 400, 90)]:
            shoot_gun(start_x, start_y, width, height, x, y)
def weaving():
    frame = 0
    clear_canvas()
    character.clip_draw(2358, 832, 48, 51, 400, 90)
    update_canvas()
    delay(0.1)
    get_events()
    for x in range(0, 4, 1):
        clear_canvas()
        character.clip_draw(frame * 48 + 2357, 895, 48, 49, 400, 90)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.3)
        get_events()
def jabandhook():
    def punch(start_x, start_y, width, height, x, y):
        clear_canvas()
        character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
        update_canvas()
        delay(0.1)
        get_events()
        return

    for start_x, start_y, width, height, x, y in [(0, 185, 47, 53, 400, 90), (61, 184, 39, 53, 400, 90),
                                                  (112, 185, 89, 53, 397, 90), (213, 185, 69, 53, 395, 90),
                                                  (291, 185, 62, 53, 395, 90), (358, 185, 59, 53, 398, 90),
                                                  (423, 185, 40, 53, 400, 90)]:
        punch(start_x, start_y, width, height, x, y)
    delay(0.1)

    for start_x, start_y, width, height, x, y in [(4, 249, 44, 51, 400, 90), (59, 249, 54, 51, 400, 90),
                                                  (112, 249, 74, 51, 400, 90), (192, 249, 74, 51, 400, 90),
                                                  (267, 249, 51, 51, 400, 90), (321, 249, 50, 51, 400, 90)]:
        punch(start_x, start_y, width, height, x, y)
    delay(0.1)
def kicks():
    def kickset(start_x, start_y, width, height, x, y):
        clear_canvas()
        character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
        update_canvas()
        delay(0.1)
        get_events()
        return

    for x in [1]:
        for start_x, start_y, width, height, x, y in [(797, 248, 59, 55, 400, 90), (844, 248, 59, 55, 400, 90),
                                                      (907, 248, 59, 55, 400, 90), (992, 248, 59, 55, 400, 90),
                                                      (1068, 248, 59, 55, 400, 90), (1140, 248, 59, 55, 400, 90),
                                                      (1198, 248, 59, 55, 400, 90), (1256, 248, 59, 55, 400, 90),
                                                      (1310, 248, 59, 55, 400, 90), (1361, 248, 59, 55, 400, 90),
                                                      (3, 332, 47, 70, 400, 81), (51, 332, 58, 70, 400, 81),
                                                      (110, 332, 87, 70, 400, 81),
                                                      (203, 332, 67, 70, 400, 81), (273, 332, 69, 70, 400, 81),
                                                      (345, 332, 69, 70, 400, 81), (416, 332, 69, 70, 400, 81),
                                                      (486, 332, 60, 70, 400, 81),
                                                      (545, 332, 60, 70, 400, 81), (605, 332, 77, 70, 408, 81),
                                                      (687, 332, 70, 70, 400, 81), (764, 332, 62, 70, 400, 81),
                                                      (829, 332, 62, 70, 400, 81),
                                                      (896, 332, 63, 70, 400, 81), (956, 332, 46, 70, 400, 81),
                                                      (1005, 332, 51, 70, 400, 90), (1063, 332, 71, 70, 400, 100),
                                                      (1140, 332, 72, 70, 400, 110), (1213, 332, 64, 70, 400, 110),
                                                      (1278, 332, 66, 70, 400, 110), (949, 389, 49, 56, 400, 100),
                                                      (1002, 389, 83, 56, 400, 100), (1085, 389, 69, 56, 400, 96),
                                                      (1168, 389, 52, 56, 400, 94), (1232, 389, 53, 56, 400, 92)]:
            kickset(start_x, start_y, width, height, x, y)
def uppercut():
    def soryugen(start_x, start_y, width, height, x, y):
        clear_canvas()
        character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
        update_canvas()
        delay(0.1)
        get_events()
        return

    for x in range(2):
        for start_x, start_y, width, height, x, y in [(9, 576, 45, 69, 400, 90), (62, 576, 45, 69, 400, 90),
                                                      (111, 576, 45, 69, 400, 100), (154, 576, 45, 69, 400, 105),
                                                      (196, 576, 45, 69, 400, 110)
            , (242, 576, 45, 69, 400, 115), (288, 576, 45, 69, 400, 120), (333, 576, 45, 67, 400, 110),
                                                      (378, 576, 45, 67, 400, 100)
            , (427, 576, 45, 65, 400, 90), (474, 576, 45, 65, 400, 90)]:
            soryugen(start_x, start_y, width, height, x, y)
def energy():
    def ki(start_x, start_y, width, height, x, y):
        clear_canvas()
        character.clip_draw(start_x, 1340 - start_y, width, height, x, y)
        update_canvas()
        delay(0.1)
        get_events()
        return

    for start_x, start_y, width, height, x, y in [(10, 645, 43, 63, 400, 90), (55, 645, 59, 63, 400, 90),
                                                  (114, 645, 59, 63, 400, 90), (177, 645, 59, 63, 400, 90),
                                                  (241, 645, 59, 63, 400, 90),
                                                  (303, 645, 59, 63, 400, 90), (365, 645, 59, 63, 400, 90),
                                                  (431, 645, 59, 63, 400, 90), (497, 645, 59, 63, 400, 90),
                                                  (562, 645, 59, 63, 400, 90)
        , (627, 645, 59, 63, 400, 90), (691, 645, 59, 63, 400, 90), (757, 645, 59, 63, 400, 90),
                                                  (823, 645, 59, 63, 400, 90), (888, 645, 59, 63, 400, 90)
        , (955, 645, 59, 63, 400, 90), (1021, 645, 59, 63, 400, 90), (1085, 645, 59, 63, 400, 90)]:
        ki(start_x, start_y, width, height, x, y)

while True:
    run()#달리기
    jump()#점프
    hurted()#피격
    hurted2()#피격
    run2()#달리기2
    cossack()#코사크 댄스
    gun_spin()#총돌리기
    gun_shoot() #총쏘기
    weaving()  #대기
    jabandhook() #잽, 훅
    kicks()#발차기(로우킥, 뒤돌려차기, 공중돌려차기, 착지)
    uppercut()#어퍼컷
    energy()#명상

close_canvas()