"""
多线程同步（函数化）
"""
# -*- coding:utf-8 -*-
import threading
import datetime
import time

__author__ = 'Evan'
locks = None
thread_pool = None


def unit_test(sleep_time):
    """
    多线程单元测试
    :param sleep_time: 睡眠时间
    :return:
    """
    # locks.acquire()   获取锁 -- 获取锁之后，其他的线程在此等待

    with thread_pool:  # 使用线程池控制多线程进入的数量，超过限定数量在此阻塞
        print('current thread name {}'.format(threading.current_thread().name))  # 当前线程名
        print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
        time.sleep(sleep_time)
        print('{} --> sleep_time ({}) finish'.format(datetime.datetime.now(), sleep_time))

    # locks.release()   释放锁 -- 如果不释放锁，后续的线程会一直被阻塞不能进入


def thread_run(sleep_list):
    """
    执行多线程
    :param sleep_list: 睡眠时间列表
    :return:
    """
    global locks, thread_pool

    locks = threading.Lock()  # 线程锁
    max_value = 3
    thread_pool = threading.Semaphore(value=max_value)  # 线程池（设置可同时执行的最大线程数为3）
    threads = []
    print('线程池最大数量：{}'.format(max_value))

    for i in sleep_list:  # 配置所有线程
        t = threading.Thread(target=unit_test, args=(i,))
        threads.append(t)

    for thread in threads:  # 开启所有线程
        thread.start()

    for thread in threads:  # 主线程在此阻塞，等待所有线程结束
        thread.join()
        print('剩余活动线程数量: {}'.format(len(threading.enumerate())))  # 包括主线程和所有活动子线程，长度最少为1

    print('所有线程执行结束')


def main():
    thread_run(sleep_list=[3, 2, 6, 1, 7])


if __name__ == '__main__':
    main()
