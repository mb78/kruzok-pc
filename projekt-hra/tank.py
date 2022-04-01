import pygame,time
from game_settings import *

class Tank:
    def __init__(self, screen):
        self.screen=screen
        self.x=0
        self.exploded=False
        self.exploded_time=0
        self.image=pygame.image.load('tank.png')
        self.image=pygame.transform.rotate(pygame.transform.scale(self.image, (100,60)), 0)
        self.image_explosion=pygame.image.load('explosion.png')
        self.image_explosion=pygame.transform.rotate(pygame.transform.scale(self.image_explosion, (150,120)), 0)
        self.explosion_sound = pygame.mixer.Sound("explosion-01.wav")

    def blit(self):
        if (self.exploded):
            self.screen.blit(self.image_explosion,(self.x,HEIGHT-120))
        else:
            self.screen.blit(self.image,(self.x,HEIGHT-60))
    def move(self,velocity):
        self.x+=velocity
        if (self.x<0):
            self.x=0
        if (self.x>WIDTH):
            self.x=WIDTH
    def explode(self):
        self.exploded=True
        self.exploded_time=time.time()
        pygame.mixer.Sound.play(self.explosion_sound)
        pygame.mixer.music.stop()
    def restart(self):
        if (time.time()-self.exploded_time>1):
            self.exploded=False
