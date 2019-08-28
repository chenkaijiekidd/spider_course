# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : http_post.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import requests

post_url = 'https://httpbin.org/post'
data = {'field1': 'a', 'field2': 'b'}
#HTTP_POST请求
#response = requests.post(post_url, data=data)
#等效于
response = requests.request('POST', url=post_url, data=data)
print(response.text)
