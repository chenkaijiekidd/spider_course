# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : http_cookie.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import requests
#在请求头中设置cookie

get_url = 'https://www.zhihu.com/'

response = requests.get(get_url)
for key, value in response.request.headers.items():
    print('{}:{}'.format(key, value))
else:
    print('**************************')
cookies = response.cookies
print(requests.utils.dict_from_cookiejar(cookies))
print('**************************')

response = requests.post(get_url, cookies=cookies)
for key, value in response.request.headers.items():
    print('{}:{}'.format(key, value))
else:
    print('**************************')
