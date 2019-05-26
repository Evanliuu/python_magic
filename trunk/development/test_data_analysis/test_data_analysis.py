# coding=UTF-8
import xlwt
import xlrd
import tkinter as Tkinter
import tkinter.messagebox as tkMessageBox
import re


class Excel_crawler(object):

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title('Excel analyse')
        self.root.geometry('480x180')
        # self.root.destroy()

        self.label1 = Tkinter.Label(self.root, text='请输入Excel表格名称 （例：evan.xlsx）').grid(row=0, column=1, sticky=Tkinter.W)
        self.input1 = Tkinter.StringVar()
        self.entry1 = Tkinter.Entry(self.root, textvariable=self.input1).grid(row=1, column=1, sticky=Tkinter.W)

        self.label2 = Tkinter.Label(self.root, text='请输入要分析的页数位置 （例：第一页则输入：1， 可多页输入1， 2， 3）').grid(row=2, column=1, sticky=Tkinter.W)
        self.input2 = Tkinter.StringVar()
        self.entry2 = Tkinter.Entry(self.root, textvariable=self.input2).grid(row=3, column=1, sticky=Tkinter.W)

        self.label3 = Tkinter.Label(self.root, text='请输入要匹配的数据和条件 （例：VALUE，>10）').grid(row=4, column=1, sticky=Tkinter.W)
        self.input3 = Tkinter.StringVar()
        self.entry3 = Tkinter.Entry(self.root, textvariable=self.input3).grid(row=5, column=1, sticky=Tkinter.W)

        self.entry_button = Tkinter.Button(self.root, text='确认', command=self.entry_event).grid(row=6, column=1, sticky=Tkinter.W)
        self.quit_button = Tkinter.Button(self.root, text='清空', command=self.erase_uese_info).grid(row=6, column=1)
        self.quit_button = Tkinter.Button(self.root, text='退出', command=self.root.quit, bg='red', fg='white').grid(row=6, column=2)

    def erase_uese_info(self):
        for i in [self.input1, self.input2, self.input3]:
            i.set('')

    def get_excel_name(self):
        excel_name = self.input1.get()
        if excel_name.endswith('.xls') or excel_name.endswith('.xlsx'):
            pass
        else:
            self.input1.set('')
            tkMessageBox.showwarning('警告', '请输入正确的Excel表格名称，\n要分析的文件必须放在当前目录下！')
            excel_name = None
        return excel_name

    def get_sheet_info(self):
        sheet_index = self.input2.get()
        capture_sheet_index = re.match('[\d,\s*\d]+', sheet_index)
        if capture_sheet_index is not None:
            capture_sheet_index = capture_sheet_index.group().split(',')
            if len(capture_sheet_index) > 1:
                sheet_index = []
                for i in capture_sheet_index:
                    # 检查每个参数，如果有多余的空白则把它删除
                    i = ''.join(i.split())
                    sheet_index.append(i)
            else:
                sheet_index = capture_sheet_index
        else:
            sheet_index = None

        if not sheet_index:
            self.input2.set('')
            tkMessageBox.showwarning('警告', '请输入正确的页数！')
        return sheet_index

    def get_analyse_data(self):
        analyse_data = self.input3.get()
        if analyse_data:
            capture_analyse_data = analyse_data.split(',')
            if len(capture_analyse_data) == 2:
                analyse_data = []
                for i in capture_analyse_data:
                    # 检查每个参数，如果有多余的空白则把它删除
                    i = ''.join(i.split())
                    analyse_data.append(i)
            else:
                analyse_data = None
        else:
            analyse_data = None

        if not analyse_data:
            self.input3.set('')
            tkMessageBox.showwarning('警告', '请输入正确的格式！')
            analyse_data = None
        return analyse_data

    def entry_event(self):
        # 获取Excel表格名称(str)，表格页数(list)，匹配方式(list)
        excel_name = self.get_excel_name()
        sheet_index = self.get_sheet_info()
        analyse_data = self.get_analyse_data()

        if excel_name and sheet_index and analyse_data:
            tkMessageBox.showinfo('提示', '输入成功，点击确定继续...')
            self.analyses_excel(file_name=excel_name, sheet_index=sheet_index, format_info=analyse_data)

    def analyses_excel(self, file_name='', sheet_index=None, format_info=None):
        # 打开Excel表格
        wb = xlrd.open_workbook(filename=file_name)

        format_value, limit = format_info
        final_list = []

        # run analyses
        for sheet_value in sheet_index:
            sheet = wb.sheet_by_index(int(sheet_value)-1)
            total_rows = sheet.nrows

            for i in range(total_rows):
                row_data = sheet.row_values(i)
                row_data = str(row_data)
                if format_value in row_data:
                    line = re.search(format_value + '.\d+', row_data)
                    if line is not None:
                        capture_value = line.group().split(format_value)[-1]
                        if eval('{}{}'.format(capture_value, limit)):
                            final_list.append(row_data)

        if final_list:
            self.create_excel(final_list)

    @staticmethod
    def create_excel(write_info=None):
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('Summary', cell_overwrite_ok=True)

        # 计算所有数据的大小
        rows_range = range(len(write_info))
        for i in rows_range:
            # 获得每行的数据
            line_value = eval(write_info[i])
            # 计算每行的大小
            each_line = range(len(line_value))
            for line in each_line:
                sheet1.write(i, line, line_value[line])

        f.save('analyses_result.xls')
        tkMessageBox.showinfo('提示', '分析完毕，请按确定结束！')


if __name__ == '__main__':
    crawler = Excel_crawler()
    root = crawler.root
    # 让GUI始终处于居中位置
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    root.geometry('+%d+%d' % (x, y))
    root.mainloop()
