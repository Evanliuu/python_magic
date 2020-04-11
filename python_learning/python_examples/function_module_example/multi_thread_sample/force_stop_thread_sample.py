"""
强制结束线程方法：
1> 使用stop_thread函数关闭指定的单个线程
2> 设置守护进程，守护进程结束后会关闭所有的子线程 --> Set daemon=True
"""
# -*- coding:utf-8 -*-
import threading
import time
import inspect
import ctypes


def stop_thread(tid, exctype=SystemExit):
    tid = ctypes.c_long(tid.ident)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("Invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def use_stop_thread_function():
    def test_1():
        while True:
            print('-------')
            time.sleep(1)

    print('Use stop thread function')
    t = threading.Thread(target=test_1)
    t.start()
    time.sleep(5)
    stop_thread(tid=t)
    print('Threads have been stopped')


class UseDaemonFunction(object):

    def __init__(self):
        self.stop_flag = False

    def test_2(self, times):
        time.sleep(times)
        print('times: {}'.format(times))
        if times == 3:  # If times equals 3, exit the daemon
            self.stop_flag = True

    def main(self):
        print('Use daemon function')
        threads = []
        for i in range(10):
            t = threading.Thread(target=self.test_2, args=(i, ))
            t.daemon = True
            threads.append(t)

        for i in threads:
            i.start()

        while True:
            if self.stop_flag:
                break
        print('Threads have been stopped')


if __name__ == "__main__":
    use_stop_thread_function()
    # ————分割线————
    use_daemon_funcion = UseDaemonFunction()
    use_daemon_funcion.main()
