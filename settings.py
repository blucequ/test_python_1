#!/usr/bin/python
# -*- coding:utf-8 -*-
class Settings():
 #存储外星人游戏的所有设置的类,注意init附近的事两个下划线
    def __init__(self):
    #“““  初始化游戏的设置  ”””
    # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allow = 4
