# -*- coding:utf-8 -*-
import pyodbc
import time
import logging
import os
import json


RECORD_LOG_FILE_PATH = './read_access_table_logs.txt'
LOG_FORMAT_INFO = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
CPP_DATA_FILE = 'cpp_automated_data.json'
APOLLO_TARGET_PATH = '/tftpboot/'
APOLLO_ACCOUNT = 'gen-apollo'
APOLLO_PASSWORD = 'Ad@pCr01!'

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


class AccessHandle(object):

    def __init__(self, access_table_path, table_name):
        self.access_table_path = access_table_path
        self.table_name = table_name

    @staticmethod
    def transfer_file_to_apollo(machine, local_file_path, target_path, first_connection=False):
        """
        The feature use the PSCP command for file transfer to the remote apollo server
        :param machine: Fill in the remote apollo server name
        :param local_file_path: Fill in the path of the local file to be transferred
        :param target_path: Fill in the placement file path for the Apollo server
        :param first_connection: The server needs to be set to True for the first connection
        :return:
        """
        if first_connection:
            cmd1 = r'echo y|pscp {} {}@{}:{}'.format(local_file_path, APOLLO_ACCOUNT, machine, target_path)
            os.system(cmd1)
        # Transfer the local file to the Apollo server
        cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(APOLLO_PASSWORD, local_file_path, APOLLO_ACCOUNT, machine, target_path)
        os.system(cmd2)
        logger.debug('Transfer file to apollo server successful')

    @staticmethod
    def write_json_file(msg):
        with open('{}'.format(CPP_DATA_FILE), 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(msg, ensure_ascii=False, indent=2) + '\n')
        logger.debug('Write json file successful')

    def read_access_table(self):
        """
        Connect to Microsoft's Access tables and return data
        :return: list or None
        """
        cnxn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s' % (self.access_table_path,))
        crsr = cnxn.cursor()
        logger.debug('Connect to --> {} successful'.format(self.access_table_path))

        # Query all data in the table
        result = [data for data in crsr.execute("SELECT * from {}".format(self.table_name))]
        if result:
            cpp_data = dict()
            # result[0] is the first line
            cpp_data['machine'] = result[0][0]
            cpp_data['cell'] = result[0][1]
            cpp_data['sn'] = result[0][2]
            cpp_data['pn'] = result[0][3]

            # Delete the first row
            crsr.execute("DELETE FROM {} WHERE machine='{}'".format(self.table_name, cpp_data['machine']))
            # Submit changes
            crsr.commit()
            crsr.close()
            cnxn.close()
            return cpp_data
        else:
            return None


def main(access_table_path, table_name):
    """
    Connect to the access data table to fetch data
    :param access_table_path: Fill in the access table path
    :param table_name: Fill in the Access table name
    :return:
    """
    handle = AccessHandle(access_table_path=access_table_path, table_name=table_name)
    while True:
        try:
            received = handle.read_access_table()
            if received:
                logger.info('Received table information:\n{}'.format(received))

                # Write the automated data transfer to json file
                handle.write_json_file(msg=received)
                # Transfer the json file to the corresponding apollo server
                handle.transfer_file_to_apollo(machine=received['machine'],
                                               local_file_path=CPP_DATA_FILE,
                                               target_path=APOLLO_TARGET_PATH,
                                               first_connection=True)
                time.sleep(1)
            else:
                logger.warning('No data was found in the table ({}) under the ({}) path'.format(table_name,
                                                                                                access_table_path))
                time.sleep(1)
        except Exception as ex:
            logger.exception(ex)
            time.sleep(1)


if __name__ == '__main__':
    main(access_table_path=r'C:\Users\evaliu\Desktop\template.mdb', table_name='tbl_CCDScanData')
