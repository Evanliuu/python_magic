import signal
import time
import datetime


def signal_decorator(func):
    def wrapper(*args, **kwargs):
        def my_handle(*args):
            print('time out!')
            exit()

        # TODO signal.SIGALRM 只能在Linux端使用
        signal.signal(signal.SIGALRM, my_handle)
        # 设置监听时间，如果func运行时间超过2秒还没结束就会强制中断，并执行 "my_handle" 函数
        signal.alarm(2)

        try:
            func(*args, **kwargs)
        finally:
            signal.alarm(0)  # Disable signal function
    return wrapper


@signal_decorator
def main():
    print(datetime.datetime.now())
    time.sleep(5)


if __name__ == '__main__':
    main()
