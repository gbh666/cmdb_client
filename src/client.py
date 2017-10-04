#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/9/27

from src.plugins import PluginManager
from lib.config import settings
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import json
import requests

class BaseClient(object):
    '''
    基类
    '''
    def __init__(self):
        self.api = settings.API

    def post_server_info(self,server_dict):
        # requests.post(self.api,data=server_dict) # 1.k=v&k=v    2.content-type:application/x-www-form-
        response = requests.post(self.api,json=server_dict) # 1.字典序列化  2.带请求头 content-type:application/json

    def exec(self):
        '''规定子类中必须有这个方法，否则在调用时会报错'''
        raise NotImplementedError("必须实现exec方法")

class AgentClient(BaseClient):
    '''
    Agent模式下执行的类
    '''

    def exec(self):
        obj = PluginManager()
        server_dict = obj.exec_plugin()
        self.post_server_info(server_dict)

class SaltSshClient(BaseClient):
    '''
    salt模式和ssh模式下执行的类
    '''

    def task(self,host):
        '''
        发送采集到的数据
        :param host: 服务器主机名
        :return: 
        '''
        obj = PluginManager(host)
        server_dict = obj.exec_plugin()
        self.post_server_info(server_dict)

    def get_host_list(self):
        '''
        获取今日未采集的服务器主机名
        :return: 服务器返回的文本
        '''
        response = requests.get(self.api)
        print(response)
        return json.loads(response.text)

    def exec(self):
        '''使用线程池采集数据'''
        pool = ThreadPoolExecutor(10) #开启线程池
        host_list = self.get_host_list()
        for host in host_list:
            pool.submit(self.task,host['hostname'])


