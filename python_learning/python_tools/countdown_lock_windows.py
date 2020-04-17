# -*- coding:utf-8 -*-
import time
from ctypes import *

__author__ = 'Evan'


def close_windows(close_time):
    """
    倒计时锁屏
    :param close_time: 锁屏倒计时间
    :return:
    """
    if close_time <= 0:
        raise ValueError('close time小于等于0，请重新输入')

    while int(close_time) > 0:
        print('倒计时: {}'.format(close_time))
        time.sleep(1)
        close_time -= 1
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


if __name__ == "__main__":
    close_windows(close_time=3)
