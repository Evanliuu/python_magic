"""
强制结束线程方法：
1> 使用stop_thread函数关闭指定的单个线程
2> 设置当前函数为守护进程，函数结束后会关闭所有的子线程 --> Set daemon=True
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

    def test_2(self, times):
        time.sleep(times)
        print('times: {}'.format(times))

    def main(self):
        # 设置主线程
        self.threads = threading.Thread(target=self._main, args=())
        self.threads.start()

    def _main(self):
        print('Use daemon function')
        threads = []
        for i in range(20):
            # 开启20个子线程
            t = threading.Thread(target=self.test_2, args=(i, ))
            t.daemon = True  # 设置当前函数为守护进程
            threads.append(t)

        for i in threads:
            i.start()

        for i in threads:
            i.join()
        print('Threads have been stopped')


if __name__ == "__main__":
    # use_stop_thread_function()
    # ————分割线————
    use_daemon_funcion = UseDaemonFunction()
    use_daemon_funcion.main()  # 执行20个子线程

    time.sleep(5)
    # 杀死主线程，所有的子线程都会被关闭
    stop_thread(tid=use_daemon_funcion.threads)
    print('All done')
