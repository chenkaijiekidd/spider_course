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
#HTTP GET请求
response = requests.get('https://httpbin.org/get')
#等效于
#response = requests.request('GET', url=get_url)
#打印响应头信息
print('********************************')
for key, value in response.headers.items():
    print('{}:{}'.format(key, value))
else:
    print('********************************')

#打印响应内容
print(response.text)
print('********************************')

