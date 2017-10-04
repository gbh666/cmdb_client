#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/26
import os
import importlib
from . import global_settings

class Settings(object):
    '''
    global_settings，配置获取
    settings，配置获取
    '''
    def __init__(self):

        # 获取全局配置
        for item in dir(global_settings): #循环全局配置中的所有变量
            if item.isupper():
                k = item
                v = getattr(global_settings,item) #取到变量的值
                setattr(self,k,v) # 以键值对的方式赋值给对象

        # 获取用户自定义配置
        settings_path = os.environ.get('AUTO_CLIENT_SETTINGS')
        md_settings = importlib.import_module(settings_path)
        for item in dir(md_settings):
            if item.isupper():
                k = item
                v = getattr(md_settings,item)
                if k == 'PLUGIN_ITEMS':
                    self.PLUGIN_ITEMS.update(v)
                else:
                    setattr(self,k,v)

settings = Settings()