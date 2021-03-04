# -*- coding:utf-8 -*-
import socket

__author__ = 'Evan'


SOCKET_IP = ('127.0.0.1', 6666)
BUFFER_SIZE = 1024


def start_server_socket():
    """
    启动服务端UDP Socket
    :return:
    """
    ip, port = SOCKET_IP
    server = socket.socket(type=socket.SOCK_DGRAM)  # 使用UDP方式传输
    server.bind((ip, port))  # 绑定IP与端口
    print(f'服务端 {ip}:{port} 开启')

    # 不断循环，接受客户端发来的消息
    while True:
        socket_data, address = server.recvfrom(BUFFER_SIZE)
        print('收到客户端 -> {} 发来的消息: {}'.format(address, socket_data.decode()))


if __name__ == '__main__':
    start_server_socket()
