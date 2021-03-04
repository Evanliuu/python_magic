"""
多进程同步（函数化）
"""
# -*- coding:utf-8 -*-
import datetime
import time
from multiprocessing import Process

__author__ = 'Evan'


def unit_test(sleep_time):
    """
    多进程单元测试
    :param sleep_time: 睡眠时间
    :return:
    """
    print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
    time.sleep(sleep_time)
    print('{} --> sleep_time ({}) finish'.format(datetime.datetime.now(), sleep_time))


def process_run(sleep_list):
    """
    执行多进程
    :param sleep_list: 睡眠时间列表
    :return:
    """
    process = []

    for i in sleep_list:  # 配置所有进程
        t = Process(target=unit_test, args=(i,))
        process.append(t)

    for i in process:  # 开启所有进程
        i.start()

    for i in process:  # 主进程在此阻塞，等待所有进程结束
        i.join()

    print('所有进程执行结束')


def main():
    process_run(sleep_list=[3, 2, 6, 1, 7])


if __name__ == '__main__':
    main()
