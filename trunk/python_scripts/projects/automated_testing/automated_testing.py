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
        Write json file
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
        # Query all data in the table
        result = [data for data in crsr.execute("SELECT * from {}".format(self.table_name))]
        if result:
            cpp_data = dict()
            # result[0] is the first row data
            cpp_data['machine'] = result[0][0]
            cpp_data['cell'] = result[0][1]
            cpp_data['sn'] = result[0][2]
            cpp_data['pn'] = result[0][3]
            # Delete the captured row data
            crsr.execute("DELETE FROM {} WHERE machine='{}'".format(self.table_name, cpp_data['machine']))
            # Submit changes
            crsr.commit()
            crsr.close()
            cnxn.close()
            return cpp_data
        else:
            return None

    def update_access_table(self, machine, status, container):
        """
        Connect to Microsoft's access table and modify the data
        :param status: Fill in the machine's immediate state
        :param machine: Enter the name of the machine whose state you want to modify
        :param container: Fill in the machine's container number
        :return:
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        # Updates the state of the specified server and container
        crsr.execute("UPDATE {} SET status={} WHERE machine={} and cell={}".format(self.table_name, status,
                                                                                   machine, container))
        # Submit changes
        crsr.commit()
        crsr.close()
        cnxn.close()
        logger.debug('The container {} status of the {} server was successfully set to {},'
                     ' Number of modifications: {}'.format(container, machine, status, crsr.rowcount))

    @staticmethod
    def read_local_ip_address():
        # Read the local IP address
        rsp = os.popen('ipconfig')
        result = re.search(r'IPv4 Address.+? : (10.1.1.\d+)', rsp.read())
        if result:
            logger.debug('Read the local ip address: {}'.format(result.groups()[0]))
            ip_address = result.groups()[0]
            return ip_address
        else:
            raise ValueError('Read the local ip address error, Please check!')

    @staticmethod
    def write_test_result(apollo_test_result=''):
        """
        Write the test results transferred from the Apollo server into the local apollo_test_result directory
        :param apollo_test_result: Fill in the apollo test result
        :return:
        """
        record_apollo_test_status_path = os.path.join(os.getcwd(), 'apollo_test_result')
        if not os.path.exists(record_apollo_test_status_path):
            os.mkdir('apollo_test_result')

        os.chdir(record_apollo_test_status_path)
        with open('{}'.format(apollo_test_result), 'w') as wf:
            wf.write('{}'.format(apollo_test_result))
        logger.debug('Write apollo test result successful, test result:\n{}'.format(apollo_test_result))

    @staticmethod
    def setup_socket_server(ip_address, port=9010):
        """
        register a function to respond to XML-RPC requests and start XML-RPC server
        :param ip_address: Fill in the server ip address
        :param port: Fill in the server port
        :return:
        """
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


def main(access_table_path, table_name):
    """
    Connect to the access table to search for data and transfer it to the Apollo server, and return test results
    :param access_table_path: Fill in the access table path
    :param table_name: Fill in the Access table name
    :return:
    """
    handle = ApolloAutomation(access_table_path=access_table_path, table_name=table_name)
    handle.send_data_to_apollo()


if __name__ == '__main__':
    tablePath = r'D:\Application\RobotWebService\RobotWebService\template.mdb'
    tableName = 'tbl_CCDScanData'
    main(access_table_path=tablePath, table_name=tableName)
