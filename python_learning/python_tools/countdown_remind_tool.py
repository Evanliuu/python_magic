# -*- coding:utf-8 -*-
"""
GUI倒计时小工具
"""
import time
import datetime
import threading
import tkinter as tk
from tkinter import messagebox

__author__ = 'Evan'


class CountdownTool(object):

    def __init__(self, minimum_value=1, maximum_value=90, default_value=30):
        self.minimum_value = minimum_value
        self.maximum_value = maximum_value
        self.default_value = default_value
        self.root = tk.Tk()
        self.root.title('倒计时小工具')
        self.root.wm_attributes("-topmost", True)  # GUI置顶，置顶后可手动最小化
        self.build_select_button_frame()
        self.build_display_times()
        self.set_window_center(window=self.root, width=347, height=135)
        self.stop_flag = False

    def build_display_times(self):
        frame = tk.Frame(relief='ridge', borderwidth=0)

        self.display_label = tk.Label(frame, text='待运行')
        self.display_label.grid(row=0, column=0, sticky=tk.W, padx=5)

        self.label = tk.Label(frame, text='00:00:00', font=('times', 40, 'bold'), fg='#FF4500')
        self.label.grid(row=0, column=0, sticky=tk.W, padx=70)
        frame.grid(row=1, column=0, sticky=tk.NSEW)

    def build_select_button_frame(self):
        frames = tk.Frame(relief='ridge', borderwidth=5)
        tk.Label(frames, text='请选择倒计时间: ').grid(row=0, column=0, sticky=tk.W)

        self.var = tk.IntVar()
        tk.Scale(frames, label='Minutes', from_=self.minimum_value, to=self.maximum_value, resolution=1,
                 orient=tk.HORIZONTAL, variable=self.var, showvalue=1).\
            grid(row=0, column=1, sticky=tk.W)
        self.var.set(self.default_value)

        self.start_button = tk.Button(frames, text='开始', command=self.progress, bg='LightSkyBlue')
        self.start_button.grid(row=0, column=2, sticky=tk.W, padx=10)
        tk.Button(frames, text='停止', command=self.stop, bg='tomato').grid(row=0, column=3, sticky=tk.W, padx=10)
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

    def stop(self):
        self.stop_flag = True

    def progress(self):
        threading.Thread(target=self._progress, args=()).start()

    def _progress(self):
        self.stop_flag = False
        self.start_button.config(text='运行中', state='disable')
        try:
            minute_input = self.var.get()
            self.display_label.config(text='共{}分钟'.format(minute_input))
            close_time = (datetime.datetime.now() + datetime.timedelta(minutes=minute_input)).strftime('%H:%M:%S')
            close_time = datetime.datetime.strptime(close_time, '%H:%M:%S')
            while True:
                if self.stop_flag:
                    break
                time.sleep(1)
                current_time = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
                gap_time = close_time - current_time
                hours = int(str(gap_time).split(':')[-3])
                minutes = int(str(gap_time).split(':')[-2])
                seconds = int(str(gap_time).split(':')[-1])
                if not hours and not minutes and not seconds:
                    self.label.config(text='{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
                    break
                self.label.config(text='{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
            if not self.stop_flag:
                messagebox.showinfo('Info', '倒计时间已到，请注意休息！')
        finally:
            self.stop_flag = False
            self.label.config(text='00:00:00')
            self.display_label.config(text='待运行')
            self.start_button.config(text='开始', state='active')


if __name__ == '__main__':
    minimum_time = 1  # 滑块最小时间
    maximum_time = 90  # 滑块最大时间
    default_time = 30  # 滑块预设时间
    countdown = CountdownTool(minimum_time, maximum_time, default_time)
    countdown.root.mainloop()
