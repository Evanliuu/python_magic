"""
The file is located on a Windows central control machine at BPM2 automation station in Barbados
This program will start three multi-threads:
1. Start an rpc-socket service that listens for all incoming data from the Apollo server
2. Read the local access data table to fetch each row of data
3. Update the received Apollo server data into the access data table
python version: 3.7
"""
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

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class ApolloAutomation(object):
    # CPP machine constants
    cpp_data_file = 'cpp_automated_data.json'
    cpp_data_path = os.path.join(os.getcwd(), cpp_data_file)
    apollo_test_status_directory = 'apollo_test_status'
    apollo_test_status_path = os.path.join(os.getcwd(), apollo_test_status_directory)
    # Apollo machine constants
    apollo_target_path = '/tftpboot/'
    apollo_account = 'gen-apollo'
    apollo_password = 'Ad@pCr01!'

    def __init__(self, access_table_path='', table_names=None):
        """
        Access table parameter initialization
        :param str access_table_path: Fill in the access table path
        :param tuple table_names: Fill in the Access table names
        """
        self.access_table_path = access_table_path
        if table_names:
            self.ccd_scan_table_name, self.link_position_table_name = table_names

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
        with open(self.cpp_data_path, 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(content, ensure_ascii=False, indent=2) + '\n')
        logger.debug('Write json file successful')

    def read_access_table(self):
        """
        Connect to the access table to read the first row data
        :return: first row data or None
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        try:
            # Query all data in the table
            data_list = [data for data in crsr.execute("SELECT * from {}".format(self.ccd_scan_table_name))]
            if data_list:
                cpp_data = dict()
                # Fetch the first row data
                cpp_data['machine'] = data_list[0][0]
                cpp_data['cell'] = data_list[0][1]
                cpp_data['sn'] = data_list[0][2]
                cpp_data['pn'] = data_list[0][3]
                # Delete the captured row data
                crsr.execute("DELETE FROM {} WHERE machine='{}'".format(self.ccd_scan_table_name, cpp_data['machine']))
                # Submit changes
                crsr.commit()
                result = cpp_data
            else:
                result = None
        finally:
            crsr.close()
            cnxn.close()
        return result

    def update_access_table(self, machine, cell, test_status):
        """
        Connect to Microsoft's access table and update the data
        :param machine: Enter the name of the machine whose state you want to update
        :param cell: Fill in the machine's container number
        :param test_status: Fill in the machine's test status
        :return: 'PASS' or 'Not data found'
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        try:
            check_list = [i for i in crsr.execute("SELECT * from {} WHERE machine='{}' and cell='{}'"
                                                  .format(self.link_position_table_name, machine, cell))]
            if not check_list:
                logger.warning('No (Cell {}) data information for ({}) server was found in the ({}) table,'
                               ' Please check!'.format(cell, machine, self.link_position_table_name))
                return 'Not data found'

            # Updates the state of the specified server and container
            crsr.execute("UPDATE {} SET passfail='{}' WHERE machine='{}' and cell='{}'".format
                         (self.link_position_table_name, test_status, machine, cell))
            # Submit changes
            crsr.commit()
        finally:
            crsr.close()
            cnxn.close()
        logger.debug('Change the (cell {}) status of the ({}) server to "{}" in the ({}) table, Number of updates: {}'
                     .format(cell, machine, test_status, self.link_position_table_name, crsr.rowcount))
        return 'PASS'

    @staticmethod
    def read_local_ip_address():
        ip_config = os.popen('ipconfig')
        result = re.search(r'IPv4.+? : (10.\d+.\d+.\d+)', ip_config.read())
        if result:
            ip_address = result.groups()[0]
            logger.debug('Read the local ip address: {}'.format(ip_address))
            return ip_address
        else:
            raise ValueError('Read the local ip address error, Please check!')

    @staticmethod
    def communication_test():
        """
        Apollo communication test
        :return:
        """
        return True

    def write_test_status_to_windows(self, apollo_test_status):
        """
        Write the test status transferred from the Apollo server into the local apollo_test_status directory
        :param str apollo_test_status: Fill in the apollo test status, The format must be "ApolloServerName_Cell_Status"
        :return:
        """
        if not os.path.exists(self.apollo_test_status_path):
            raise FileNotFoundError('Not found the Apollo_test_status directory in windows, Please check!')

        with open('{}.txt'.format(os.path.join(self.apollo_test_status_path, apollo_test_status)), 'w') as wf:
            wf.write('{}'.format(apollo_test_status))
        logger.debug('Write the apollo test status successful, test status is:\n{}'.format(apollo_test_status))
        return True

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
                    logger.info('Received the table ({}) information:\n{}'.format(self.ccd_scan_table_name, received))
                    # Write the automated data transfer to json file
                    self.write_json_file(content=received)
                    # Transfer the json file to the corresponding apollo server
                    self.transfer_file_to_apollo(remote_machine=received['machine'],
                                                 local_file_path=self.cpp_data_path,
                                                 target_path=self.apollo_target_path,
                                                 first_connection=True)
                else:
                    time.sleep(1)
            except Exception as ex:
                logger.exception(ex)
                time.sleep(1)

    def update_test_status(self):
        """
        Loop through the files under the local apollo_test_status path
        and update the data in the files to the access data table, if any
        :return:
        """
        while True:
            try:
                if not os.path.exists(self.apollo_test_status_path):
                    os.mkdir(self.apollo_test_status_path)
                    logger.debug('Create ({}) directory under {} path successfully'
                                 .format(self.apollo_test_status_directory, self.apollo_test_status_path))

                # Read the test status information from the apollo_test_status directory
                test_status_list = os.listdir(self.apollo_test_status_path)

                if test_status_list:
                    logger.debug('Read the file under path {}:\n{}'.format(self.apollo_test_status_path,
                                                                           test_status_list))
                    for file in test_status_list:
                        if re.match('fx.+?_.+?_.+?.txt', file):
                            logger.info('Captured file: {}'.format(file))
                            # Format to check
                            machine, cell, test_status = file.split('.txt')[0].split('_')
                            # Start updating the access data table
                            updated_status = self.update_access_table(machine=machine,
                                                                      cell=cell,
                                                                      test_status=test_status)
                            # Delete test status files whose status has been updated
                            if updated_status == 'PASS':
                                updated_file = os.path.join(self.apollo_test_status_path, file)
                                if os.path.exists(updated_file):
                                    os.remove(updated_file)
                                logger.debug('Delete {} successful'.format(updated_file))
                else:
                    time.sleep(1)
            except Exception as ex:
                logger.exception(ex)
                time.sleep(1)


def main(access_table_path, table_names):
    """
    Connect to the access data table to read the data and send it to the Apollo server,
    and receive the data from the Apollo server to update it to the access data table
    :param str access_table_path: Fill in the access table path
    :param tuple table_names: Fill in the Access table names
    :return:
    """
    handle = ApolloAutomation(access_table_path=access_table_path, table_names=table_names)
    threads = []

    # Multi-threaded setup
    setup_socket_server = threading.Thread(target=handle.setup_socket_server, args=())
    send_data_to_apollo = threading.Thread(target=handle.send_data_to_apollo, args=())
    update_test_status = threading.Thread(target=handle.update_test_status, args=())

    # Add multi-threaded to threads list
    for t in [setup_socket_server, send_data_to_apollo, update_test_status]:
        threads.append(t)

    # Start all threads
    for thread in threads:
        thread.start()


if __name__ == '__main__':
    tablePath = r'D:\Application\RobotWebService\RobotWebService\template.mdb'
    tableNames = ('tbl_CCDScanData', 'tbl_linkPosition')
    main(access_table_path=tablePath, table_names=tableNames)
