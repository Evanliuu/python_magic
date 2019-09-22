import os
import threading


def file_transfer(machine, user_info=('username', 'password'), file_path=r'C:\Users\evaliu\Desktop\123.txt',
                  target_path='/tftpboot/', transfer_to_local=False, first_connection=False):
    """
    此功能使用PSCP命令与远程服务器进行文件传输
    :param machine: 远程服务器名称
    :param user_info: 远程服务器登陆账户名和密码
    :param file_path: 被传输的文件路径
    :param target_path: 传输文件的放置路径
    :param transfer_to_local: 如果为True则是从远程服务器传输文件到本地, False则是从本地传输文件到远程服务器
    :param first_connection: 第一次连接会询问"Store key in cache? (y/n)", 此时要输入y (第一次连接指定的服务器要打开，后续不用)
    :return:
    """
    username = user_info[0]
    password = user_info[1]

    # 将远程服务器的文件传输到本地
    if transfer_to_local:
        if first_connection:
            cmd1 = r'echo y|pscp {}@{}:{} {}'.format(username, machine, file_path, target_path)
            os.system(cmd1)

        # 输入密码开始传输文件
        cmd2 = r'echo {}|pscp {}@{}:{} {}'.format(password, username, machine, file_path, target_path)
        os.system(cmd2)

    # 将本地的文件传输到远程服务器
    else:
        if first_connection:
            cmd1 = r'echo y|pscp {} {}@{}:{}'.format(file_path, username, machine, target_path)
            os.system(cmd1)

        # 输入密码开始传输文件
        cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(password, file_path, username, machine, target_path)
        os.system(cmd2)


def main(machine_list):
    """

    :param list machine_list: 填入远程服务器列表
    :return:
    """
    loops = range(len(machine_list))
    threads = []

    # 启用多线程传输文件
    for machine in machine_list:
        print('Now start transferring files to {} server...'.format(machine))
        t = threading.Thread(target=file_transfer, args=(machine,))
        threads.append(t)

    for i in loops:
        threads[i].start()

    for i in loops:
        threads[i].join()
    print('All servers have been transferred')


if __name__ == '__main__':
    machine_list = [
        'fxcavp831',
    ]
    main(machine_list)
