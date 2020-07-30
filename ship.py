#-*- codeing = utf-8 -*-
#@Time : 2020/7/13 20:54
#@Author : James
#@File : ship.py
#@Software : PyCharm
import pygame

class Ship():
    def __init__(self,screen,game_settings):
        self.screen=screen

        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.game_settings=game_settings

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.centerx=float(self.rect.centerx)
        self.centery=float(self.rect.centery)


        self.moving_right=False
        self.moving_up=False
        self.moving_down=False
        self.moving_left=False

    def update(self):
        if self.moving_up and self.rect.top >0:
            self.centery -=1

        if self.moving_down and (self.rect.bottom<self.screen_rect.bottom):
            self.centery +=1

        if self.moving_right and (self.rect.right<self.screen_rect.right):
            self.centerx +=1

        if self.moving_left and self.rect.left >0:
            self.centerx -=1

        self.rect.centerx=self.centerx
        self.rect.centery=self.centery

    def blitme(self):
        self.screen.blit(self.image,self.rect)