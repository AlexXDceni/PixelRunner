import pygame
#import pygame_menu as pm
import json

from sys import exit
from random import choice

from config import *
from game_states import *
from textures import *
from player_sprite import Player , player_group
from enemy_sprite import Obstacle , obstacle_group, collisions_sprite


pygame.init()

player = Player()  
player_group.add(player)

def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time - paused_total_time
    score_surface = test_font.render(f'Score: {current_time}',False,'Black')
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

pause_time  = int(pygame.time.Clock.get_time(clock)/1000)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Python/Pixel Runner/save_file.txt', 'w') as save_file:
               json.dump(highscore,save_file)
            pygame.quit()
            exit()
        
        
        
        # Setting the screen size    
        if event.type == pygame.VIDEORESIZE:
           screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
        
        # Adding obstacles and pause
        if game_active:    
            if event.type == obstacle_timer and not game_pause:
                obstacle_group.add(Obstacle(choice(['bat','snail','snail','snail'])))
           
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if game_pause:
                        game_pause = False
                        paused_total_time = paused_total_time + (int(pygame.time.get_ticks() / 1000) - pause_time)
                    else: 
                        game_pause = True 
                        pause_time = int(pygame.time.get_ticks() / 1000)            
            
        # Accesing menus          
        else:
            if event.type == pygame.MOUSEBUTTONUP and restart_button_rect.collidepoint(pygame.mouse.get_pos()) and game_result == 'game_over':   
                game_result = 'start_menu'
            
            if event.type == pygame.MOUSEBUTTONUP and settings_button_rect.collidepoint(pygame.mouse.get_pos()) and game_result == 'start_menu':   
                game_result = 'settings'
                #settings.enable()

            if event.type == pygame.MOUSEBUTTONUP and back_button_rect.collidepoint(pygame.mouse.get_pos()) and game_result == 'settings':   
                game_result = 'start_menu'
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_result == 'settings':  # de ce nu merge
                game_result == 'start_menu'
         
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_result == 'start_menu':
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000) # nu creste daca functia nu este in main
                    paused_total_time = 0
                    game_pause = False
                   
                          

                 
    # Game stuff
    if game_active:    
       
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300)) 

        if  not game_pause:
            score = display_score()
        if score > highscore: highscore = score 
        
        # INCREASE DIFICULTY
        enemy_mov_speed += 0.005

        obstacle_group.draw(screen)
        if not game_pause:
            obstacle_group.update()
        
        player_group.draw(screen)
        if not game_pause:  
            player_group.update()
 
        if collisions_sprite() == False:
            game_active = False
            game_result = 'game_over'
            player.reset_location()

        
        
        
        # Pause stuff
        if game_pause:
            
            screen.blit(pause_foreground,(0,0))
            screen.blit(pause_title,pause_title_rect)
           
 
    # Menu stuff    
    else:

        if game_result == 'start_menu':
        
            screen.fill((94,129,162))
            screen.blit(player_scaled, player_scaled_rect)
            enemy_mov_speed = 4
            
            score_surface = test_font.render(f'Score: {score}', False , 'Black')
            score_rect = score_surface.get_rect(center = (400,140))
            
            highscore_surface = test_font.render(f'Highscore: {highscore}', False , 'Black')
            highscore_rect = highscore_surface.get_rect(center = (400,100))
            
            screen.blit(title_surface,title_rect)
            screen.blit(instructions_surface,instructions_rect)
            screen.blit(highscore_surface,highscore_rect)
            screen.blit(settings_button_surface,settings_button_rect)
            
            if score == 0: screen.blit(message_surface,message_rect)
            else: screen.blit(score_surface,score_rect)
    
                
    
        elif game_result == 'game_over':
            
            screen.fill((94,129,162))
            enemy_mov_speed = 4
            score_surface = test_font.render(f'Score: {score}', False , 'Black')
            score_rect = score_surface.get_rect(center = (400,140))
            screen.blit(score_surface,score_rect)
            screen.blit(restart_button_surface,restart_button_rect)          



        elif game_result == 'settings':
            screen.fill((94,129,162))
            screen.blit(back_button_surface,back_button_rect)
            
            
   

    pygame.display.update()
    clock.tick(FPS)
