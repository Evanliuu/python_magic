# -*- coding:utf-8 -*-
import csv
import pandas

__author__ = 'Evan'


def write_csv_data(write_info, file_name='csv_file', headers=None):
    """
    写入csv表格
    :param write_info: 要写入CSV表格的数据
    :param file_name: CSV表格名称
    :param headers: CSV表格的第一行表头
    :return:
    """
    # 取消多余的空白行: Python3.7是newline=''，Python2.7是用'wb'写入
    # 使用 encoding=utf-8-sig 可以防止写入中文乱码
    with open('{}.csv'.format(file_name), 'w', encoding='utf-8', newline='') as wf:
        # 这个是字典格式的写入
        dict_write = csv.DictWriter(wf, fieldnames=headers)
        dict_write.writeheader()  # 写入第一行的表头数据
        for i in write_info:
            dict_write.writerow(i)  # 循环写入每行数据
        # 同时写入多行数据
        dict_write.writerows(write_info)

        # TODO 这个是普通格式的写入
        """
        write = csv.writer(wf)
        msg = [['name', 'evan'], ['id', '66']]
        for i in msg:
            write.writerow(i)  # 循环写入每行数据
        # 同时写入多行数据
        write.writerows(msg)
        """


def read_csv_data(file_name='csv_file'):
    """
    读取csv表格
    :param file_name: CSV表格名称
    :return:
    """
    # 用pandas读取，返回一个二维数组
    result = pandas.read_csv('{}.csv'.format(file_name))
    print(result)

    # 用CSV读取
    with open('{}.csv'.format(file_name), 'r', encoding='utf-8') as rf:
        # 读取所有行数据
        # reader = csv.reader((line.replace('\0', '') for line in rf))  # 如果读取报错，使用这个
        data = list(csv.reader(rf))

    header, values = data[0], data[1:]  # 切分列索引和数据行
    print('读取每一列的数据：{}'.format({h: v for h, v in zip(header, zip(*values))}))
    return data  # 返回所有行的数据


if __name__ == '__main__':
    msg = [{'name': 'evan', 'id': '66'}, {'name': 'jane', 'id': '99'}]
    write_csv_data(msg, headers=['name', 'id'])  # 写入CSV表格
    print(read_csv_data())  # 读取CSV表格
