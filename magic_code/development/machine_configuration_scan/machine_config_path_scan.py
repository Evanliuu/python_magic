# This python version is 2.7
import json
import time
import os
import re
from pexpect import pxssh
import threading
import datetime
import Tkinter as tk
import tkMessageBox
import csv
from apollo.libs import lib


class Gui(object):

    def __init__(self, station_path=None):
        self.root_path = os.getcwd()
        self.station_path = station_path
        self.username = self.password = None
        self.root = None
        self.source = tk.Tk()
        self.source.title('Login user')

        tk.Label(self.source, text='Please enter your username: ').grid(row=0, column=0)
        tk.Label(self.source, text='Please enter your password: ').grid(row=1, column=0)

        self.user_input1 = tk.StringVar()
        tk.Entry(self.root, textvariable=self.user_input1).grid(row=0, column=1)
        self.user_input2 = tk.StringVar()
        tk.Entry(self.root, textvariable=self.user_input2, show='*').grid(row=1, column=1)

        tk.Button(self.source, text='Clear', command=self.clear_user_input, bg='DodgerBlue').grid(row=2, column=0)
        tk.Button(self.source, text='Login', command=self.login_user, bg='GreenYellow').grid(row=2, column=1)

        self.set_gui_center(root=self.source)

    def clear_user_input(self):
        for i in [self.user_input1, self.user_input2]:
            i.set('')

    def login_user(self):
        self.username = self.user_input1.get()
        self.password = self.user_input2.get()

        if self.username and self.password:
            # quit source window
            self.source.destroy()
            # create new gui window for machine config path scan
            self.create_new_gui_window()
        else:
            tkMessageBox.showwarning('Warning', 'User name and password cannot be empty!')

    def create_new_gui_window(self):
        self.root = tk.Tk()
        self.root.title('Machine config mapping scanning')

        tk.Label(self.root, text='Please enter your machine list:').grid(row=0, column=0)
        self.text1 = tk.Text(self.root, width=40, height=5)
        self.text1.grid(row=0, column=1)
        tk.Button(self.root, text='Use default machine list', command=self.read_machine_list, bg='Turquoise').grid(
            row=0, column=2)

        tk.Button(self.root, text='Clear', command=self.clear_text_information, bg='DodgerBlue').grid(row=1, column=0)
        tk.Button(self.root, text='Start', command=self.start_scan, bg='GreenYellow').grid(row=1, column=1)
        tk.Button(self.root, text='Quit', command=self.root.quit, bg='red', fg='white').grid(row=1, column=2)

        self.set_gui_center(root=self.root)

    def read_machine_list(self):
        machine_list = []
        listdir = os.listdir(self.station_path)

        for machine in self.start_search(listdir):
            # Save each machine information
            if machine:
                machine_list.append(machine)

        # Displayed in the text1 control
        self.text1.delete(1.0, tk.END)
        self.text1.insert(tk.END, machine_list)

    def start_search(self, listdir=None):
        for machine_file in listdir:
            if 'fx' in machine_file:
                lines = self.open_machine_file(machine_file)

                product_line = re.search("PRODUCT_LINE = '(\w+)'", lines)
                test_area = re.search("TEST_AREA = '(\w+)'", lines)
                stations = re.match('(\w+)\.py', machine_file)

                if product_line and test_area and stations:
                    product = product_line.groups()[0]
                    area = test_area.groups()[0]
                    station = stations.groups()[0]
                    yield [product, area, station]
                else:
                    print('no station information found in the file - {}'.format(machine_file))
                    yield None

    def open_machine_file(self, machine_file):
        with open(os.path.join(self.station_path, str(machine_file)), 'r') as rf:
            lines = rf.read()
            return lines

    def clear_text_information(self):
        self.text1.delete(1.0, tk.END)

    @staticmethod
    def set_gui_center(root=None):
        root.update_idletasks()
        x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        y = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
        root.geometry('+%d+%d' % (x, y))

    def start_scan(self):
        user_info = (self.username, self.password)
        machine_list = self.text1.get(1.0, tk.END)

        try:
            # Check that the machine list is in the correct format
            machine_list = eval(machine_list)
            handle = Machine_handle(user_info=user_info, machine_list=machine_list)
            tkMessageBox.showinfo('info', 'Start scanning all the machines\nPlease press OK to continue!')

            # Run machine config path check
            handle.main()
            tkMessageBox.showinfo('info', 'The scan is complete\npress OK to end...')
            self.clear_text_information()
        except Exception:
            tkMessageBox.showwarning('Warning', 'The machine list is empty or incorrectly formed\nPlease re-enter!')


class Machine_handle(object):

    def __init__(self, user_info=None, machine_list=None):
        """
        This feature is used to scan configuration mappings for all machines
        :param user_info: Fill out a legitimate Apollo account
        :param machine_list: Fill in the list of machines to scan

        Manually build the machine list type: [['Product_line', 'Station_name', 'Apollo_server_name'], [...], [...]]
        example:
            [
                ['Barbados', 'SYSFA', 'fxcavp288'],
                ['Barbados', 'PCBDL', 'fxcavp362'],
                ['Zephyr', 'PCBPB', 'fxcavp457'],
                ['Antigua', 'PCBST', 'fxcavp216'],
            ]
        """
        self.username, self.password = user_info
        self.machine_list = machine_list
        self.result_info = []
        self.connection_error_info = []

    def machine_config_path_check(self, machine_list=None):
        machine = machine_list[2]
        if '_' in machine:
            machine_name = machine.split('_')[0]
        else:
            machine_name = machine

        # TODO Add the config mapping check path
        config_mapping_check_cmd = [
            ['cd /opt/cisco/constellation/apollo/scripts/wnbu', 'trunk -> /opt/cisco/scripts/prod/wnbu/trunk'],
            ['cd /opt/cisco/constellation/apollo/config', '{0}_config.py -> /opt/cisco/constellation/apollo/scripts/wnbu/trunk/trunk/stations/foc/{0}.py'.format(machine)],
        ]

        error_config_mapping_list = []
        connection_error_info = dict()
        collection_info = dict()
        collection_info['Product_line'] = '-'.join(machine_list)

        for i in range(3):
            try:
                # Connect apollo server...
                s = pxssh.pxssh()
                s.login(machine_name, self.username, self.password)

                # Check the machine config mapping
                for line in config_mapping_check_cmd:
                    cmd = line[0]
                    expect_value = line[1]
                    # Run check command
                    s.sendline(cmd)
                    s.prompt()
                    s.sendline('ls -l')
                    s.prompt()

                    # Check to see if there are more configuration mappings
                    config_mappings = re.findall('\w+_config.py -> .+?\.py', s.before)
                    if len(config_mappings) > 1:
                        result = '{}:\n'.format(cmd) + ',\n'.join(config_mappings)
                    else:
                        result = '{}: Null'.format(cmd)

                    if 'Multiple_machine_mapping' in collection_info:
                        collection_info['Multiple_machine_mapping'] = \
                            collection_info['Multiple_machine_mapping'] + ',\n' + result
                    else:
                        collection_info['Multiple_machine_mapping'] = result

                    # Check that the configuration mapping is correct
                    if expect_value not in s.before:
                        error_config_mapping_list.append(expect_value)

                if error_config_mapping_list:
                    collection_info['Mapping_check_result'] = ',\n'.join(
                        ['Not found {}: {}'.format(i + 1, r) for i, r in enumerate(error_config_mapping_list)])
                else:
                    collection_info['Mapping_check_result'] = 'Pass'

                # Check the prod packet version
                check_cmd = 'cat /opt/cisco/scripts/prod/wnbu/trunk/wnbu_trunk.egg-info/PKG-INFO'
                s.sendline(check_cmd)
                s.prompt()
                received = s.before
                line = re.search('Version: (\d+\.\d+\.\d+)', received)
                if line:
                    collection_info['Packet_version'] = line.groups()[0]
                else:
                    collection_info['Packet_version'] = 'Not found'

                # Check the apollo version
                check_cmd = 'apollo version'
                s.sendline(check_cmd)
                s.prompt()
                received = s.before
                line = re.search('Apollo-\d+-\d+', received)
                if line:
                    collection_info['Apollo_version'] = line.group()
                else:
                    collection_info['Apollo_version'] = 'Not found'

                s.logout()
                break
            except Exception as ex:
                if i == 2 or 'Could not establish connection to host' in ex.message:
                    connection_error_info['Product_line'] = '-'.join(machine_list)
                    connection_error_info['Error_message'] = ex.message
                    break
                time.sleep(2)

        if connection_error_info:
            self.connection_error_info.append(connection_error_info)
        else:
            self.result_info.append(collection_info)

    @staticmethod
    def write_csv_file(msg, file_name, csv_header):
        with open('{}.csv'.format(file_name), 'wb') as file:
            write = csv.DictWriter(file, fieldnames=csv_header)
            write.writeheader()

            # Write each row data to csv file
            for each_data in msg:
                write.writerow(each_data)

    def main(self):
        machine_list = self.machine_list

        threads = []
        loops = range(len(machine_list))
        print('Multi-thread process start time: {}'.format(datetime.datetime.now()))

        for list in machine_list:
            t = threading.Thread(target=self.machine_config_path_check, args=(list,))
            threads.append(t)

        for i in loops:
            threads[i].start()

        for i in loops:
            threads[i].join()

        print('Multi-thread process end time: {}'.format(datetime.datetime.now()))

        if self.result_info:
            all_machines = len(machine_list)
            error_machines = len(self.connection_error_info)

            print('Scanning result:')
            print('*' * 50)
            print('All machines: {}\nPass machines: {}\nError machines: {}'.
                  format(all_machines, all_machines - error_machines, error_machines))
            print('*' * 50)

            # Write all the information into the CSV table
            csv_header = ['Product_line', 'Mapping_check_result', 'Multiple_machine_mapping',
                          'Packet_version', 'Apollo_version', ]
            self.write_csv_file(self.result_info, file_name='machine_mapping_scan_result',
                                csv_header=csv_header)

        # Write the connection error information into the CSV table
        if self.connection_error_info:
            csv_header = ['Product_line', 'Error_message']
            if self.connection_error_info:
                self.write_csv_file(self.connection_error_info, file_name='scan_error_result',
                                    csv_header=csv_header)


def send_mail(email, attachments):
    lib.sendmail(to=email, subject='Scan machines mapping summary',
                 body='all the scan machines result is in the attachment, Please review, Thanks!',
                 attachments=attachments)
    print('send email to {} mailbox successful!'.format(email))


if __name__ == '__main__':
    station_path = '/opt/cisco/scripts/prod/wnbu/trunk/trunk/stations/foc'
    gui = Gui(station_path=station_path)
    gui.source.mainloop()

    # TODO Send mail to cisco mailbox
    # send_mail(email='evaliu', attachments='machine_mapping_scan_result.csv')
    # send_mail(email='evaliu', attachments='scan_error_result.csv')
