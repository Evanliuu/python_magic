import time
import datetime
import threading
import tkinter as tk

from tkinter import messagebox

__author__ = 'Evan'


class CountdownTool(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('倒计时小工具')
        self.root.wm_attributes("-topmost", True)
        self.build_select_button_frame()
        self.build_display_times()
        self.set_window_center(window=self.root, width=275, height=135)

    def build_display_times(self):
        frames = tk.Frame(relief='ridge', borderwidth=0)
        self.label = tk.Label(frames, text='00:00', font=('times', 40, 'bold'))
        self.label.grid(row=0, column=0, sticky=tk.W, padx=70)
        frames.grid(row=1, column=0, sticky=tk.NSEW)

    def build_select_button_frame(self):
        frames = tk.Frame(relief='ridge', borderwidth=5)
        tk.Label(frames, text='请选择倒计时间: ').grid(row=0, column=0, sticky=tk.W)

        self.var = tk.IntVar()
        tk.Scale(frames, label='Minutes', from_=1, to=60, resolution=1,
                 orient=tk.HORIZONTAL, variable=self.var, showvalue=1).\
            grid(row=0, column=1, sticky=tk.W)
        self.var.set(30)

        self.start_button = tk.Button(frames, text='开始', command=self.progress, bg='LightBlue')
        self.start_button.grid(row=0, column=2, sticky=tk.W, padx=5)
        frames.grid(row=0, column=0, sticky=tk.NSEW)

    def quit(self):
        self.root.destroy()
        self.root.quit()

    @staticmethod
    def set_window_center(window, width=300, height=300):
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def progress(self):
        threading.Thread(target=self._progress, args=()).start()

    def _progress(self):
        self.start_button.config(text='运行中', state='disable')
        try:
            close_time = (datetime.datetime.now() + datetime.timedelta(minutes=self.var.get())).strftime('%H:%M:%S')
            close_time = datetime.datetime.strptime(close_time, '%H:%M:%S')
            while True:
                time.sleep(1)
                current_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
                gap_time = close_time - current_time
                minutes = str(gap_time).split(':')[-2]
                seconds = str(gap_time).split(':')[-1]
                if str(minutes) == '00' and str(seconds) == '00':
                    self.label.config(text='{}:{}'.format(minutes, seconds))
                    break
                self.label.config(text='{}:{}'.format(minutes, seconds))
            messagebox.showinfo('Info', '倒计时间已到，请注意休息！')
        finally:
            self.start_button.config(text='开始', state='active')


if __name__ == '__main__':
    countdown = CountdownTool()
    countdown.root.mainloop()
