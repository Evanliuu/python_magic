import xlrd
import xlwt
import os


def excel_write(information=None):
    # 创建一个新的Excel文档
    ex_wt = xlwt.Workbook()
    # 添加一个新的工作表
    sheet1 = ex_wt.add_sheet('first_page', cell_overwrite_ok=True)

    # 计算数据的总行数
    rows_range = range(len(information))
    for row in rows_range:
        each_data = information[row]

        if isinstance(each_data, (list, tuple)):
            # 循环写入每条数据
            for column in range(len(each_data)):
                sheet1.write(row, column, each_data[column])
        else:
            # 写入一条数据
            sheet1.write(row, 0, each_data)

    ex_wt.save('excel_example.xls')


def excel_read(file_name='', sheet_index=0):
    def read_local_excel():
        files = os.listdir(os.getcwd())
        for file in files:
            if '.xls' in file:
                local_excel = file
                return local_excel
        else:
            print('No excel documents were found locally！')
            return None
    file_name = file_name or read_local_excel()

    # 打开Excel文档
    ex_rd = xlrd.open_workbook(filename=file_name)
    # 读取Excel的表格（index：1）读取第一张表格
    sheet = ex_rd.sheet_by_index(sheet_index)

    # 读取表格的总行数
    total_rows = range(sheet.nrows)
    for i in total_rows:
        # 循环读取表格内每一行的数据
        row_data = sheet.row_values(i)
        print(row_data)


if __name__ == '__main__':
    message = [
        ['name', 'id'],
        ['evan', '66'],
        'writer finish'
    ]
    excel_write(information=message)
    excel_read()
