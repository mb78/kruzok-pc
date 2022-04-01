import pygame
from game_settings import *

class Rocket:
    def __init__(self,screen,x,y):
        self.screen=screen
        self.x,self.y=x,y
        self.image=pygame.image.load('rocket.png')
        self.image=pygame.transform.rotate(pygame.transform.scale(self.image, (30,60)), 0)
    def blit(self):
        self.screen.blit(self.image,(self.x,self.y))
    def limit_pos(self,v,maxv):
        if (v<0): return 0
        if (v>maxv): return maxv
        return v
    def move(self,velocity_x,velocity_y):
        self.x=self.limit_pos(self.x+velocity_x,WIDTH)
        self.y=self.limit_pos(self.y+velocity_y,HEIGHT)
