import os
import threading


def file_transfer(machine, user_info=('username', 'password'),
                  file_path=r'C:\Users\evaliu\Desktop\123.txt', target_path='/tftpboot/'):
    """
    此功能使用PSCP命令将本地文件传输到远程的Linux服务器上
    :param machine: 目标服务器
    :param user_info: 目标服务器登陆账户和密码
    :param file_path: 传输的文件路径
    :param target_path: 目标服务器的存放路径
    :return:
    """
    username = user_info[0]
    password = user_info[1]

    # TODO 执行PSCP文件传输命令: 第一次连接会询问"Store key in cache? (y/n)"，此时要输入y
    # cmd1 = r'echo y|pscp {} {}@{}:{}'.format(file_path, username, machine, target_path)
    # os.system(cmd1)

    # 执行PSCP文件传输命令: 第二次连接直接输入密码
    cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(password, file_path, username, machine, target_path)
    os.system(cmd2)


def main(machine_list):
    """

    :param list machine_list: 填入目标服务器列表
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
