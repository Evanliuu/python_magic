# -*-coding:utf-8-*-
import pyodbc
import time
import logging
import os
import json

RECORD_FILE_PATH = './read_access_table_result.txt'
FORMAT_INFO = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

# logging init
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set the ability to write files
fh = logging.FileHandler(RECORD_FILE_PATH, mode='a')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(FORMAT_INFO))
logger.addHandler(fh)

# Set the ability to print log messages
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter(FORMAT_INFO))
logger.addHandler(ch)


class AccessHandle(object):

    def __init__(self, access_table_path, table_name):
        self.access_table_path = access_table_path
        self.table_name = table_name

    @staticmethod
    def transfer_file_to_apollo(machine, user_info=('gen-apollo', 'Ad@pCr01!'),
                                file_path=r'win_machine_info.json', target_path='/tftpboot/',
                                first_connection=False):
        """
        The feature use the PSCP command for file transfer to the apollo server
        :param machine: Apollo server name
        :param user_info: Connect account and password
        :param file_path: Local file path
        :param target_path: Remote apollo server file path
        :param first_connection: The server needs to be set to True for the first connection
        :return:
        """
        username = user_info[0]
        password = user_info[1]
        if first_connection:
            cmd1 = r'echo y|pscp {} {}@{}:{}'.format(file_path, username, machine, target_path)
            os.system(cmd1)
        # Transfer the local file to the Apollo server
        cmd2 = r'echo {}|pscp {} {}@{}:{}'.format(password, file_path, username, machine, target_path)
        os.system(cmd2)
        logger.debug('Transfer file to apollo successful')

    @staticmethod
    def write_json_file(msg):
        with open('win_machine_info.json', 'w', encoding='utf-8') as wf:
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
                logger.info('Received table information: {}'.format(received))
                handle.write_json_file(msg=received)
                handle.transfer_file_to_apollo(machine=received['machine'],
                                               file_path='win_machine_info.json',
                                               target_path='/tftpboot/win_machine_info.json',
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
