import pygame
from game_settings import *

class Jetplane:
    def __init__(self, screen):
        self.screen=screen
        self.x=0
        self.image=pygame.image.load('mig.png')
        self.image=pygame.transform.rotate(pygame.transform.scale(self.image, (160,40)), 0)
        self.direction_right=False
        self.explosion_sound = pygame.mixer.Sound("bomb-falling-and-exploding-02.mp3")
    def blit(self):
        self.screen.blit(self.image,(self.x,0))
    def move(self,velocity):
        self.x+=velocity
        if (self.x<0):
            self.x=0
        if (self.x>WIDTH):
            self.x=WIDTH
        if (self.direction_right and velocity<0):
            self.image=pygame.transform.flip(self.image,True,False)
            self.direction_right=False
        if (not self.direction_right and velocity>0):
            self.image=pygame.transform.flip(self.image,True,False)
            self.direction_right=True
