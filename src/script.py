#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/27

from lib.config import settings
from .client import AgentClient
from .client import SaltSshClient

def start():
    if settings.MODE == 'AGENT':
        obj = AgentClient()
    elif settings.MODE == 'SSH' or settings.MODE == 'SALT':
        obj = SaltSshClient()
    else:
        raise Exception('模式仅支持：AGENT/SSH/SALT')
    obj.exec()
