# -*- coding:utf-8 -*-
import socket

__author__ = 'Evan'


REMOTE_IP = ('127.0.0.1', 6666)
BUFFER_SIZE = 1024
SOCKET_TIMEOUT_TIME = 60


def start_client_socket():
    """
    启动客户端UDP Socket
    :return:
    """
    ip, port = REMOTE_IP
    client = socket.socket(type=socket.SOCK_DGRAM)  # 使用TCP方式传输
    print(f'开始连接服务端 {ip}:{port} ...')
    client.connect((ip, port))  # 连接远程服务端
    print(f'连接服务端 {ip}:{port} 成功')

    # 与服务端交互
    while True:
        answer = input('请输入要发送给服务端的信息：')
        client.sendto(answer.encode(), REMOTE_IP)  # 使用sendto发送UDP消息，address填入服务端IP和端口
        if 'quit' in answer:
            break

    # 断开socket连接
    client.close()
    print(f'与服务端 {ip}:{port} 断开连接')


if __name__ == '__main__':
    start_client_socket()  # 启动客户端socket
