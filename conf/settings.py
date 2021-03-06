#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/25
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 插件
PLUGIN_ITEMS = {
    "nic": "src.plugins.nic.Nic",
    "disk": "src.plugins.disk.Disk",
    "memory": "src.plugins.memory.Memory",
}

API = "http://127.0.0.1:8000/api/server.html"

TEST = True

MODE = "SSH"  #AGENT/SSH/SALT 兼容模式

SSH_USER = "root"
SSH_PORT = 22
SSH_PWD = 123