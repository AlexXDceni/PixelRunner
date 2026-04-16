import pygame

from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Python/Pixel Runner/sources/pixel-knight-right.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom = (80,330))
        self.initial_pos = (80,330)
        self.gravity = 0
        self.direction = 0
        self.facing_right = True
        
        self.sound_jump = pygame.mixer.Sound('Python/Pixel Runner/sources/jump.mp3')
        self.sound_jump.set_volume(0.02)
        # self.reset_location()
        
    def player_input(self):
        keysd = pygame.key.get_pressed()
        if (keysd[pygame.K_SPACE] or keysd[pygame.K_w]) and self.rect.bottom >= 300:
            self.gravity = -20
            self.sound_jump.play()
            
        if (keysd[pygame.K_a] or keysd[pygame.K_LEFT]) and self.rect.left >= 0:
            self.direction = -5
            self.facing_right = False 
            
        if (keysd[pygame.K_d] or keysd[pygame.K_RIGHT]) and self.rect.left <= 800:
            self.direction = 5 
            self.facing_right = True 
             
        if not(keysd[pygame.K_a] or keysd[pygame.K_d]):
            self.direction = 0
    
    def player_animation(self):
        if self.facing_right == True:
            self.image = pygame.image.load('Python/Pixel Runner/sources/pixel-knight-right.png').convert_alpha()
        else:
            self.image = pygame.image.load('Python/Pixel Runner/sources/pixel-knight-left.png').convert_alpha()
        
    def apply_gravity(self):
        self.gravity +=1
        self.rect.y += self.gravity
        if self.rect.bottom >= 330: self.rect.bottom = 330 
    
    def player_movement(self):
        self.rect.x += self.direction
        if self.rect.left <= 0: self.rect.left = 0
        if self.rect.right >= 800: self.rect.right = 800
        
    def reset_location(self):
        self.rect.x = 80
        self.rect.bottom = 330

    
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_movement()
        self.player_animation()
        
        
player_group = pygame.sprite.GroupSingle()
