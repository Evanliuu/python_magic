# -*- coding:utf-8 -*-
from queue import Queue

__author__ = 'Evan'


def queue_usage(put_data):
    """
    Queue常用方法
    :param put_data: 放入的数据，列表或元组类型
    :return:
    """
    q = Queue(maxsize=3)  # 设置队列上限为3

    for each in put_data:
        print(f'添加({each})到队列')
        q.put(each)

    print(f'返回队列的大小: {q.qsize()}')
    print(f'判断队列是否为空: {q.empty()}')
    print(f'判断队列是否满了: {q.full()}')

    while not q.empty():
        print(f'取出：{q.get()}')
        q.task_done()  # 告诉队列，这个数据已经使用完毕

    q.join()  # 阻塞调用线程，直到队列中的所有任务被处理掉


if __name__ == '__main__':
    queue_usage(put_data=[1, 2, 3])
