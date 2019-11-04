# -*- coding:utf-8 -*-
import pyodbc
import time
import logging
import os
import json
import re
import threading

from xmlrpc.server import SimpleXMLRPCServer

__author__ = 'Evan'


# Logging parameter
RECORD_LOG_FILE_PATH = './apollo_automation_logs.txt'
LOG_FORMAT_INFO = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

# logging module initialize
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Set the ability to write files
fh = logging.FileHandler(RECORD_LOG_FILE_PATH, mode='a')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(LOG_FORMAT_INFO))
logger.addHandler(fh)
# Set the ability to print log messages
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter(LOG_FORMAT_INFO))
logger.addHandler(ch)


class ApolloAutomation(object):

    def __init__(self, access_table_path='', table_name=''):
        # Access table parameter
        self.access_table_path = access_table_path
        self.table_name = table_name
        # CPP parameter
        self.cpp_data_file = 'cpp_automated_data.json'
        self.apollo_test_result_directory = 'apollo_test_result'
        # Apollo parameter
        self.apollo_target_path = '/tftpboot/'
        self.apollo_account = 'gen-apollo'
        self.apollo_password = 'Ad@pCr01!'

    def transfer_file_to_apollo(self, remote_machine, local_file_path, target_path, first_connection=False):
        """
        The feature use the PSCP command for file transfer to the remote apollo server
        :param remote_machine: Fill in the remote apollo server name
        :param local_file_path: Fill in the path of the local file to be transferred
        :param target_path: Fill in the placement file path for the Apollo server
        :param first_connection: The server needs to be set to True for the first connection
        :return:
        """
        if first_connection:
            cmd1 = r'echo y|pscp {} {}@{}:{}'.format(local_file_path, self.apollo_account,
                                                     remote_machine, target_path)
            os.system(cmd1)
        # Transfer the local file to the Apollo server
        cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(self.apollo_password, local_file_path, self.apollo_account,
                                                  remote_machine, target_path)
        os.system(cmd2)
        logger.debug('Transfer file to apollo server ({}) successful'.format(remote_machine))

    def write_json_file(self, content):
        """
        Write the json file
        :param content: Fill in the information to be written
        :return:
        """
        with open(self.cpp_data_file, 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(content, ensure_ascii=False, indent=2) + '\n')
        logger.debug('Write json file successful')

    def read_access_table(self):
        """
        Connect to Microsoft's access tables and return data
        :return: first row data or None
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        try:
            # Query all data in the table
            data_list = [data for data in crsr.execute("SELECT * from {}".format(self.table_name))]
            if data_list:
                cpp_data = dict()
                # result[0] is the first row data
                cpp_data['machine'] = data_list[0][0]
                cpp_data['cell'] = data_list[0][1]
                cpp_data['sn'] = data_list[0][2]
                cpp_data['pn'] = data_list[0][3]
                # Delete the captured row data
                crsr.execute("DELETE FROM {} WHERE machine='{}'".format(self.table_name, cpp_data['machine']))
                # Submit changes
                crsr.commit()
                result = cpp_data
            else:
                result = None
        finally:
            crsr.close()
            cnxn.close()
        return result

    def update_access_table(self, machine, container, test_status):
        """
        Connect to Microsoft's access table and update the data
        :param machine: Enter the name of the machine whose state you want to modify
        :param container: Fill in the machine's container number
        :param test_status: Fill in the machine's test status
        :return:
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        try:
            # Updates the state of the specified server and container
            crsr.execute("UPDATE {} SET status='{}' WHERE machine='{}' and cell='{}'".format
                         (self.table_name, test_status, machine, container))
            # Submit changes
            crsr.commit()
        finally:
            crsr.close()
            cnxn.close()
        logger.debug('The container {} status of the {} server was successfully set to {},'
                     ' Number of modifications: {}'.format(container, machine, test_status, crsr.rowcount))

    @staticmethod
    def read_local_ip_address():
        # Read the local IP address
        configurations = os.popen('ipconfig')
        result = re.search(r'IPv4.+? : (10.1.1.\d+)', configurations.read())
        if result:
            ip_address = result.groups()[0]
            logger.debug('Read the local ip address: {}'.format(ip_address))
            return ip_address
        else:
            raise ValueError('Read the local ip address error, Please check!')

    def write_test_result(self, apollo_test_result=''):
        """
        Write the test results transferred from the Apollo server into the local apollo_test_result directory
        :param apollo_test_result: Fill in the apollo test result
        :return:
        """
        apollo_test_result_path = os.path.join(os.getcwd(), self.apollo_test_result_directory)
        if not os.path.exists(apollo_test_result_path):
            os.mkdir(self.apollo_test_result_directory)

        os.chdir(apollo_test_result_path)
        with open('{}'.format(apollo_test_result), 'w') as wf:
            wf.write('{}'.format(apollo_test_result))
        logger.debug('Write apollo test result successful, test result:\n{}'.format(apollo_test_result))

    def setup_socket_server(self, ip_address='', port=9010):
        """
        register a function to respond to XML-RPC requests and start XML-RPC server
        :param ip_address: Fill in the server ip address
        :param port: Fill in the server port
        :return:
        """
        # If the ip_address parameter is null, read the local IP address for use
        ip_address = ip_address or self.read_local_ip_address()
        try:
            # Start the xml-rpc socket service
            server = SimpleXMLRPCServer((ip_address, port))
            logger.debug('Server {} Listening on port {} ...'.format(ip_address, port))
            server.register_instance(ApolloAutomation())
            server.serve_forever()
        except Exception as ex:
            raise Exception('Setup socket server error:\n{}'.format(ex))

    def send_data_to_apollo(self):
        """
        While the loop scans the data in the Access table, if any, it will transfer the data to the Apollo server
        :return:
        """
        while True:
            try:
                received = self.read_access_table()
                if received:
                    logger.info('Received the table ({}) information:\n{}'.format(self.table_name, received))
                    # Write the automated data transfer to json file
                    self.write_json_file(content=received)
                    # Transfer the json file to the corresponding apollo server
                    self.transfer_file_to_apollo(remote_machine=received['machine'],
                                                 local_file_path=self.cpp_data_file,
                                                 target_path=self.apollo_target_path,
                                                 first_connection=True)
                    time.sleep(1)
                else:
                    time.sleep(1)
            except Exception as ex:
                logger.exception(ex)
                time.sleep(1)

    def update_test_results(self):
        """
        Accept the returned data from the apollo server and update it to the access data table
        :return:
        """
        while True:
            try:
                # TODO need more function
                received = self.read_access_table()
                if received:
                    self.update_access_table(machine='', container='', test_status='')
                    time.sleep(1)
                else:
                    time.sleep(1)
            except Exception as ex:
                logger.exception(ex)
                time.sleep(1)


def main(access_table_path, table_name):
    """
    Connect to the access table to search for data and transfer it to the Apollo server, and update test results
    :param access_table_path: Fill in the access table path
    :param table_name: Fill in the Access table name
    :return:
    """
    handle = ApolloAutomation(access_table_path=access_table_path, table_name=table_name)
    threads = []

    # multi-threaded setup
    send_data_to_apollo = threading.Thread(target=handle.send_data_to_apollo, args=())
    setup_socket_server = threading.Thread(target=handle.setup_socket_server, args=())
    update_test_results = threading.Thread(target=handle.update_test_results, args=())

    # Add multi-threaded to threads list
    for t in [send_data_to_apollo, setup_socket_server, update_test_results]:
        threads.append(t)

    # start all threads
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    tablePath = r'D:\Application\RobotWebService\RobotWebService\template.mdb'
    tableName = 'tbl_CCDScanData'
    main(access_table_path=tablePath, table_name=tableName)
