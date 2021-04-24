# -*- coding:utf-8 -*-
from collections import deque

__author__ = 'Evan'


def deque_example(put_data):
    """
    Deque，双端队列
    :param put_data: 放入的数据，列表或元组类型
    :return:
    """
    assert isinstance(put_data, (list, tuple)), '请传入列表或元组类型的put_data'

    # 放入数据到双端队列
    dq = deque(put_data)
    print(f'当前队列所有数据：{dq}')

    # 增加数据到队左
    dq.appendleft('aa')
    print(f'当前队列所有数据：{dq}')

    # 增加数据到队尾
    dq.append('cc')
    print(f'当前队列所有数据：{dq}')

    print(f'移除队尾，并返回：{dq.pop()}')
    print(f'移除队左，并返回：{dq.popleft()}')

    print(f'当前队列所有数据：{dq}')


if __name__ == '__main__':
    deque_example(put_data=['a', 'b', 'c'])
