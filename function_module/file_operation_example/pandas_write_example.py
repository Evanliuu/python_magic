# -*- coding:utf-8 -*-
import pandas as pd

__author__ = 'Evan'


def write_excel(file_name, sheets, data):
    """
    使用pandas，写入多页工作表到Excel
    :param file_name: 需要生成的Excel表格名
    :param sheets: 需要写入的工作表名
    :param data: 需要写入的数据
    :return:
    """
    writer = pd.ExcelWriter(file_name)
    for sheet in sheets:
        df = pd.DataFrame(data)
        df.to_excel(writer, sheet_name=sheet, index=False)
    writer.save()
    writer.close()


if __name__ == '__main__':
    write_excel(file_name='example.xlsx', sheets=['sheet1', 'sheet2'], data=[1, 2, 3])
