import threading
import datetime
import time
import multiprocessing


def sleep_test(sleep):
    # 执行测试
    print('start {} loop: '.format(sleep), datetime.datetime.now())
    time.sleep(sleep)
    print('loop {} done: '.format(sleep), datetime.datetime.now())


def thread_loop(index, sleep_list):
    # 添加多线程
    print('start thread {} time: '.format(index), datetime.datetime.now())
    loops = range(len(sleep_list))
    threads = []
    # insert all threads to threads list
    for i in sleep_list:
        t = threading.Thread(target=sleep_test, args=(i,))
        threads.append(t)

    # start all threads
    for i in loops:
        threads[i].start()

    # waiting all thread close
    for i in loops:
        threads[i].join()
    print('thread {} all done: '.format(index), datetime.datetime.now())


def main(sleep_list=None):
    for index, sleep in enumerate(sleep_list):
        # 添加多进程
        p = multiprocessing.Process(target=thread_loop, args=(index, sleep))
        p.start()
        print('process {} start'.format(index + 1))


if __name__ == '__main__':
    sleep_list = [
        [4, 3, 2],
        [7, 6, 5]
    ]
    main(sleep_list=sleep_list)
