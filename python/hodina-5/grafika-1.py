#!/bin/env python3

import os,sys,pygame,random
pygame.font.init()
pygame.mixer.init()

SCREEN=pygame.display.set_mode((800,500))
pygame.display.set_caption("Pokus s grafikou")

# zelena farba - najvacsie cislo je pre zelenu, 100 je pre cervenu, 101 pre modru
COLOR_SCREEN=(100,150,101)
SCREEN.fill(COLOR_SCREEN)

# priblizny pocet prekresleni v cykle "while run:" za sekundu
FPS = 10

def postava(x,y,farba):
    global SCREEN
    # prekreslenie pozadia
    SCREEN.fill(COLOR_SCREEN)
    # hlava
    pygame.draw.rect(SCREEN, farba, (x+20, y, 10, 12))
    # lava ruka
    pygame.draw.line(SCREEN, farba, (x, y), (x+15, y+15) )
    # prava ruka
    pygame.draw.line(SCREEN, farba, (x+50, y), (x+35, y+15) )
    # telo
    pygame.draw.rect(SCREEN, farba, (x+15, y+15, 20, 20))
    # lava noha
    pygame.draw.line(SCREEN, farba, (x+5, y+60), (x+15, y+35) )
    # prava noha
    pygame.draw.line(SCREEN, farba, (x+45, y+60), (x+35, y+35) )

def main():
    yellow_bullets = []
    bullet = pygame.Rect( 250,250, 5, 5)
    yellow_bullets.append(bullet)
    clock = pygame.time.Clock()
    run = True
    x=400
    y=250
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # koniec pri stlaceni klavesu 'q' (s alebo bez shiftu)
                if event.key == pygame.K_q:
                    run = False
                    pygame.quit()
        # nahodne posunieme orientacny bod pre vykreslovanie o bod hore/dole/doprava/dolava
        x+=random.randint(-1,1)*10
        y+=random.randint(-1,1)*10
        # biela farba - vsetky cisla su na najvyssej hodnote
        farba=(255,255,255)
        # vykreslenie postavy zavolanim funkcie
        postava(x,y,farba)
        # a prekreslenie obrazovky
        pygame.display.update()

if __name__ == "__main__":
    main()
