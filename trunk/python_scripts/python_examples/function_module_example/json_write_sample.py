# -*- coding:utf-8 -*-
import json


def write_json_data(write_info, file_name='json_file'):
    """
    写入JSON数据
    :param write_info: 要写入的字符串
    :param file_name: 文件名称
    :return:
    """
    with open('{}.json'.format(file_name), 'w', encoding='utf-8') as wf:
        # 将文本字符串转换为JSON对象，如果有中文ensure_ascii要设置为False，indent代表缩进字符个数
        wf.write(json.dumps(write_info, ensure_ascii=False, indent=2) + '\n')


def read_json_data(file_name='json_file'):
    """
    读取JSON数据
    :param file_name: json文件名称
    :return:
    """
    with open('{}.json'.format(file_name), 'r', encoding='utf-8') as rf:
        # 将JSON对象转换为字典
        json_dict = json.loads(rf.read())
        return json_dict


if __name__ == '__main__':
    msg = {'name': 'Evan'}
    write_json_data(msg)  # 写入json
    print(read_json_data())  # 读取json
