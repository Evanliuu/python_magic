# -*- coding:utf-8 -*-
import xlwt


def write_excel_table(write_info, table_name='excel.xls', sheet_name='Sheet1'):
    """
    写入Excel表格
    :param write_info: 写入Excel表格内的数据
    :param table_name: Excel文档名称
    :param sheet_name: Excel文档内的页面名称
    :return:
    """
    # 创建一个Excel文档对象
    ex_wt = xlwt.Workbook()
    # 添加一个新的工作表
    sheet1 = ex_wt.add_sheet(sheet_name, cell_overwrite_ok=True)

    # 写入表格第一行标题
    title = write_info[0][0][1]  # 获取标题信息
    style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow; font: bold on')  # 填充灰色背景，字体加粗
    sheet1.write_merge(0, 0, 0, 19, title, style)  # 合并第一行的第0列到第19列

    # 从第二行开始写剩下的数据
    for row_index, each_row in enumerate(write_info[1:]):
        # 循环写入每列数据
        for column_index, each_column in enumerate(each_row):
            background_color = each_column[0]  # 获取背景颜色
            value = each_column[1]  # 获取列值

            if background_color == 'FFFFC000':  # 填充灰色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour gray25')
            elif background_color == 'FFFF0000':  # 填充红色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour red')
            elif background_color == 'FF00B0F0':  # 填充蓝色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour blue')
            elif background_color == 'FF00B050':  # 填充绿色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour green')
            elif background_color == 'FF7030A0':  # 填充紫色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour violet')
            elif background_color == 'FF0070C0':  # 填充珊瑚红背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour coral')
            elif background_color == 'FFFFFF00':  # 填充黄色背景
                style = xlwt.easyxf('pattern: pattern solid, fore_colour yellow')
            else:
                style = None  # 样式默认为None

            if style:
                sheet1.write(row_index + 1, column_index, value, style)
            else:  # 如果style为None，写入默认颜色
                sheet1.write(row_index + 1, column_index, value)
    # 保存所有数据到表格
    ex_wt.save(table_name)


def read_raw_data(file_name):
    """
    读取原始数据
    :param file_name: 文件名
    :return:
    """
    result = []
    with open(file_name, 'r') as rf:
        for i in rf.read().splitlines():
            result.append(eval(i))
    return result


def main():
    result = read_raw_data(file_name='原始数据.txt')
    write_excel_table(write_info=result, table_name='example.xls', sheet_name='example')


if __name__ == '__main__':
    main()
