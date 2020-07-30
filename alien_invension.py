#-*- codeing = utf-8 -*-
#@Time : 2020/7/13 20:23
#@Author : James
#@File : alien_invension.py
#@Software : PyCharm

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions
from pygame.sprite import Group
from alien import Alien

def main():
    run_game()




def run_game():
    pygame.init()

    game_settings=Settings()
    screen=pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(screen,game_settings)
    aliens=Group()
    game_functions.create_fleet(game_settings,screen,aliens)
    bullets=Group()
    while True:
        game_functions.check_events(ship,bullets,screen,game_settings)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(game_settings,screen,ship,aliens,bullets)






if __import__(__name__):
    main()