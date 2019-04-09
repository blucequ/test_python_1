#!/usr/bin/python
# -*- coding:utf-8 -*-
# �������У����Ա�������ע������
import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    # --+++ ʵ�� +++--
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
       (ai_settings.screen_width , ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()

    while True:
       gf.check_events(ai_settings, screen, ship, bullets)
       ship.update()
      
       #print (len(bullets))
       gf.update_bullets(bullets)
       gf.update_screen(ai_settings, screen, ship, bullets)
run_game()
            
      
    