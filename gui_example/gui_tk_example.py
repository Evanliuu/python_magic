"""<<Tkinter 16个核心窗口部件>>
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

<<Tkinter grid参数使用方法>>
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

<<Tkinter 所有颜色对照表>>
* #FFB6C1 LightPink 浅粉红
* #FFC0CB Pink 粉红
* #DC143C Crimson 深红/猩红
* #FFF0F5 LavenderBlush 淡紫红
* #DB7093 PaleVioletRed 弱紫罗兰红
* #FF69B4 HotPink 热情的粉红
* #FF1493 DeepPink 深粉红
* #C71585 MediumVioletRed 中紫罗兰红
* #DA70D6 Orchid 暗紫色/兰花紫
* #D8BFD8 Thistle 蓟色
* #DDA0DD Plum 洋李色/李子紫
* #EE82EE Violet 紫罗兰
* #FF00FF Magenta 洋红/玫瑰红
* #FF00FF Fuchsia 紫红/灯笼海棠
* #8B008B DarkMagenta 深洋红
* #800080 Purple 紫色
* #BA55D3 MediumOrchid 中兰花紫
* #9400D3 DarkViolet 暗紫罗兰
* #9932CC DarkOrchid 暗兰花紫
* #4B0082 Indigo 靛青/紫兰色
* #8A2BE2 BlueViolet 蓝紫罗兰
* #9370DB MediumPurple 中紫色
* #7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
* #6A5ACD SlateBlue 石蓝色/板岩蓝
* #483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
* #E6E6FA Lavender 淡紫色/熏衣草淡紫
* #F8F8FF GhostWhite 幽灵白
* #0000FF Blue 纯蓝
* #0000CD MediumBlue 中蓝色
* #191970 MidnightBlue 午夜蓝
* #00008B DarkBlue 暗蓝色
* #000080 Navy 海军蓝
* #4169E1 RoyalBlue 皇家蓝/宝蓝
* #6495ED CornflowerBlue 矢车菊蓝
* #B0C4DE LightSteelBlue 亮钢蓝
* #778899 LightSlateGray 亮蓝灰/亮石板灰
* #708090 SlateGray 灰石色/石板灰
* #1E90FF DodgerBlue 闪兰色/道奇蓝
* #F0F8FF AliceBlue 爱丽丝蓝
* #4682B4 SteelBlue 钢蓝/铁青
* #87CEFA LightSkyBlue 亮天蓝色
* #87CEEB SkyBlue 天蓝色
* #00BFFF DeepSkyBlue 深天蓝
* #ADD8E6 LightBlue 亮蓝
* #B0E0E6 PowderBlue 粉蓝色/火药青
* #5F9EA0 CadetBlue 军兰色/军服蓝
* #F0FFFF Azure 蔚蓝色
* #E0FFFF LightCyan 淡青色
* #AFEEEE PaleTurquoise 弱绿宝石
* #00FFFF Cyan 青色
* #00FFFF Aqua 浅绿色/水色
* #00CED1 DarkTurquoise 暗绿宝石
* #2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
* #008B8B DarkCyan 暗青色
* #008080 Teal 水鸭色
* #48D1CC MediumTurquoise 中绿宝石
* #20B2AA LightSeaGreen 浅海洋绿
* #40E0D0 Turquoise 绿宝石
* #7FFFD4 Aquamarine 宝石碧绿
* #66CDAA MediumAquamarine 中宝石碧绿
* #00FA9A MediumSpringGreen 中春绿色
* #F5FFFA MintCream 薄荷奶油
* #00FF7F SpringGreen 春绿色
* #3CB371 MediumSeaGreen 中海洋绿
* #2E8B57 SeaGreen 海洋绿
* #F0FFF0 Honeydew 蜜色/蜜瓜色
* #90EE90 LightGreen 淡绿色
* #98FB98 PaleGreen 弱绿色
* #8FBC8F DarkSeaGreen 暗海洋绿
* #32CD32 LimeGreen 闪光深绿
* #00FF00 Lime 闪光绿
* #228B22 ForestGreen 森林绿
* #008000 Green 纯绿
* #006400 DarkGreen 暗绿色
* #7FFF00 Chartreuse 黄绿色/查特酒绿
* #7CFC00 LawnGreen 草绿色/草坪绿
* #ADFF2F GreenYellow 绿黄色
* #556B2F DarkOliveGreen 暗橄榄绿
* #9ACD32 YellowGreen 黄绿色
* #6B8E23 OliveDrab 橄榄褐色
* #F5F5DC Beige 米色/灰棕色
* #FAFAD2 LightGoldenrodYellow 亮菊黄
* #FFFFF0 Ivory 象牙色
* #FFFFE0 LightYellow 浅黄色
* #FFFF00 Yellow 纯黄
* #808000 Olive 橄榄
* #BDB76B DarkKhaki 暗黄褐色/深卡叽布
* #FFFACD LemonChiffon 柠檬绸
* #EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
* #F0E68C Khaki 黄褐色/卡叽布
* #FFD700 Gold 金色
* #FFF8DC Cornsilk 玉米丝色
* #DAA520 Goldenrod 金菊黄
* #B8860B DarkGoldenrod 暗金菊黄
* #FFFAF0 FloralWhite 花的白色
* #FDF5E6 OldLace 老花色/旧蕾丝
* #F5DEB3 Wheat 浅黄色/小麦色
* #FFE4B5 Moccasin 鹿皮色/鹿皮靴
* #FFA500 Orange 橙色
* #FFEFD5 PapayaWhip 番木色/番木瓜
* #FFEBCD BlanchedAlmond 白杏色
* #FFDEAD NavajoWhite 纳瓦白/土著白
* #FAEBD7 AntiqueWhite 古董白
* #D2B48C Tan 茶色
* #DEB887 BurlyWood 硬木色
* #FFE4C4 Bisque 陶坯黄
* #FF8C00 DarkOrange 深橙色
* #FAF0E6 Linen 亚麻布
* #CD853F Peru 秘鲁色
* #FFDAB9 PeachPuff 桃肉色
* #F4A460 SandyBrown 沙棕色
* #D2691E Chocolate 巧克力色
* #8B4513 SaddleBrown 重褐色/马鞍棕色
* #FFF5EE Seashell 海贝壳
* #A0522D Sienna 黄土赭色
* #FFA07A LightSalmon 浅鲑鱼肉色
* #FF7F50 Coral 珊瑚
* #FF4500 OrangeRed 橙红色
* #E9967A DarkSalmon 深鲜肉/鲑鱼色
* #FF6347 Tomato 番茄红
* #FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
* #FA8072 Salmon 鲜肉/鲑鱼色
* #FFFAFA Snow 雪白色
* #F08080 LightCoral 淡珊瑚色
* #BC8F8F RosyBrown 玫瑰棕色
* #CD5C5C IndianRed 印度红
* #FF0000 Red 纯红
* #A52A2A Brown 棕色
* #B22222 FireBrick 火砖色/耐火砖
* #8B0000 DarkRed 深红色
* #800000 Maroon 栗色
* #FFFFFF White 纯白
* #F5F5F5 WhiteSmoke 白烟
* #DCDCDC Gainsboro 淡灰色
* #D3D3D3 LightGrey 浅灰色
* #C0C0C0 Silver 银灰色
* #A9A9A9 DarkGray 深灰色
* #808080 Gray 灰色
* #696969 DimGray 暗淡灰
* #000000 Black 纯黑
"""
# -*- coding:utf-8 -*-
import tkinter as tk

__author__ = 'Evan'


class GuiSample(object):

    def __init__(self):
        self.root = tk.Tk()

        # 设置GUI界面属性
        self.root.title('Gui sample')  # 设置GUI标题
        self.root.wm_attributes("-alpha", 1.0)  # 设置GUI透明度(0.0~1.0)
        self.root.wm_attributes("-topmost", True)  # 设置GUI置顶
        # self.root.wm_attributes("-toolwindow", True)  # 设置为工具窗口（没有放大和缩小按钮）
        # self.root.overrideredirect(-1)  # 去除GUI边框（GUI标题、放大缩小和关闭按钮都会消失）
        # self.bind_window_move_events()  # 如果去除GUI边框了，就要绑定窗口移动事件，否则GUI无法移动

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
        self.add_new_window.grid(row=2, column=1, sticky=tk.W)
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
        self.menu = tk.StringVar()
        self.menu.set('OptionMenu is here')
        select_list = ['Evan', 'Jane']
        self.option_menu = tk.OptionMenu(self.root, self.menu, *select_list)
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
        self.quit_button = tk.Button(self.root, text='Quit', command=self.tk_quit, bg='tomato')
        self.add_new_window = tk.Button(self.root, text='Add_New_Window', command=self.new_window, bg='PeachPuff')

        def display(info):
            self.text_input.delete(1.0, tk.END)  # 清空text控件内容
            self.text_input.insert(tk.END, info)  # 写入内容到text控件
            self.display_button.config(text='Displayed', state='disable')  # 当点击后，更新text文本，并让button失效
            # self.display_button.config(text='Display', state='active')  # 重新激活button变为可点击状态

        # 使用lambda函数进行传参
        self.display_button = tk.Button(self.root, text='Display',
                                        command=lambda: display(self.entry_input.get()), bg='gold')

    def tk_quit(self):
        self.root.destroy()  # 销毁当前窗口
        self.root.quit()  # 退出GUI

    def new_window(self):
        """
        在主窗口上添加一个新的窗口
        :return:
        """
        self.window = tk.Toplevel(self.root)  # 设置self.root为主窗口
        self.window.title('Login Window')
        self.window.wm_attributes("-topmost", True)  # 设置新窗口置顶
        tk.Label(self.window, text='Username').grid(row=0, column=0)

        self.username = tk.StringVar()
        tk.Entry(self.window, textvariable=self.username).grid(row=1, column=0)
        tk.Label(self.window, text='Password').grid(row=0, column=1)

        self.password = tk.StringVar()
        tk.Entry(self.window, textvariable=self.password, show='*').grid(row=1, column=1)
        tk.Label(self.window, text='Pass Code').grid(row=2, column=0)

        self.pass_code = tk.StringVar()
        tk.Entry(self.window, textvariable=self.pass_code).grid(row=3, column=0, sticky=tk.NSEW)

        self.return_confirm = tk.Button(self.window, text='Return', command=self.window.destroy, bg='MediumSpringGreen')
        self.return_confirm.grid(row=3, column=1)
        self.set_gui_geometry(window=self.window, x=1.6, y=3.5)

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
    def set_gui_geometry(window, x=2.5, y=4.0):
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
