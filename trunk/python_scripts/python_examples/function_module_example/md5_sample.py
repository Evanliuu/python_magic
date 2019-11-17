# -*- coding:utf-8 -*-
import hashlib


def get_file_md5(path):
    """
    打开文件读取MD5值
    :param path: 文件的所在路径
    :return:
    """
    with open(path, 'r') as file:
        data = file.read()

    diff_check = hashlib.md5()
    diff_check.update(data.encode())
    md5_code = diff_check.hexdigest()
    return md5_code


if __name__ == '__main__':
    md5_str = get_file_md5(path=r'C:\Users\evaliu\Desktop\sample.txt')
    print(md5_str)
