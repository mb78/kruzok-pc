#!/bin/env python3

import os,sys,pygame,random
pygame.font.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pokus s grafikou")

FPS = 30

IMAGE = pygame.image.load('obloha3.jpg')
IMAGE=pygame.transform.rotate(pygame.transform.scale(IMAGE, (WIDTH,HEIGHT)), 0)

s=pygame.image.load('vlocka.png')
SNOWFLAKE=pygame.transform.rotate(pygame.transform.scale(s, (50,50)), 0)
SNOWFLAKES=[]

def main():
    yellow_bullets = []
    bullet = pygame.Rect( 250,250, 5, 5)
    yellow_bullets.append(bullet)
    clock = pygame.time.Clock()
    run = True
    iteracia=0
    x,y=100,100
    VEL=5
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # koniec pri stlaceni klavesu 'q' (s alebo bez shiftu)
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT] and x-VEL>0:
            x -= VEL
        if keys_pressed[pygame.K_RIGHT] and x+VEL<WIDTH:
            x += VEL
        if keys_pressed[pygame.K_UP] and y-VEL>0:
            y -= VEL
        if keys_pressed[pygame.K_DOWN] and y+VEL<HEIGHT:
            y += VEL
        if keys_pressed[pygame.K_SPACE]:
            SNOWFLAKES.append( (x,y) )
        SCREEN.blit(IMAGE, (0,0))
        SCREEN.blit(SNOWFLAKE, (x,y))
        for s in SNOWFLAKES:
            SCREEN.blit(SNOWFLAKE,s)
        pygame.display.update()

if __name__ == "__main__":
    main()
