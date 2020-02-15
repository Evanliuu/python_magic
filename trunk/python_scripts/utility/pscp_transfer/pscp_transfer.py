# -*- coding:utf-8 -*-
import os
import threading

__author__ = 'Evan'


def file_transfer(remote_machine, transfer_config, first_connection=True):
    """
    此函数用于在同一个网段内传输文件
    此函数只能在Windows系统上使用，并且需要在Windows上装好PSCP控件
    :param remote_machine: 远程机器名称
    :param transfer_config: 传输配置信息
    :param first_connection: 第一次连接没有传输过的机器会询问"Store key in cache? (y/n)", 此时要输入y，否则会传输失败
    :return:
    """
    username = str(transfer_config['username']) or 'evanliu'
    password = str(transfer_config['password']) or 'Cisco321!'
    transfer_file_path = str(transfer_config['transfer_file_path'])
    target_file_path = str(transfer_config['target_file_path']) or r'C:\Users\evaliu\Desktop\\'
    whether_transfer_to_local = False if str(transfer_config['whether_transfer_to_local']).upper() == 'N' else True

    print('\nTransfer configuration:')
    print('****************************************************')
    print('remote_machine: {}'.format(remote_machine))
    print('username: {}'.format(username))
    print('password: {}'.format(password))
    print('transfer_file_path: {}'.format(transfer_file_path))
    print('target_file_path: {}'.format(target_file_path))
    print('whether_transfer_to_local: {}'.format(whether_transfer_to_local))
    print('****************************************************')

    # 将远程机器的文件传输到本地
    if whether_transfer_to_local:
        if first_connection:
            # 输入y保存密钥
            first_cmd_line = r'echo y|pscp {}@{}:{} {}'.format(username, remote_machine, transfer_file_path, target_file_path)
            os.system(first_cmd_line)
        cmd_line = r'echo {}|pscp {}@{}:{} {}'.format(password, username,
                                                      remote_machine, transfer_file_path, target_file_path)

    # 将本地的文件传输到远程机器
    else:
        if first_connection:
            # 输入y保存密钥
            first_cmd_line = r'echo y|pscp {} {}@{}:{}'.format(transfer_file_path, username, remote_machine, target_file_path)
            os.system(first_cmd_line)
        cmd_line = r'echo {}|pscp {} {}@{}:{}'.format(password, transfer_file_path,
                                                      username, remote_machine, target_file_path)
    # 开始传输文件
    os.system(cmd_line)


def ask_transfer_config(machine):
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
    print('Current remote machine: {}'.format(machine))
    for key in ask_info:
        ask_info[key] = input(ask_info[key])
    return ask_info


def main(machine_list):
    """
    多线程传输文件
    :param machine_list: 机器名列表
    :return:
    """
    threads = []
    for each_machine in machine_list:
        transfer_config = ask_transfer_config(each_machine)
        t = threading.Thread(target=file_transfer, args=(each_machine, transfer_config))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('All servers have been transferred')


if __name__ == '__main__':
    # TODO 填入要传输的机器名
    machine_info = [
        'fxcavp1017',
    ]
    main(machine_list=machine_info)
