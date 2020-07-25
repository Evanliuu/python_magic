# -*- coding:utf-8 -*-
import json

__author__ = 'Evan'


def write_json_data(write_info, file_name='json_file'):
    """
    写入JSON数据
    :param write_info: 要写入的字符串
    :param file_name: 文件名称
    :return:
    """
    with open('{}.json'.format(file_name), 'w', encoding='utf-8') as wf:
        # 将Python对象序列化为JSON中的字符串对象
        # 如果有中文ensure_ascii要设置为False
        # indent代表缩进字符个数
        wf.write(json.dumps(write_info, ensure_ascii=False, indent=2) + '\n')


def read_json_data(file_name='json_file'):
    """
    读取JSON数据
    :param file_name: json文件名称
    :return:
    """
    print(json.load(open('{}.json'.format(file_name))))  # 使用load方法接受一个文件句柄

    with open('{}.json'.format(file_name), 'r', encoding='utf-8') as rf:
        # 将JSON中的字符串对象反序列化为Python对象
        json_dict = json.loads(rf.read())  # 使用loads方法接受一个JSON字符串
        return json_dict


if __name__ == '__main__':
    msg = {'name': 'Evan'}
    write_json_data(msg)  # 写入json
    read_json_data()  # 读取json
