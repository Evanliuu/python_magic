"""
使用pxssh模块进行远程连接服务器
注意事项：
1. 确保本地机器和远程机器都开启ssh服务
2. 该模块不支持在Windows系统中使用（可以使用Linux系统来驱动该模块）
"""
# -*- coding:utf-8 -*-
import getpass
from pexpect import pxssh

__author__ = 'Evan'


def remote_connection():
    """
    使用ssh协议远程到指定服务器
    :return:
    """
    remote_machine = input('remote machine: ')
    username = input('username: ')
    password = input('password: ')
    # pasword = getpass.getpass('password: ')  # pycharm中无法使用此功能

    # 实例化pxssh，使用login进行远程登录
    s = pxssh.pxssh()
    # original_prompt参数为终止符，需要提供终止符响应命令结果，如：original_prompt='>' or original_prompt='#'
    s.login(remote_machine, username, password, original_prompt='[$#>]')  # original_prompt='[$#>]'表示匹配中括号内的任意字符

    s.sendline('ls -l')  # 发送命令
    s.prompt()  # 匹配终止符内的字符串，匹配到了则停止接受字符
    print(s.before)  # s.before为命令起始符到终止符中间的所有字符，即命令 'ls -l' 的执行结果

    s.logout()   # 退出ssh服务


if __name__ == '__main__':
    remote_connection()
