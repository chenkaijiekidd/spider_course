# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : lxml_example.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

from lxml import etree

text = '''
<?xml version="1.0" encoding="UTF-8"?>
<bookstore>
    <book category="cooking">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
    <book category="children">
        <title lang="en">Harry Potter</title>
        <author>J K. Rowling</author>
        <year>2005</year>
        <price>29.99</price>
    </book>
    <book category="web">
        <title lang="en">XQuery Kick Start</title>
        <author>James McGovern</author>
        <author>Per Bothner</author>
        <author>Kurt Cagle</author>
        <author>James Linn</author>
        <author>Vaidyanathan Nagarajan</author>
        <year>2003</year>
        <price>49.99</price>
    </book>
    <book category="web">
        <title lang="en">Learning XML</title>
        <author>Erik T. Ray</author>
        <year>2003</year>
        <price>39.95</price>
    </book>
    <book category="xpath">
        <title lang="ch">Learning xpath</title>
        <author>Anyone</author>
        <year>2013</year>
        <price>59.95</price>
    </book>    
</bookstore>
'''
# html = etree.HTML(text)
# result = etree.tostring(html, encoding='gbk')
# print(result.decode('utf-8'))
# 自动补全功能，由于涉及中文， 需要用gbk编码
# print(result.decode('gbk'))

#读取字符串变量
#html = etree.HTML(text)
#读取文件
html = etree.parse('./book_store.xml')

#显示所有的内容
result = etree.tostring(html)
print('所有节点：', result.decode('utf-8'), end='\n************************************\n')

#显示所有的节点
result = html.xpath('//*')
print(result, end='\n************************************\n')

# // 从当前节点选取子孙节点 text()获取文本
print('选取所有书本的标题', html.xpath('//book/title/text()'), end='\n************************************\n')

# // 从当前节点选取子孙节点 [@]属性筛选
print('选取所有英文书本的标题', html.xpath('//book/title[@lang="en"]/text()'), end='\n************************************\n')

# // 从当前节点选取子孙节点 @属性获取
print('选取所有书本的分类', html.xpath('//book/@category'), end='\n************************************\n')

#获取第一本书，注意序号是从1开始！！
print('第一本书名字：', html.xpath('//bookstore/book[1]/title/text()')[0], end='\n************************************\n')

#获取最后一本书的名字
print('最后一本书名字：', html.xpath('//bookstore/book[last()]/title/text()')[0], end='\n************************************\n')

#筛选价格
print('价格大于35块的书：', html.xpath('//bookstore/book[price>35.00]/title/text()'), end='\n************************************\n')

# 分开不同的列表 . 表示获取当前节点
for book in html.xpath('//book'):
    print(book.xpath('./title/text()'))
