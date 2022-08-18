#!/bin/env python3

import os,sys,pygame,random
pygame.font.init()
pygame.mixer.init()

# OKNO je WINDOW v anglictine
OKNO = pygame.display.set_mode((500,500))

# nastavenie titulku okna
pygame.display.set_caption("Pokus s grafikou")

# BIELA je "WHITE v anglictine
BIELA = [255, 255, 255]

# CIERNA je "BLACK" v anglictine
CIERNA = [0, 0, 0]

NAHODNA_FARBA = [0, 0, 200]

# OKRAJ je "BORDER" v anglictine
OKRAJ = pygame.Rect(250, 250, 10, 500)

FPS = 60

def main():
    yellow_bullets = []
    bullet = pygame.Rect( 250,250, 5, 5)
    yellow_bullets.append(bullet)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
        bullet.y = max(0,bullet.y+random.randint(-5,5))
        bullet.x = max(0,bullet.x+random.randint(-5,5))
        NAHODNA_FARBA[0]=random.randint(50,100)
        NAHODNA_FARBA[1]=random.randint(100,255)
        NAHODNA_FARBA[2]=random.randint(200,255)
        for bullet in yellow_bullets:
            pygame.draw.rect(OKNO, NAHODNA_FARBA, bullet)
        pygame.display.update()

if __name__ == "__main__":
    main()
