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
    with open('{}.csv'.format(file_name), 'w', encoding='utf-8', newline='') as wf:
        # TODO 这个是字典格式的写入
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
    # 用pandas读取，返回一个CSV表格，并且有行数显示
    result = pandas.read_csv('{}.csv'.format(file_name))
    print(result)

    # 用CSV读取
    with open('{}.csv'.format(file_name), 'r', encoding='utf-8') as rf:
        # 读取CSV表格并返回所有行数据
        reader = csv.reader(rf)
        result = []
        for i in reader:
            result.append(i)
        return result


if __name__ == '__main__':
    msg = [{'name': 'evan', 'id': '66'}, {'name': 'jane', 'id': '99'}]
    write_csv_data(msg, headers=['name', 'id'])  # 写入CSV表格
    print(read_csv_data())  # 读取CSV表格
