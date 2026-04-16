import pygame
#import pygame_menu as pm
import json
pygame.init()

WIDTH = 800
#HEIGHT = 400
HEIGHT = WIDTH / 2
FPS = 60



# SPRITES VARIABLES

enemy_mov_speed = 4

# TIME and SCORE

pause_time = 0
paused_total_time = 0
start_time = 0    
score = 0
highscore = 0
with open('Python/Pixel Runner/save_file.txt') as save_file:
    highscore = json.load(save_file)


# MUSIC

bg_music = pygame.mixer.Sound('Python/Pixel Runner/sources/music.wav')
bg_music.set_volume(0.09)
bg_music.play(loops = -1)

