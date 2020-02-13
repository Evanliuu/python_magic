"""
异步多线程
"""
# -*- coding:utf-8 -*-
import time
import datetime
from concurrent.futures import ThreadPoolExecutor


pool_max = 2  # 线程池最大数量
thread_pool = ThreadPoolExecutor(max_workers=pool_max)  # 初始化多线程


def unit_test(sleep_time):
    """
    多线程单元测试
    :param sleep_time: 睡眠时间
    :return:
    """
    print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
    time.sleep(sleep_time)
    print('{} --> sleep_time ({}) done'.format(datetime.datetime.now(), sleep_time))


def main():
    # 异步多线程运行不会阻塞主线程，异步线程队列满了后继续往下运行主线程，等队列释放后又会回到异步线程继续执行
    for times in [5, 2, 4, 1]:
        thread_pool.submit(unit_test, times)


if __name__ == '__main__':
    main()
    print('ll')
    main()
