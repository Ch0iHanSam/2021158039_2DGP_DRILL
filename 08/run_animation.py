from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
dir = 300
running = True
x = 800//2
y = 150
frame = 0
move = 'idle'


def handle_events():
    global running
    global dir
    global x
    global y
    global move
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir = 300
            elif event.key == SDLK_LEFT:
                dir = 200
            move = 'idle'
        if event.type == SDL_KEYDOWN or move != 'idle':
            if event.key == SDLK_RIGHT or move == 'right':
                move = 'right'
                dir = 100
                x = x + 10
            elif event.key == SDLK_LEFT or move == 'left':
                move = 'left'
                dir = 0
                x = x - 10
            elif event.key == SDLK_UP or move == 'up':
                move = 'up'
                y = y + 10
            elif event.key == SDLK_DOWN or move == 'down':
                move = 'down'
                y = y - 10


while running:
    clear_canvas()
    grass.draw(400,300,800,600)


    if x > 30 and x < 770 and y > 30 and y < 570:
        character.clip_draw(frame * 100, dir, 100, 100, x, y)
    elif x == 30 and y <= 30:
        x = 30
        y = 30
        character.clip_draw(frame * 100, dir, 100, 100, 30, 30)
    elif x == 770 and y <= 30:
        x = 770
        y = 30
        character.clip_draw(frame * 100, dir, 100, 100, 770, 30)
    elif x == 770 and y >= 570:
        x = 770
        y = 570
        character.clip_draw(frame * 100, dir, 100, 100, 770, 570)
    elif x == 30 and y >= 570:
        x = 30
        y = 570
        character.clip_draw(frame * 100, dir, 100, 100, 30, 570)
    elif x <= 30:
        x = 30
        character.clip_draw(frame * 100, dir, 100, 100, 30, y)
    elif x >= 770:
        x = 770
        character.clip_draw(frame * 100, dir, 100, 100, 770, y)
    elif y <= 30:
        y = 30
        character.clip_draw(frame * 100, dir, 100, 100, x, 30)
    elif y >= 570:
        y = 570
        character.clip_draw(frame * 100, dir, 100, 100, x, 570)

    update_canvas()

    handle_events()
    frame = (frame+1)%8

    delay(0.01)

close_canvas()