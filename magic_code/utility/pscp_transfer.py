import os
import threading


def file_transfer(machine, username='gen-apollo', password='Ad@pCr01!', file_path=r'C:\Users\evaliu\Desktop\123.txt'):
    """

    :param machine: 传输的服务器名
    :param username: 连接服务器的用户名
    :param password: 连接服务器的密码
    :param file_path: 需要传输的文件路径
    :return:
    """
    # 切换到pscp.exe的存放路径下
    os.chdir(r'C:\Program Files\PuTTY')

    # 执行pscp文件传输命令: 第一次连接会询问"Store key in cache? (y/n)"，此时要输入y
    cmd1 = r'echo y|pscp {0} {1}@{2}:/tftpboot/' \
        .format(file_path, username, machine)
    os.system(cmd1)

    # 执行pscp文件传输命令: 第二次连接直接输入密码
    cmd2 = r'echo {0}|pscp {1} {2}@{3}:/tftpboot/'\
        .format(password, file_path, username, machine)
    os.system(cmd2)


def main(machines):
    """

    :param list machines: 提供要传输的服务器名列表
    :return:
    """
    loops = range(len(machines))
    threads = []

    # 启用多线程传输文件
    for machine in machines:
        print('Now start transferring files to {} server...'.format(machine))
        t = threading.Thread(target=file_transfer, args=(machine,))
        threads.append(t)

    for i in loops:
        threads[i].start()

    for i in loops:
        threads[i].join()
    print('All servers have been transferred')


if __name__ == '__main__':
    machines = [
        'fxcavp375',
        'fxcavp376',
        'fxcavp377',
    ]
    main(machines)
