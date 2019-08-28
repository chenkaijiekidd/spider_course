# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : urllib_example.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urljoin

#urlparse()
#实现url的识别和分段
result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(
    {'scheme': result.scheme,        #协议
        'netloc': result.netloc,     #域名
        'path': result.path,         #访问路径，以;作为分隔符
        'params': result.params,     #参数，以?作为分隔符
        'query': result.query,       #查询条件，以=作为分隔符
        'fragment': result.fragment  #页面锚点，以#作为分隔符
     }
)


#urlsplit
#实现url的识别，比urlparse少了params
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(
    {'scheme': result.scheme,        #协议
        'netloc': result.netloc,     #域名
        'path': result.path,         #访问路径，以;作为分隔符
        'query': result.query,       #查询条件，以=作为分隔符
        'fragment': result.fragment  #页面锚点，以#作为分隔符
     }
)


#urlunparse
#实现url的组合，参数是一个可迭代的对象，长度必须是6
# dict = {'scheme': 'http',
#         'netloc': 'www.baidu.com',
#         'path': '/index.html',
#         'params': 'user',
#         'query': 'id=5',
#         'fragment': 'comment'}
# print(urlunparse(dict.values()))

data = ['http', 'www.baidu.com', '/index.html', 'user', 'id=5', 'comment']
print('urlunparse:', urlunparse(data))


#urlunsplit
data = ['http', 'www.baidu.com', '/index.html;user', 'id=5', 'comment']
print('urlunsplit:', urlunsplit(data))
