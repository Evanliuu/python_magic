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
    max_value = 3  # 设置可同时执行的最大线程数为3
    thread_pool = threading.Semaphore(value=max_value)  # 初始化线程池
    print('线程池最大数量：{}'.format(max_value))

    threads = []
    for i in sleep_list:  # 配置所有线程
        t = threading.Thread(target=unit_test, args=(i,))
        threads.append(t)

    for thread in threads:  # 开启所有线程
        thread.start()
        while True:
            # 判断正在运行的线程数量, 控制执行的线程数量永远为4-1=3个
            if len(threading.enumerate()) <= 4:
                # threading.enumerate()包括主线程和所有的活动子线程，长度最少为1
                print('剩余活动线程数量: {}'.format(len(threading.enumerate())))
                break

    # TODO thread.join()和下面的while循环都可阻塞所有线程，依据情况进行选择
    # for thread in threads:  # 主线程在此阻塞，等待所有线程结束
    #     thread.join()

    while True:
        # 当线程数量等于1时，并且只剩下一个主线程，退出循环
        if len(threading.enumerate()) == 1 and 'MainThread(MainThread' in str(threading.enumerate()[0]):
            break

    print('所有线程执行结束')

    # 标准写法
    """
    threads = []
    for i in range(5):
        t = threading.Thread(target=unit_test, args=(i,))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    """


def main():
    thread_run(sleep_list=[3, 2, 6, 1, 7, 5, 8])


if __name__ == '__main__':
    main()
