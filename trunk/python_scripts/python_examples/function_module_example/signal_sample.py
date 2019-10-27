#!/usr/local/bin/python2.7
import signal
import time
import datetime


def signal_decorator(time_out=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # callback function
            def my_handle(*args):
                print('args: {}'.format(args))
                print('time out!')

            # TODO signal.SIGALRM 只能在Linux端使用
            signal.signal(signal.SIGALRM, my_handle)
            # 设置监听时间，如果func运行时间超过设定的time_out时间就会被强制中断，并执行 "my_handle" 函数
            signal.alarm(time_out)

            try:
                func(*args, **kwargs)
            finally:
                signal.alarm(0)  # Disable signal function
        return wrapper
    return decorator


@signal_decorator(time_out=2)
def main():
    print(datetime.datetime.now())
    time.sleep(5)


if __name__ == '__main__':
    main()
