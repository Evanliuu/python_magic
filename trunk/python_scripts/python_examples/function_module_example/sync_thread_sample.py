"""
同步多线程
"""
# -*- coding:utf-8 -*-
import threading
import datetime
import time

locks = None


def unit_test(sleep_time):
    """
    多线程单元测试
    :param sleep_time: 睡眠时间
    :return:
    """
    # locks.acquire()   获取锁 -- 获取锁之后，其他的线程在此等待
    print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
    time.sleep(sleep_time)
    print('{} --> sleep_time ({}) done'.format(datetime.datetime.now(), sleep_time))
    # locks.release()   释放锁 -- 如果不释放锁，后续的线程会一直被阻塞不能进入


def thread_run(sleep_list):
    """
    交替同步执行多线程
    :param sleep_list: 睡眠时间列表
    :return:
    """
    global locks
    locks = threading.Lock()
    threads = []
    start_time = datetime.datetime.now()

    # Insert all threads to threads list
    for i in sleep_list:
        t = threading.Thread(target=unit_test, args=(i,))
        threads.append(t)

    # Start all threads
    for thread in threads:
        thread.start()

    # Waiting all threads done
    for thread in threads:
        thread.join()

    end_time = datetime.datetime.now()
    print('所有线程结束，一共消耗{}秒钟'.format((end_time - start_time).seconds))


def main():
    sleep_list = [2, 4, 1]
    thread_run(sleep_list=sleep_list)


if __name__ == '__main__':
    main()
