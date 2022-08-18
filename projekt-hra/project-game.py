#!/bin/env python3

import os,sys,pygame,random,time
from game_settings import *
from jetplane import *
from tank import *
from rocket import *

pygame.font.init()
pygame.mixer.init()

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Projekt hra")

background=pygame.image.load('background.jpg')
background=pygame.transform.rotate(pygame.transform.scale(background,(WIDTH,HEIGHT)),0)

color_white=(255,255,255)
font_size40=pygame.font.SysFont('comicsans',40)
def blit_text(text,x=100,y=100,font=font_size40):
    draw_text = font.render(text,1,color_white)
    # draw_text.get_width / draw_text.get_height
    screen.blit(draw_text,(x,y))

def blit_backgound():
    screen.blit(background, (0,0))

run = True
def stop_game():
    run=False
    pygame.quit()

score_launched=0
score_hits=0
def launch_rocket():
    global last_rocket_launch_ts,score_launched
    if (time.time()-last_rocket_launch_ts>0.5):
        if (jetplane.direction_right):
            velocity_x=VELOCITY_JETPLANE
        else:
            velocity_x=-VELOCITY_JETPLANE
        rockets.append(Rocket(screen,jetplane.x+80,30,velocity_x))
        last_rocket_launch_ts=time.time()
        score_launched+=1

rockets=[]
last_rocket_launch_ts=0
jetplane=Jetplane(screen)
jetplane.move(3*WIDTH/4)
tank=Tank(screen)
tank.move(WIDTH/4)
def handle_key_event():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                stop_game()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        jetplane.move(-VELOCITY_JETPLANE)
    if keys_pressed[pygame.K_RIGHT]:
        jetplane.move(VELOCITY_JETPLANE)
    if keys_pressed[pygame.K_a]:
        tank.move(-VELOCITY_TANK)
    if keys_pressed[pygame.K_d]:
        tank.move(VELOCITY_TANK)
    if keys_pressed[pygame.K_SPACE]:
        launch_rocket()

def main():
    global rockets,score_hits
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        try: handle_key_event()
        except pygame.error: break
        blit_backgound()
        blit_text("SCORE",x=10,y=HEIGHT//2-40)
        blit_text("  jetplane %d" % score_hits,x=10,y=HEIGHT//2)
        blit_text("  tank %d" % score_launched,x=10,y=HEIGHT//2+40)
        jetplane.blit()
        tank.blit()
        del_rockets=[]
        i=0
        for rocket in rockets:
            rocket.move(0,VELOCITY_ROCKET)
            rocket.blit()
            if (rocket.y>=HEIGHT):
                del_rockets.append(i)
            i+=1
            if ( abs(tank.x+30-rocket.x)<50 and rocket.y>HEIGHT-20):
                blit_text("BOOM",x=rocket.x,y=HEIGHT-80)
                tank.explode()
                score_hits+=1
                break
        for i in del_rockets:
            del rockets[i]
        if (tank.exploded):
            rockets=[]
            tank.restart()
        pygame.display.update()

if __name__ == "__main__":
    main()
