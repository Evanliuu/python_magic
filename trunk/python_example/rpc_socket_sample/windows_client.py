import tkinter as tk
from tkinter import messagebox
from xmlrpc.client import ServerProxy


class WindowsConnect(object):
    """
    This class is used on the remote server side
    """
    def __init__(self, addr=None, port=None):
        self.addr = addr
        self.port = port or 6666
        self.proxy = ServerProxy('http://%s:%s/' % (self.addr, self.port), allow_none=True)

    def get_windows_host(self):
        """
        Executes functions on the remote server side and returns data
        :return:
        """
        host = self.proxy.get_windows_host()
        return host


class Gui(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Client interface')
        self.set_window_center(width=720, height=410)

        tk.Label(self.root, text='Connect ip: ').grid(row=0, column=1, sticky=tk.W)
        self.input1 = tk.StringVar()
        self.entry1 = tk.Entry(self.root, textvariable=self.input1).grid(row=0, column=2, padx=45)

        tk.Label(self.root, text='Connect port: ').grid(row=1, column=1, sticky=tk.W)
        self.input2 = tk.StringVar()
        self.entry2 = tk.Entry(self.root, textvariable=self.input2).grid(row=1, column=2, padx=45)

        tk.Label(self.root, text='Received: ').grid(row=3, column=1, sticky=tk.W)
        self.text = tk.Text(self.root)
        self.text.grid(row=3, column=2)

        tk.Button(self.root, text='Clear', command=self.clear_text).grid(row=4, column=1, pady=5)
        tk.Button(self.root, text='Start', command=self.open_connection, bg='blue', fg='white') \
            .grid(row=4, column=2, pady=5)
        tk.Button(self.root, text='Quit', command=self.root.quit, bg='red', fg='white') \
            .grid(row=4, column=3, pady=5)

    def clear_text(self):
        self.text.delete(1.0, tk.END)

    def open_connection(self):
        if not self.input1.get() or not self.input2.get():
            messagebox.showwarning('Warning', 'IP and host cannot be empty!')
        else:
            try:
                windows = WindowsConnect(addr=self.input1.get(), port=self.input2.get())
                self.text.insert(tk.END, 'Connect ip {} port {}\n'.
                                 format(self.input1.get(), self.input2.get()))
                self.text.insert(tk.END, 'Wait for the remote server to respond...\n')
                host = windows.get_windows_host()
            except Exception as ex:
                host = None
                self.text.insert(tk.END, 'No server response was received\nerror msg: {}'.format(ex))

            if host:
                self.text.insert(tk.END, 'read ok!\n')
                self.text.insert(tk.END, '*' * 30 + '\n')
                self.text.insert(tk.END, 'read the server host name: {}\n'.format(host))
                self.text.insert(tk.END, '*' * 30 + '\n')

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
    gui = Gui()
    gui.root.mainloop()
