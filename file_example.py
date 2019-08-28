# -*- coding: utf-8 -*-
"""
@Time : 2019-08-12 11:24
@Author : kidd
@Site : http://www.bwaiedu.com/
@File : file_example.py
@公众号: 蓝鲸AI教育 bwaiedu
"""

import os

#如文件已经存在则先删除再做实验
if os.path.exists('file_example.txt'):
    os.remove('file_example.txt')

#写模式打开文件
with open('file_example.txt', 'w') as file:
    file.write('This is for file handle test!\n')

#追加写的模式打开文件
with open('file_example.txt', 'a') as file:
    file.writelines(['add first line\n', 'add second line\n'])

#读模式打开文件
with open('file_example.txt', 'r') as file:
    print(file.read())

#读模式打开文件，并可以更新文件内容，文件指针将会放在文件的开头
with open('file_example.txt', 'r+') as file:
    file.write('That')

#读模式打开文件，并且读取多行，需要注意把换行符也读取
with open('file_example.txt', 'r') as file:
    line_list = file.readlines()
    print(line_list)

