# -*- coding:utf-8 -*-
"""
Numpy基本用法
"""
import numpy as np

__author__ = 'Evan'

# 创建数组
print('创建一维数组\n{}'.format(np.array([1, 2, 3])))
print('创建0-9范围的一维数组\n{}'.format(np.arange(10)))
print('创建二维数组\n{}'.format(np.array([[1, 2, 3], [4, 5, 6]])))
print('创建2行3列的随机数组\n{}'.format(np.random.rand(2, 3)))
print('指定二维数组\n{}'.format(np.array([1, 2, 3], ndmin=2)))
print('指定元素类型为复数\n{}'.format(np.array([1, 2, 3], dtype=complex)))

# 查看数组属性
test = np.array([[1, 2, 3], [4, 5, 6]])
print('\n当前数组\n{}'.format(test))
print('返回当前维度\n{}'.format(test.ndim))
print('返回一个包含数组纬度的元组（行，列）\n{}'.format(test.shape))
print('返回元素的类型\n{}'.format(test.dtype))
print('返回元素的个数\n{}'.format(test.size))
print('返回每个元素的大小，以字节为单位 ，每个元素占4个字节\n{}'.format(test.itemsize))

# 数组操作
test.resize((3, 2))  # 改变当前数组，依shape生成
print('数组转置\n{}'.format(test.transpose()))  # 行列转置
print('数组转换为列表\n{}'.format(test.tolist()))
print('改变数组维度的大小\n{}'.format(test.reshape(1, 6)))  # 不改变当前数组，依shape生成
print('转换数组的数据类型\n{}'.format(test.astype(np.float64)))
