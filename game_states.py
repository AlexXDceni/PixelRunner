import pygame
import pygame_menu as pm
from config import *

pygame.init()



# python -m auto_py_to_exe  # run app

# TIMERS

clock = pygame.time.Clock()
obstacle_timer = pygame.USEREVENT + 1 
pygame.time.set_timer(obstacle_timer,1500)

# GAME STATES

game_result = 'start_menu'
game_active = False
game_pause = True



























# PYGAME_MENU

# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# CYAN = (0, 100, 100)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)




# resolution = [("1920x1080", "1920x1080"),
#                   ("1920x1200", "1920x1200"),
#                   ("1280x720", "1280x720"),
#                   ("2560x1440", "2560x1440"),
#                   ("3840x2160", "3840x2160")]


# difficulty = [("Easy", "Easy"),
#                   ("Medium", "Medium"),
#                   ("Hard", "Hard")]


# global settings
# settings = pm.Menu(title="Settings",
#                        width=WIDTH,
#                        height=HEIGHT,
#                        theme=pm.themes.THEME_GREEN)

# settings._theme.widget_font_size = 25
# settings._theme.widget_font_color = BLACK
# settings._theme.widget_alignment = pm.locals.ALIGN_LEFT


# settings.add.text_input(title="User Name : ", textinput_id="username")

# settings.add.dropselect_multiple(title="Window Resolution", items=resolution,
#                                      dropselect_multiple_id="Resolution",
#                                      open_middle=True, max_selected=1,
#                                      selection_box_height=6)


# settings.add.toggle_switch(
#     title="Muisc", default=True, toggleswitch_id="music")
# settings.add.toggle_switch(
#     title="Sounds", default=False, toggleswitch_id="sound")


# settings.add.selector(title="Difficulty\t", items=difficulty,
#                           selector_id="difficulty", default=0)

    
# settings.add.button(title="Restore Defaults", action=settings.reset_value,
#                         font_color=WHITE, background_color=RED)
   
# def menu_closing():
#     settings.disable()   
    
# settings.add.button("Return To Main Menu",
#                         menu_closing(), align=pm.locals.ALIGN_CENTER)

  
# settings.mainloop(screen)


