"""
多线程异步
"""
# -*- coding:utf-8 -*-
import time
import datetime
from concurrent.futures import ThreadPoolExecutor

__author__ = 'Evan'


def unit_test(sleep_time):
    """
    多线程单元测试
    :param sleep_time: 睡眠时间
    :return:
    """
    print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
    time.sleep(sleep_time)
    print('{} --> sleep_time ({}) finish'.format(datetime.datetime.now(), sleep_time))


def main():
    max_value = 4  # 线程池最大数量
    thread_pool = ThreadPoolExecutor(max_workers=max_value)  # 初始化线程池
    print('线程池最大数量：{}'.format(max_value))

    # 异步多线程运行不会阻塞主线程，异步线程队列满了后会继续往下运行主线程，等队列释放后又回到异步线程继续执行
    for i in [3, 2, 6, 1, 7]:
        thread_pool.submit(unit_test, i)
    print('{} --> 我是主线程'.format(time.ctime()))


if __name__ == '__main__':
    main()
