# -*- coding:utf-8 -*-
from queue import Queue

__author__ = 'Evan'


def fifo_queue(put_data):
    """
    FIFO，先进先出队列
    :param put_data: 放入的数据，列表或元组类型
    :return:
    """
    assert isinstance(put_data, (list, tuple)), '请传入列表或元组类型的put_data'

    # maxsize为队列数据上限，小于或等于0则不限制，当容器数量大于这个数则阻塞，直到队列中的数据被消掉
    q = Queue(maxsize=0)

    # 依次写入队列数据
    for each in put_data:
        print(f'添加({each})到队列')
        q.put(each)

    print(f'当前队列所有数据：{q.queue}')

    # 逐次取出所有数据
    while not q.empty():
        print(f'取出：{q.get()}')

    print(f'当前队列所有数据：{q.queue}')


if __name__ == '__main__':
    fifo_queue(put_data=[3, 2, 1])
