# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : http_post_json.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import requests

post_url = 'https://httpbin.org/post'
json_str = {'name': 'Mike', 'age': 25}

response = requests.post(post_url, json=json_str)
print(response.text)
