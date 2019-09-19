import os
import re
import tkinter as tk
import threading
from xmlrpc.server import SimpleXMLRPCServer
from tkinter import messagebox


class Function(object):
    """
    This class holds server-side execution functions
    """
    @staticmethod
    def get_windows_host():
        """
        Gets the host name of the local computer
        :return: get hostname to client side
        """
        result = os.popen('ipconfig -all')
        read_info = result.readlines()[3]
        host = re.search(': (\w+)', read_info)
        if host:
            host = host.groups()[0]
        else:
            host = 'not find windows host'
        return host


class Gui(object):
    """
    This class is used to start the service on the server side
    """
    def __init__(self, port=6666):
        self.port = port
        self.root = tk.Tk()
        self.root.title('Server interface')
        self.set_window_center(width=280, height=90)

        tk.Label(self.root, text='Server ip: ').grid(row=0, column=1, sticky=tk.W)
        self.input1 = tk.StringVar()
        self.input1.set(self.get_windows_ip())
        self.entry1 = tk.Entry(self.root, textvariable=self.input1).grid(row=0, column=2, padx=45)

        tk.Label(self.root, text='Server port: ').grid(row=1, column=1, sticky=tk.W)
        self.input2 = tk.StringVar()
        self.input2.set(self.port)
        self.entry2 = tk.Entry(self.root, textvariable=self.input2).grid(row=1, column=2, padx=45)

        tk.Button(self.root, text='Quit', command=self.root.quit, bg='red', fg='white')\
            .grid(row=2, column=1, pady=5)
        tk.Button(self.root, text='Start', command=self.handle_windows, bg='blue', fg='white')\
            .grid(row=2, column=2, pady=5)

    @staticmethod
    def get_windows_ip():
        """
        Gets the IP address of the local computer
        :return:
        """
        result = os.popen('ipconfig')
        windows_ip = re.search('\d+\.\d+\.\d+\.\d+', result.read())
        if windows_ip:
            windows_ip = windows_ip.group()
        else:
            windows_ip = 'Please enter your ip'
        return windows_ip

    def handle_windows(self):
        """
        Start thread to setup_server function
        :return:
        """
        threading.Thread(target=self.setup_server()).start()

    def setup_server(self):
        """
        Set the server never to stop
        :return:
        """
        try:
            server = SimpleXMLRPCServer((self.input1.get(), int(self.input2.get())))
            messagebox.showinfo('Information', 'Server {} Listening on port {}...'.
                                format(self.input1.get(), int(self.input2.get())))
            server.register_instance(Function())
            server.serve_forever()
        except Exception as ex:
            messagebox.showerror('Error', 'Start server error...\nerror msg: {}'.format(ex))
            self.root.quit()

    def set_window_center(self, width=300, height=300):
        """
        Center the GUI interface
        :param width: expect width (type： int)
        :param height: expect height (type： int)
        :return:
        """
        # Gets the width and height of the computer screen
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        # Calculate the X and Y positions
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == '__main__':
    gui = Gui(port=6666)
    gui.root.mainloop()
