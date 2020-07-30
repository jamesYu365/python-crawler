#-*- codeing = utf-8 -*-
#@Time : 2020/7/13 21:19
#@Author : James
#@File : game_functions.py
#@Software : PyCharm

import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ship,bullets,screen,game_settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship,bullets,screen,game_settings)
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ship,bullets,screen,game_settings)



def check_keydown_events(event,ship,bullets,screen,game_settings):

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key==pygame.K_SPACE:
        if len(bullets)<game_settings.bullet_allowed:
            new_bullet=Bullet(game_settings,screen,ship)
            bullets.add(new_bullet)

    elif event.key==pygame.K_q:
        sys.exit()
    else:
        pass

def check_keyup_events(event,ship,bullets,screen,game_settings):

    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
    else:
        pass

def update_screen(game_settings,screen,ship,aliens,bullets):
    screen.fill(game_settings.bg_color)
    for bullet in bullets:
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_fleet(game_settings,screen,alien):
    pass