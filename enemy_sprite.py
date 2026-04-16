import pygame
from random import randint

from config import *
from player_sprite import player_group


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == 'bat':       # adding more caracters
            self.bat = pygame.image.load('Python/Pixel Runner/sources/bat.png').convert_alpha()
            self.enemy = self.bat    
            y_pos = 235
        else:
            self.snail = pygame.image.load('Python/Pixel Runner/sources/pixel-snail.png').convert_alpha()    
            self.enemy = self.snail
            y_pos = 330
        
        
        
        
        self.image = self.enemy 
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
        
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()        
        
    
        
    def update(self):  
        self.destroy()
        self.rect.x -= enemy_mov_speed
        
obstacle_group = pygame.sprite.Group()

def collisions_sprite():
    if pygame.sprite.spritecollide(player_group.sprite,obstacle_group,False):
        obstacle_group.empty()
        
        return False
        
    else: return True