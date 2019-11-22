# -*- coding:utf-8 -*-
from xmlrpc.client import ServerProxy


class SocketClient(object):

    def __init__(self, ip_address, port=6666):
        # Connect to the specified rpc-socket server
        self.proxy = ServerProxy('http://%s:%s/' % (ip_address, port), allow_none=True)
        print('Connect to ({}:{}) successful'.format(ip_address, port))

    def get_windows_host(self):
        """
        Calls server-side functions
        :return:
        """
        host_name = self.proxy.get_windows_host()
        return host_name


if __name__ == '__main__':
    client = SocketClient(ip_address='10.28.200.165')
    host = client.get_windows_host()
    print('From socket server host is {}'.format(host))
