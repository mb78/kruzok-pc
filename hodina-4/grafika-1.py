#!/bin/env python3

# pre zlozitejsi program, pozrite hodina-3/grafika-1.py

import os,sys,pygame,random,time
pygame.font.init()
pygame.mixer.init()

OKNO = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pokus s grafikou")
BIELA = [255, 255, 255]
CIERNA = [0,0,0]

if __name__ == "__main__":
    # lave oko
    obdlznik = pygame.Rect( 250, 250, 20, 30)
    pygame.draw.rect(OKNO, BIELA, obdlznik)
    obdlznik = pygame.Rect( 253, 260, 5, 5)
    pygame.draw.rect(OKNO, CIERNA, obdlznik)

    # prave oko
    obdlznik = pygame.Rect( 280, 250, 20, 30)
    pygame.draw.rect(OKNO, BIELA, obdlznik)
    obdlznik = pygame.Rect( 283, 260, 5, 5)
    pygame.draw.rect(OKNO, CIERNA, obdlznik)

    # usta
    obdlznik = pygame.Rect( 255, 285, 40, 10)
    pygame.draw.rect(OKNO, BIELA, obdlznik)

    pygame.display.update()
    time.sleep(1)
