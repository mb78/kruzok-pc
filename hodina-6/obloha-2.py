#!/bin/env python3

import os,sys,pygame,random
pygame.font.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pokus s grafikou")

FPS = 30

IMAGE = pygame.image.load('obloha1.jpg')
IMAGE=pygame.transform.rotate(pygame.transform.scale(IMAGE, (WIDTH,HEIGHT)), 0)

SNOWFLAKES=[]
for i in range(5,20):
    s=pygame.image.load('vlocka.png')
    SNOWFLAKES.append(pygame.transform.rotate(pygame.transform.scale(s, (i*2,i*2)), 0))

def hviezda(iteracia,x0):
    farba=hash(str(x0)) % 255
    rychlost=1+(farba%10)
    x=x0 + (iteracia*rychlost % WIDTH)
    y=(iteracia*rychlost % HEIGHT)
    velkost=farba%len(SNOWFLAKES)
    SCREEN.blit(SNOWFLAKES[velkost], (x,y))
    return 

def main():
    yellow_bullets = []
    bullet = pygame.Rect( 250,250, 5, 5)
    yellow_bullets.append(bullet)
    clock = pygame.time.Clock()
    run = True
    iteracia=0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # koniec pri stlaceni klavesu 'q' (s alebo bez shiftu)
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
        SCREEN.blit(IMAGE, (0,0))
        iteracia+=1
        for i in range(0,20):
            hviezda(iteracia,i*10)
        pygame.display.update()

if __name__ == "__main__":
    main()
