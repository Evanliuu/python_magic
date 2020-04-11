"""
强制结束单个线程方法
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


def test():
    while True:
        print('-------')
        time.sleep(1)


if __name__ == "__main__":
    t = threading.Thread(target=test)
    t.start()
    time.sleep(5)

    print('Start stopping threads')
    stop_thread(tid=t)
    print('Threads have been stopped')
