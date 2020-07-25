"""<<Tkinter16个核心窗口部件>>
Button:             一个简单的按钮，用来执行一个命令或别的操作。
Canvas:             组织图形。这个部件可以用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
Checkbutton:        代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换。
Entry:              文本输入域。
Frame:              一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。
Label:              显示一个文本或图象。
Listbox:            显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。
Menu:               菜单条。用来实现下拉和弹出式菜单。
Menubutton:         菜单按钮。用来实现下拉式菜单。
Message:            显示一文本。类似label窗口部件，但是能够自动地调整文本到给定的宽度或比率。
Radiobutton:        代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。
Scale:              允许你通过滑块来设置一数字值。
Scrollbar:          为配合使用canvas, entry, listbox, and text窗口部件的标准滚动条。
Text:               格式化文本显示。允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。
Toplevel:           一个容器窗口部件，作为一个单独的、最上面的窗口显示。
messageBox:         消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox)

<<grid参数使用方法>>
column:             列数 [number - use cell identified with given column (starting with 0)]
columnspan:         跨列数 [number - this widget will span several columns]
in:                 master - use master to contain this widget
in_:                master - see 'in' option description
ipadx:              单元格左右间距 [amount - add internal padding in x direction]
ipady:              单元格上下间距 [amount - add internal padding in y direction]
padx:               单元格内部元素与单元格的左右间距 [amount - add padding in x direction]
pady:               单元格内部元素与单元格的上下间距 [amount - add padding in y direction]
row:                行数 [number - use cell identified with given row (starting with 0)]
rowspan:            跨行数 [number - this widget will span several rows]
sticky:             空间位置 [NSWE - if cell is larger on which sides will this]
"""
# -*- coding:utf-8 -*-
import tkinter as tk

__author__ = 'Evan'


class GuiSample(object):

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Gui sample')  # 设置GUI标题

        # 设置GUI界面属性
        self.root.wm_attributes("-alpha", 1.0)  # 设置GUI透明度(0.0~1.0)
        self.root.wm_attributes("-topmost", True)  # 设置GUI置顶
        # self.root.wm_attributes("-toolwindow", True)  # 设置为工具窗口（没有放大和缩小按钮）
        # self.root.overrideredirect(-1)  # 去除GUI边框（GUI标题、放大缩小和关闭按钮都会消失）
        # self.bind_window_move_events()  # 如果去除GUI边框了，就要绑定窗口移动事件，否则GUI无法移动和退出

        # 设置所有窗口部件
        self.build_label()
        self.build_entry()
        self.build_text()
        self.build_check_button()
        self.build_button()
        self.build_option_menu()

        # 执行所有窗口部件
        self.label.grid(row=0, column=0, sticky=tk.W)
        self.entry.grid(row=1, column=0, sticky=tk.W)
        self.checkbutton1.grid(row=0, column=1, sticky=tk.W)
        self.checkbutton2.grid(row=1, column=1, sticky=tk.W)
        self.option_menu.grid(row=2, column=0, sticky=tk.W)
        self.text_input.grid(row=3, column=0, sticky=tk.W, columnspan=2)
        self.display_button.grid(row=4, column=0, sticky=tk.W)
        self.quit_button.grid(row=4, column=1, sticky=tk.W)

        # 设置窗口位置居中
        self.set_gui_geometry(window=self.root)

    def build_option_menu(self):
        """
        构建选择菜单控件
        :return:
        """
        self.from_language = tk.StringVar()
        self.from_language.set('OptionMenu is here')
        select_list = ['Evan', 'Jane']
        self.option_menu = tk.OptionMenu(self.root, self.from_language, *select_list)
        self.option_menu.config(bg='LightSkyBlue')

    def build_label(self):
        """
        构建文本或图像控件
        :return:
        """
        self.label = tk.Label(self.root, text="Label is here")

    def build_button(self):
        """
        构建点击按钮控件
        :return:
        """
        def display(info):
            self.text_input.delete(1.0, tk.END)  # 清空text控件内容
            self.text_input.insert(tk.END, info)  # 写入内容到text控件
        self.quit_button = tk.Button(self.root, text='Quit', command=self.root.quit, bg='tomato')
        # 使用lambda函数进行传参
        self.display_button = tk.Button(self.root, text='Display',
                                        command=lambda: display(self.entry_input.get()), bg='gold')

    def build_check_button(self):
        """
        构建多选按钮控件
        :return:
        """
        self.checkbutton_a = tk.StringVar()
        self.checkbutton1 = tk.Checkbutton(self.root, text="CheckbuttonA", variable=self.checkbutton_a,
                                           offvalue='', onvalue='A')  # 选中后variable值为'A'，不选默认为空字符串
        self.checkbutton1.select()  # 默认选中这个按钮

        self.checkbutton_b = tk.StringVar()
        self.checkbutton2 = tk.Checkbutton(self.root, text="CheckbuttonB", variable=self.checkbutton_b,
                                           offvalue='', onvalue='B')  # 选中后variable值为'B'，不选默认为空字符串

    def build_entry(self):
        """
        构建单行文本输入域
        :return:
        """
        self.entry_input = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_input)
        self.entry_input.set('Entry is here')  # 写入信息到Entry
        # self.entry_input.get()  # 获取Entry控件内所有信息
        # self.entry_input.set('')  # 清空Entry控件内所有信息

    def build_text(self):
        """
        构建多行文本输入域
        :return:
        """
        self.text_input = tk.Text(self.root, height=5, width=40)
        self.text_input.insert(tk.END, 'Text is here')  # 写入信息到Text
        # self.text_input.get(1.0, tk.END).strip()  # 获取Text控件内所有信息
        # self.text_input.delete(1.0, tk.END)  # 清空Text控件内所有信息

    def bind_window_move_events(self):
        """
        绑定窗口移动事件
        :return:
        """
        def start_move(event):
            global x, y
            x = event.x
            y = event.y

        def stop_move(event):
            global x, y
            x = None
            y = None

        def on_motion(event):
            global x, y
            deltax = event.x - x
            deltay = event.y - y
            self.root.geometry("+%s+%s" % (self.root.winfo_x() + deltax, self.root.winfo_y() + deltay))
            self.root.update()

        self.root.bind("<ButtonPress-1>", start_move)  # 监听左键按下操作响应函数
        self.root.bind("<ButtonRelease-1>", stop_move)  # 监听左键松开操作响应函数
        self.root.bind("<B1-Motion>", on_motion)  # 监听鼠标移动操作响应函数

    @staticmethod
    def set_gui_geometry(window, x=2.5, y=4):
        """
        设置window的几何分布，可以控制x轴和y轴的位置
        :param window:
        :param x: x轴位置
        :param y: y轴位置
        :return:
        """
        window.update_idletasks()
        x_info = (window.winfo_screenwidth() - window.winfo_reqwidth()) / x
        y_info = (window.winfo_screenwidth() - window.winfo_reqwidth()) / y
        window.geometry('+%d+%d' % (x_info, y_info))

    @staticmethod
    def set_window_center(window, width=300, height=300):
        """
        设置window居中显示，可以控制窗口的宽度和高度
        :param window:
        :param width: 宽度
        :param height: 高度
        :return:
        """
        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == '__main__':
    guiSample = GuiSample()
    guiSample.root.mainloop()
