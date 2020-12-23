# -*- coding:utf-8 -*-
import os
import sys
import chardet

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


# 循环取出指定目录下所有的子文件夹和子文件
all_files = []
for root, dirs, files in os.walk(os.getcwd()):  # 展开文件目录下所有的子目录和文件
    # root 返回当前文件夹的绝对路径 - str
    # dirs 返回该文件夹下所有的子目录名 - list
    # files 返回该文件夹下所有的子文件 - list
    for each_file in files:  # 遍历保存所有的文件
        all_files.append(os.path.join(root, each_file))
print('目录: {}, 所有文件: {}'.format(os.getcwd(), all_files))


# 获取文件的编码格式
file_name = 'os_example.py'
result = chardet.detect(open(file_name, mode='rb').read())
print('{} -> file encoding: {}'.format(file_name, result))
