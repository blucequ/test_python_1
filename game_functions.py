#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event_key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
	#���û�дﵽ���ƣ��ͷ����ӵ�
	if len(bullets) < ai_settings.bullet_allow:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
       ship.moving_right = False
    elif event.key == pygame.K_LEFT:
       ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets):
    # ��Ӧ����������¼�
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        #��ⰴ�Ҽ�����
        elif event.type == pygame.KEYDOWN:
             check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
             check_keyup_events(event, ship)

        #��ⰴ�Ҽ�̧��
        elif event.type == pygame.KEYUP:
             if event.key == pygame.K_RIGHT:
                 ship.moving_right = False
             if event.key == pygame.K_LEFT:
                 ship.moving_left = False

def update_screen(ai_settings, screen,ship, bullets):
    screen.fill(ai_settings.bg_color)
    #Ҫ�ڷɴ�������ӵ�������ᱻ���ǵ�
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    pygame.display.flip()
    
def update_bullets(bullets):
     bullets.update()
       #ɾ���Ѿ���ʧ���ӵ�
     for bullet in bullets.copy():
           if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
