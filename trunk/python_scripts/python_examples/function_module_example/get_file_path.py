# -*- coding: UTF-8 -*-
import os
import sys


# 当前目录路径
print('getcwd ==>', os.getcwd())
# 当前目录路径
print('path ==>', sys.path[0])
# 当前目录路径
print('dirname ==>', os.path.dirname(os.path.abspath(__file__)))

# 当前文件名路径
print('file ==>', __file__)
# 当前文件名路径
print('argv ==>', sys.argv[0])

# 当前文件名真实路径
print('realpath ==>', os.path.realpath(__file__))
# 当前文件名绝对路径
print('abspath ==>', os.path.abspath(__file__))

# 分隔符
print('path.sep ==>', os.path.sep)
# 字符串拼接
print(os.path.join(os.getcwd(), __file__))
