# -*- coding:utf-8 -*-
"""
非阻塞式TCP连接
"""
import time
import socketserver

__author__ = 'Evan'


SOCKET_IP = ('127.0.0.1', 6666)
BUFFER_SIZE = 1024
SOCKET_TIMEOUT_TIME = 60


class UnblockSocketServer(socketserver.BaseRequestHandler):
    # 继承socketserver.BaseRequestHandler类
    # 首先执行setup方法，然后执行handle方法，最后执行finish方法
    # 如果handle方法报错，则会跳过
    # setup与finish无论如何都会执行
    # 一般只定义handle方法即可

    def setup(self):
        print('开启非阻塞式连接...')

    @staticmethod
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

    @staticmethod
    def receive_socket_info(handle, expected_msg, side='server', do_decode=True, do_print_info=True):
        """
        循环接收socket info，判断其返回值，直到指定的值出现为止，防止socket信息粘连，并根据side打印不同的前缀信息
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

    def handle(self):
        """
        所有和客户端交互的操作写在这里
        :return:
        """
        conn = self.request  # 获取socket句柄

        # 与客户端握手，达成一致
        self.receive_socket_info(handle=conn, expected_msg='客户端已就绪')
        self.send_socket_info(handle=conn, msg='服务端已就绪')

        # 不断接收客户端发来的消息
        while True:
            socket_data = self.receive_socket_info(handle=conn, expected_msg='')
            if 'quit' in socket_data:
                self.send_socket_info(handle=conn, msg='quit')
                break

            answer = input('请回复客户端的信息：')
            self.send_socket_info(handle=conn, msg=answer)

        # 断开socket连接
        conn.close()

    def finish(self):
        print('连接关闭')


def main():
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(SOCKET_IP, UnblockSocketServer)
    # 开启异步多线程，等待连接
    server.timeout = SOCKET_TIMEOUT_TIME  # 设置服务端超时时间
    print(f'服务端 {SOCKET_IP[0]}:{SOCKET_IP[1]} 开启')
    server.serve_forever()  # 永久运行


if __name__ == '__main__':
    main()
