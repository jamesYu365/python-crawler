#-*- codeing = utf-8 -*-
#@Time : 2020/7/14 21:24
#@Author : James
#@File : bullet.py
#@Software : PyCharm

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,game_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen
        self.rect=pygame.Rect(0,0,game_settings.bullet_width,game_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top
        self.y=float(self.rect.y)
        self.color=game_settings.bullet_color
        self.speed_factor=game_settings.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)