# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : test.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

#注意 response.request.headers - 是请求头
# response.headers - 是响应头
import requests

get_url = 'https://httpbin.org/get'

print('#############################')
#未设置请求头
response = requests.post(get_url)
for key, value in response.request.headers.items():
    print('{}:{}'.format(key, value))
print('#############################')


#设置请求头
headers = {
    "Host": "search.51job.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0",
    "Accept": "text/css,*/*;q=0.1",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Pragma": "no-cache",
}
response = requests.post(get_url, headers=headers)
for key, value in response.request.headers.items():
    print('{}:{}'.format(key, value))
