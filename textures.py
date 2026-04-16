import pygame
from config import *
from game_states import *


pygame.init()


# WINDOW

screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
# ,pygame.RESIZABLE

screen_width = pygame.display.get_surface().get_width() 
screen_height = pygame.display.get_surface().get_height()

program_Icon = pygame.image.load('Python/Pixel Runner/sources/pixel-knight-right.png')
pygame.display.set_icon(program_Icon)
pygame.display.set_caption('Pixel Runner')



# BACKGROUND 

sky_surface = pygame.Surface((800,400))
sky_surface.fill('lightblue')

ground_surface = pygame.Surface((800,50))
ground_surface = pygame.image.load('Python/Pixel Runner/sources/ground.png').convert_alpha()

pause_foreground = pygame.Surface((800,400))
pause_foreground.set_alpha(128)
pause_foreground.fill((255,255,255))

# BUTTONS

restart_button_surface = pygame.image.load('Python/Pixel Runner/sources/UI-gameover.fw.png')
restart_button_rect = restart_button_surface.get_rect(center = (400, 200)) 

settings_button_surface = pygame.image.load('Python/Pixel Runner/sources/settings_button.png')
settings_button_rect = settings_button_surface.get_rect(topleft = (10,10))

back_button_surface = pygame.image.load('Python/Pixel Runner/sources/back_button.fw.png')
back_button_rect = back_button_surface.get_rect(topright = (790,10))

# INTRO
player_surface = pygame.image.load('Python/Pixel Runner/sources/pixel-knight-right.png').convert_alpha()
player_scaled = pygame.transform.rotozoom(player_surface,0,2)
player_scaled_rect = player_scaled.get_rect(center = (400,250))


# TEXT

test_font = pygame.font.Font('Python/Pixel Runner/sources/Pixeltype.ttf',50)



title_surface = test_font.render('Pixel Runner', False , 'Black')
title_rect = title_surface.get_rect(center = (400, 50))

message_surface = test_font.render('Press space to play', False , 'Black')
message_rect = message_surface.get_rect(center = (400,140))

instructions_surface = test_font.render('A for left , D for right , Space for jump', False , 'Black')
instructions_rect = instructions_surface.get_rect(center = (400, 370))

pause_title = test_font.render('Paused',False,'Black') 
pause_title_rect = pause_title.get_rect(center = (400,150))