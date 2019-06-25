import threading
import datetime
import time


def unit_test(sleep):
    # 执行测试
    print('start loop {}, '.format(sleep), datetime.datetime.now())
    time.sleep(sleep)
    print('loop {} down, '.format(sleep), datetime.datetime.now())


def thread_loop(sleep_list):
    start_time = datetime.datetime.now()
    # 计算多线程总数量
    loops = range(len(sleep_list))
    threads = []

    # insert all threads to threads list
    for i in sleep_list:
        t = threading.Thread(target=unit_test, args=(i,))
        threads.append(t)

    # start all threads
    for i in loops:
        threads[i].start()

    # waiting all thread close
    for i in loops:
        threads[i].join()

    end_time = datetime.datetime.now()
    print('所有线程结束，一共消耗{}秒钟'.format((end_time - start_time).seconds / 60))


def main():
    sleep_list = [2, 4, 1]
    thread_loop(sleep_list=sleep_list)


if __name__ == '__main__':
    main()
