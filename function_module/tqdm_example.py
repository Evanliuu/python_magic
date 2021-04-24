# -*- coding:utf-8 -*-
import tqdm
import time

__author__ = 'Evan'

"""tqdm常用参数
desc：进度条标题
total：迭代总次数
ncols：进度条总长度
ascii：使用ASCII字符串作为进度条主体
bar_format：自定义字符串格式化输出
mininterval：最小更新间隔，单位：秒
maxinterval：最大更新间隔，单位：秒
postfix：以字典形式传入
"""


# 如果已知循环次数，使用trange方法输出
for i in tqdm.trange(5):
    time.sleep(0.5)


# 迭代数组形式输出
for i in tqdm.tqdm([1, 2, 3, 4, 5]):
    time.sleep(0.5)


# 手动控制输出，常用于文件发送或读取的情景
file_name = 'example.txt'
file_size = 100
with tqdm.tqdm(desc=f'发送: {file_name}', total=file_size, unit='B') as bar:
    for i in range(5):
        time.sleep(0.5)
        bar.update(20)  # 指定每次更新的数量
