#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/25
import sys
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASEDIR)

os.environ['AUTO_CLIENT_SETTINGS'] = "conf.settings" #把配置文件路径写进当前进程的环境变量，
from src import script

if __name__ == '__main__':

    script.start()