#!/bin/env python3

import os,sys,pygame,random,time
pygame.font.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hodina-8")

FPS = 50

IMAGE = pygame.image.load('obloha3.jpg')
IMAGE=pygame.transform.rotate(pygame.transform.scale(IMAGE, (WIDTH,HEIGHT)), 0)

LOPTA=pygame.image.load('ball.png')
LOPTA=pygame.transform.rotate(pygame.transform.scale(LOPTA, (30,30)), 0)

UFO=pygame.image.load('ufo.png')
UFO=pygame.transform.rotate(pygame.transform.scale(UFO, (100,60)), 0)

KYBEL=pygame.image.load('bucket.png')
KYBEL=pygame.transform.rotate(pygame.transform.scale(KYBEL, (100,80)), 0)

LOPTY=[]

def main():
    clock = pygame.time.Clock()
    run = True
    x,x1=500,500
    VEL=5
    cas_hodu=0
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
        if keys_pressed[pygame.K_a] and x1-VEL>0:
            x1 -= VEL
        if keys_pressed[pygame.K_d] and x1+VEL<WIDTH:
            x1 += VEL
        if keys_pressed[pygame.K_SPACE]:
            if (time.time()-cas_hodu>0.5):
                LOPTY.append([x+40,40])
                cas_hodu=time.time()
        SCREEN.blit(IMAGE, (0,0))
        SCREEN.blit(UFO,(x,0))
        SCREEN.blit(KYBEL,(x1,HEIGHT-80))
        for l in LOPTY:
            SCREEN.blit(LOPTA,l)
            l[1]+=10
        pygame.display.update()

if __name__ == "__main__":
    main()
