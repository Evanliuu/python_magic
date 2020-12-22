# -*- coding:utf-8 -*-
"""
阻塞式TCP连接
"""
import time
import socket

__author__ = 'Evan'


SOCKET_IP = ('127.0.0.1', 6666)
BUFFER_SIZE = 1024
SOCKET_TIMEOUT_TIME = 60


def send_socket_info(handle, msg, side='server', do_encode=True, do_print_info=True):
    """
    发送socket info，并根据side打印不同的前缀信息
    :param handle: socket句柄
    :param msg: 要发送的内容
    :param side: 默认server端
    :param do_encode: 是否需要encode，默认True
    :param do_print_info: 是否需要打印socket信息，默认True
    :return:
    """
    if do_encode:
        handle.send(msg.encode())
    else:
        handle.send(msg)

    if do_print_info:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        if side == 'server':
            print(f'Server send --> {current_time} - {msg}')
        else:
            print(f'Client send --> {current_time} - {msg}')


def receive_socket_info(handle, expected_msg, side='server', do_decode=True, do_print_info=True):
    """
    循环接收socket info，判断其返回值，直到返回值出现为止，防止socket信息粘连，并根据side打印不同的前缀信息
    :param handle: socket句柄
    :param expected_msg: 期待接受的内容，如果接受内容不在返回结果中，一直循环等待，期待内容可以为字符串，也可以为多个字符串组成的列表或元组
    :param side: 默认server端
    :param do_decode: 是否需要decode，默认True
    :param do_print_info: 是否需要打印socket信息，默认True
    :return:
    """
    while True:
        if do_decode:
            socket_data = handle.recv(BUFFER_SIZE).decode()
        else:
            socket_data = handle.recv(BUFFER_SIZE)

        if do_print_info:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            if side == 'server':
                print(f'Server received ==> {current_time} - {socket_data}')
            else:
                print(f'Client received ==> {current_time} - {socket_data}')

        # 如果expected_msg为空，跳出循环
        if not expected_msg:
            break

        if isinstance(expected_msg, (list, tuple)):
            flag = False
            for expect in expected_msg:  # 循环判断每个期待字符是否在返回结果中
                if expect in socket_data:  # 如果有任意一个存在，跳出循环
                    flag = True
                    break
            if flag:
                break
        else:
            if expected_msg in socket_data:
                break
        time.sleep(3)  # 每隔3秒接收一次socket
    return socket_data


def start_server_socket():
    """
    启动服务端socket
    :return:
    """
    ip, port = SOCKET_IP
    server = socket.socket()  # 使用TCP方式传输
    server.bind((ip, port))  # 绑定IP与端口
    server.listen(5)  # 设置最大连接数为5
    print(f'服务端 {ip}:{port} 开启')

    # 不断循环，接受客户端请求
    while True:
        print('等待客户端连接...')
        conn, address = server.accept()  # 使用accept阻塞式等待客户端请求，如果多个客户端同时访问，排队一个一个进
        print(f'当前连接客户端：{address}')
        conn.settimeout(SOCKET_TIMEOUT_TIME)  # 设置服务端超时时间

        # 与客户端握手，达成一致
        receive_socket_info(handle=conn, expected_msg='客户端已就绪')
        send_socket_info(handle=conn, msg='服务端已就绪')

        # 不断接收客户端发来的消息
        while True:
            socket_data = receive_socket_info(handle=conn, expected_msg='')
            if 'quit' in socket_data:
                send_socket_info(handle=conn, msg='quit')
                break

            answer = input('请回复客户端的信息：')
            send_socket_info(handle=conn, msg=answer)

        # 断开socket连接
        conn.close()
        print(f'与客户端 {ip}:{port} 断开连接')


if __name__ == '__main__':
    start_server_socket()  # 启动服务端socket
