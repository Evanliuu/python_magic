import threading
import datetime
import time


def unit_test(sleep):
    # locks.acquire()   获取锁 -- 获取锁之后，其他的线程在此等待
    print('start loop {}, '.format(sleep), datetime.datetime.now())
    time.sleep(sleep)
    print('loop {} down, '.format(sleep), datetime.datetime.now())
    # locks.release()   释放锁 -- 如果不释放锁，后续的线程会一直被阻塞不能进入


def thread_loop(sleep_list):
    global locks
    locks = threading.Lock()

    # 计算多线程总数量
    loops = range(len(sleep_list))
    threads = []

    start_time = datetime.datetime.now()
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
    print('所有线程结束，一共消耗{}秒钟'.format((end_time - start_time).seconds))


def main():
    sleep_list = [2, 4, 1]
    thread_loop(sleep_list=sleep_list)


if __name__ == '__main__':
    main()
