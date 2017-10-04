#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/26
import importlib
import requests
from lib.config import settings
import traceback

# 把采集到的信息以post的形式发送给server端
# requests.post(
#     url=settings.API,
#     data=server_info
# )

class PluginManager(object):
    '''
    插件管理
    '''
    def __init__(self,hostname=None):
        self.hostname = hostname
        self.plugin_items = settings.PLUGIN_ITEMS
        self.mode = settings.MODE
        self.test = settings.TEST
        if self.mode == "SSH":
            self.ssh_user = settings.SSH_USER
            self.ssh_port = settings.SSH_PORT
            self.ssh_pwd = settings.SSH_PWD

    def exec_plugin(self):
        '''
        采取信息
        :return: 
        '''
        server_info = {}
          # 返回给server端的字典

        for k, v in self.plugin_items.items():  # 循环每个插件的路径
            info = {'status': True, 'data': None, 'error_msg': None}
            try:
                module_path, cls_name = v.rsplit('.', maxsplit=1)  # 以'.'从右向左分隔，分隔一次，拿到插件路径和类名
                module = importlib.import_module(module_path)  # 用importlib模块根据字符串路径引入模块
                cls = getattr(module, cls_name)  # 查看模块中有没有类，有的话实例化之后执行process方法拿到信息，
                if hasattr(cls,'initial'):
                    obj = cls.initial()
                else:
                    obj = cls()
                ret = obj.process(self.exec_cmd,self.test)
                info['data'] = ret
            except Exception as e:
                info['status'] = False
                info['error_msg'] = traceback.format_exc()
            server_info[k] = info# 拿到信息写入字典
        return server_info

    def exec_cmd(self,cmd):
        '''根据兼容模式执行对应操作'''
        if self.mode == 'AGENT':
            import subprocess
            result = subprocess.getoutput(cmd)
        elif self.mode == 'SSH':
            import paramiko
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hostname, port=self.ssh_port, username=self.ssh_user, password=self.ssh_pwd)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()
        elif self.mode == 'SALT':
            import subprocess
            result = subprocess.getoutput('salt "%s" cmd.run "%s"' %(self.hostname,cmd))

        else:
            raise Exception("模式选择错误，AGENT,SSH,SALT")
        return result