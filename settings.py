#!/usr/bin/python
# -*- coding:utf-8 -*-
class Settings():
 #�洢��������Ϸ���������õ���,ע��init�������������»���
    def __init__(self):
    #������  ��ʼ����Ϸ������  ������
    # ��Ļ����
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1
        # �ӵ�����
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allow = 4
