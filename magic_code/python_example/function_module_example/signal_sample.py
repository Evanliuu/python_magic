import signal
import time
import datetime


def my_handle(*args):
    print('time out!')


# TODO signal.SIGALRM 只能在Linux端使用
signal.signal(signal.SIGALRM, my_handle)
# 设置监听时间，如果程序运行时间超过2秒还没结束就会执行 "my_handle" 函数
signal.alarm(2)

# Running
print(datetime.datetime.now())
time.sleep(5)
