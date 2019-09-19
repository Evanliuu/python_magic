import tkinter as tk

""" Tkinter16个核心窗口部件：
Button：一个简单的按钮，用来执行一个命令或别的操作。
Canvas：组织图形。这个部件可以用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
Checkbutton：代表一个变量，它有两个不同的值。点击这个按钮将会在这两个值间切换。
Entry：文本输入域。
Frame：一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。
Label：显示一个文本或图象。
Listbox：显示供选方案的一个列表。listbox能够被配置来得到radiobutton或checklist的行为。
Menu：菜单条。用来实现下拉和弹出式菜单。
Menubutton：菜单按钮。用来实现下拉式菜单。
Message：显示一文本。类似label窗口部件，但是能够自动地调整文本到给定的宽度或比率。
Radiobutton：代表一个变量，它可以有多个值中的一个。点击它将为这个变量设置值，并且清除与这同一变量相关的其它radiobutton。
Scale：允许你通过滑块来设置一数字值。
Scrollbar：为配合使用canvas, entry, listbox, and text窗口部件的标准滚动条。
Text：格式化文本显示。允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。
Toplevel：一个容器窗口部件，作为一个单独的、最上面的窗口显示。
messageBox：消息框，用于显示你应用程序的消息框。(Python2中为tkMessagebox)
"""


class Gui(object):
    """ grid参数使用方法:
    column = 列数 [number - use cell identified with given column (starting with 0)]
    columnspan = 跨列数 [number - this widget will span several columns]
    in = master - use master to contain this widget
    in_ = master - see 'in' option description
    ipadx = 单元格左右间距 [amount - add internal padding in x direction]
    ipady = 单元格上下间距 [amount - add internal padding in y direction]
    padx = 单元格内部元素与单元格的左右间距 [amount - add padding in x direction]
    pady = 单元格内部元素与单元格的上下间距 [amount - add padding in y direction]
    row = 行数 [number - use cell identified with given row (starting with 0)]
    rowspan = 跨行数 [number - this widget will span several rows]
    sticky = 空间位置 [NSWE - if cell is larger on which sides will this]
    """

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Gui sample')
        # 设置界面居中
        self.set_window_center(width=720, height=410)
        # 显示一个文本或图象
        self.label = tk.Label(self.root, text="Label is here")
        # 单行文本输入域
        self.input = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.input)
        self.input.set('Entry is here')
        # 多行文本输入域，允许你用不同的样式和属性来显示和编辑文本。同时支持内嵌图象和窗口。
        self.text = tk.Text(self.root)
        self.text.insert(tk.END, 'Test is here')
        # 执行所有窗口部件
        self.label.grid(row=0, column=0, sticky=tk.W)
        self.entry.grid(row=1, column=0, sticky=tk.W)
        self.text.grid(row=3, column=0)

    def set_window_center(self, width=300, height=300):
        """
        设置GUI界面居中显示
        :param width: expect width (type： int)
        :param height: expect height (type： int)
        :return:
        """
        # 获取电脑屏幕高度和宽度
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        # 计算X & Y轴位置
        x = (ws / 2) - (width / 2)
        y = (hs / 2) - (height / 2)
        # 设置GUI大小和位置
        self.root.geometry('%dx%d+%d+%d' % (width, height, x, y))


if __name__ == '__main__':
    gui = Gui()
    gui.root.mainloop()
