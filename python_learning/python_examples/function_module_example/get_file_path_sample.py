# -*- coding:utf-8 -*-
import os
import sys

__author__ = 'Evan'


print('getcwd ==>', os.getcwd())  # 获取当前目录路径
print('path ==>', sys.path[0])  # 获取当前目录路径
print('dirname ==>', os.path.dirname(os.path.abspath(__file__)))  # 获取当前目录路径


print('file ==>', __file__)  # 获取当前文件名路径
print('argv ==>', sys.argv[0])  # 获取当前文件名路径


print('realpath ==>', os.path.realpath(__file__))  # 获取当前文件名真实路径
print('abspath ==>', os.path.abspath(__file__))  # 获取当前文件名绝对路径


print('path.sep ==>', os.path.sep)  # 分隔符
print(os.path.join(os.getcwd(), __file__))  # 路径拼接
