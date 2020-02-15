"""
同步多线程 类方法使用例子
"""
# -*- coding:utf-8 -*-
import threading
import time
import datetime

__author__ = 'Evan'


class Test(threading.Thread):  # 继承threading.Thread类

    def __init__(self, sleep_time, thread_pool):
        super().__init__()  # 执行父类的构造方法
        self.sleep_time = sleep_time
        self.thread_pool = thread_pool  # 线程池句柄

    def run(self):
        """
        改写父类run方法，需要执行的多线程函数写在这里
        :return:
        """
        print('current thread name {}'.format(threading.current_thread().name))  # 当前线程名
        print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), self.sleep_time))
        time.sleep(self.sleep_time)
        print('{} --> sleep_time ({}) finish'.format(datetime.datetime.now(), self.sleep_time))
        self.thread_pool.release()  # 释放线程锁，可用线程数加1


if __name__ == '__main__':
    pool = threading.Semaphore(value=2)  # 线程池（设置可同时执行的最大线程数为2）
    for i in [3, 2, 6, 1, 7]:
        pool.acquire()  # 获得线程锁，可用线程数减1
        t = Test(sleep_time=i, thread_pool=pool)  # 实例化线程类
        t.start()  # 开启线程（线程会自动执行run方法）
