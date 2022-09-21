from pico2d import *
import math

def character_move(x,y,r_x,move):
    while(move=='rectangular'):
        while(x>=400 and x<800 and y==90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x+2
            delay(0.01)
        while(x==800 and y<600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y+2
            delay(0.01)
        while(x>0 and x<=800 and y==600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x-2
            delay(0.01)
        while(x==0 and y>90 and y<=600):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            y=y-2
            delay(0.01)
        while(x<400 and y==90):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(x,y)
            x=x+2
        if(x==400):
            move='circle'
            delay(0.01)

    while(move =='circle'):
        while(r_x>=270 and r_x<360):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+200*(math.cos(r_x/360*2*math.pi)), 290+200*(math.sin(r_x/360*2*math.pi)))
            r_x+=1
            delay(0.01)
        while(r_x>=360 or (r_x>=0 and r_x<90)):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+200*(math.cos(r_x/360*2*math.pi)), 290+200*(math.sin(r_x/360*2*math.pi)))
            r_x+=1
            delay(0.01)
        while(r_x>=90 and r_x<180):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+200*(math.cos(r_x/360*2*math.pi)), 290+200*(math.sin(r_x/360*2*math.pi)))
            r_x+=1
            delay(0.01)
        while(r_x>=180 and r_x<270):
            clear_canvas_now()
            grass.draw_now(400,30)
            character.draw_now(400+200*(math.cos(r_x/360*2*math.pi)), 290+200*(math.sin(r_x/360*2*math.pi)))
            r_x+=1
            print(r_x)
            if(r_x == 270):
                move = 'rectangular'
            delay(0.01)

    
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
r_x=270

move = 'rectangular'

while(True):
    character_move(x,y,r_x,move)
        
close_canvas()
    

