import os
import threading


def file_transfer(remote_machine, account=('evanliu', 'Cisco321!'), file_path='/tftpboot/step.zip',
                  target_path=r'C:\Users\evaliu\Desktop\\', transfer_to_local=True, first_connection=True):
    """
    这个函数是用来在同一个局域网内传输文件的，
    此功能只能在Windows系统上使用，并且需要在Windows上装好PSCP控件
    :param remote_machine: 远程机器名称
    :param account: 登陆远程机器的用户名和密码
    :param file_path: 被传输的文件路径
    :param target_path: 传输文件的放置路径
    :param transfer_to_local: 如果为True则是从远程服务器传输文件到本地, False则是从本地传输文件到远程服务器
    :param first_connection: 第一次连接会询问"Store key in cache? (y/n)", 此时要输入y (第一次连接指定的服务器要打开，后续不用)
    :return:
    """
    username, password = account
    # 将远程服务器的文件传输到本地
    if transfer_to_local:
        if first_connection:
            cmd1 = r'echo y|pscp {}@{}:{} {}'.format(username, remote_machine, file_path, target_path)
            os.system(cmd1)

        # 输入密码开始传输文件
        cmd2 = r'echo {}|pscp {}@{}:{} {}'.format(password, username, remote_machine, file_path, target_path)
        os.system(cmd2)

    # 将本地的文件传输到远程服务器
    else:
        if first_connection:
            cmd1 = r'echo y|pscp {} {}@{}:{}'.format(file_path, username, remote_machine, target_path)
            os.system(cmd1)

        # 输入密码开始传输文件
        cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(password, file_path, username, remote_machine, target_path)
        os.system(cmd2)


def main(machine_info):
    """

    :param list machine_info: 填入远程服务器列表
    :return:
    """
    loops = range(len(machine_info))
    threads = []

    # 启用多线程传输文件
    for each_machine in machine_info:
        print('Now start transferring files to {} server...'.format(each_machine))
        t = threading.Thread(target=file_transfer, args=(each_machine,))
        threads.append(t)

    for i in loops:
        threads[i].start()

    for i in loops:
        threads[i].join()
    print('All servers have been transferred')


if __name__ == '__main__':
    machine_list = [
        'fxcavp1017',
    ]
    main(machine_info=machine_list)
