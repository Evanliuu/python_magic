# -*- coding:utf-8 -*-
from xmlrpc.client import ServerProxy


class SocketClient(object):

    def __init__(self, ip_address, port=6666):
        # Connect to the specified rpc-socket server
        self.proxy = ServerProxy('http://%s:%s/' % (ip_address, port), allow_none=True)
        print('Connect to {}:{} successful'.format(ip_address, port))

    def get_server_host_name(self):
        """
        Calls server-side functions
        :return:
        """
        host_name = self.proxy.get_server_host_name()
        print('Received the server host name: {}'.format(host_name))


if __name__ == '__main__':
    client = SocketClient(ip_address='10.28.205.207')
    client.get_server_host_name()
