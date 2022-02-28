#!/bin/env python3

import os,sys,pygame,random
pygame.font.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=500
SCREEN=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pokus s grafikou")

FPS = 60

IMAGE = pygame.image.load('obloha1.jpg')
IMAGE=pygame.transform.rotate(pygame.transform.scale(IMAGE, (WIDTH,HEIGHT)), 0)

def main():
    yellow_bullets = []
    bullet = pygame.Rect( 250,250, 5, 5)
    yellow_bullets.append(bullet)
    clock = pygame.time.Clock()
    run = True
    x=0
    y=0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # koniec pri stlaceni klavesu 'q' (s alebo bez shiftu)
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
        SCREEN.blit(IMAGE, (0,0))
        x=(x+4)%WIDTH
        y=(y+3)%HEIGHT
        pygame.draw.circle(SCREEN, (100,100,100), (x,y), 10)
        pygame.draw.circle(SCREEN, (200,200,200), (x+100,y), 5)
        pygame.display.update()

if __name__ == "__main__":
    main()
