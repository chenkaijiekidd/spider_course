# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : test.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import requests

get_url = 'https://httpbin.org/get'
#构造参数
params = {'param1': '1', 'param2': '2'}
#HTTP GET请求
#构造url:https://httpbin.org/get?param1=1&param2=2
response = requests.get('https://httpbin.org/get', params=params)
#等效于
#response = requests.request('GET', url=get_url, params=params)
print(response.text)
