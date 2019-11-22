# -*- coding:utf-8 -*-
import os
import re

from xmlrpc.server import SimpleXMLRPCServer


class ServiceFunction(object):
    """
    This class holds server-side execution functions, The function must have a return value
    """
    @staticmethod
    def get_windows_host():
        """
        Gets the host name of the local computer
        :return: get hostname to client side
        """
        result = os.popen('ipconfig /all')
        read_info = re.search(r': (\w+)', result.readlines()[3])
        if read_info:
            host = read_info.group(1)
        else:
            host = 'Not found windows host'
        return host


class SocketServer(object):

    def __init__(self, ip_address='', port=6666):
        self.ip_address = ip_address
        self.port = port

    @staticmethod
    def read_local_ip_address():
        ip_config = os.popen('ipconfig')
        result = re.search(r'IPv4.+? : (\d+?\.\d+?\.\d+?\.\d+)', ip_config.read())
        if result:
            ip_address = result.group(1)
            print('Read the local ip address: {}'.format(ip_address))
            return ip_address
        else:
            raise ValueError('Read the local ip address error, Please check!')

    def setup_socket_server(self):
        """
        register a function to respond to XML-RPC requests and start XML-RPC server
        :return:
        """
        # If the ip_address parameter is null, read the local IP address for use
        ip_address = self.ip_address or self.read_local_ip_address()
        try:
            # Start the xml-rpc socket service
            service = SimpleXMLRPCServer((ip_address, self.port))
            print('Server {} Listening on port {} ...'.format(ip_address, self.port))

            # service.register_function(function)  # Enable a function service
            service.register_instance(ServiceFunction())  # Open a class service
            service.serve_forever()  # performs a permanent run
        except Exception as ex:
            raise Exception('Setup socket server error:\n{}'.format(ex))


if __name__ == '__main__':
    server = SocketServer(port=6666)
    server.setup_socket_server()
