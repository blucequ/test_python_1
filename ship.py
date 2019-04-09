#!/usr/bin/python
# -*- coding:utf-8 -*-
import pygame

class Ship():
    def __init__(self, ai_settings, screen):
      #"""��ʼ���ɴ����ò��������ʼλ��"""
      self.screen = screen
      #���طɴ�ͼ�񲢻�ȡ����Ӿ���
      self.image = pygame.image.load('images/feiji1.bmp')
      self.rect = self.image.get_rect()
      self.screen_rect = screen.get_rect()
      self.ai_settings = ai_settings

      #��ÿ���·ɴ�������Ļ�ײ�����
      self.rect.centerx = self.screen_rect.centerx
      self.rect.bottom = self.screen_rect.bottom
      # �ڷɴ��������д洢С��ֵ
      self.center = float(self.rect.centerx)
      #�ƶ���־
      self.moving_right = False
      self.moving_left = False
    def update(self):
		#�����ƶ���־�����ɴ���λ��
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center			            
    def blitme(self):
      #��ָ��λ�û��Ʒɴ�
      self.screen.blit(self.image,self.rect)
