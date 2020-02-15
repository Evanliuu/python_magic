# -*- coding:utf-8 -*-

__author__ = 'Evan'


def ask_transfer_config():
    """
    询问传输配置信息
    1. 是否传输到本地
    2. 待传输文件路径
    3. 传输目标路径
    4. 用户名
    5. 密码
    :return:
    """
    ask_info = {
        'whether_transfer_to_local': '是否传输到本地(Y/N，默认Y): ',
        'transfer_file_path': '待传输文件路径: ',
        'target_file_path': '传输目标路径(如果是传输到本地则默认到本地桌面): ',
        'username': '用户名: ',
        'password': '密码: '
    }
    for key in ask_info:
        ask_info[key] = input(ask_info[key])
    print('Ask result: {}'.format(ask_info))
    return ask_info


ask_transfer_config()
