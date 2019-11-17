"""
Write wifi radio limits
"""
import xlrd
import re


def excel_read(file_name=None, sheet_index=0):
    """
    读取Excel表格
    :param file_name: 要读取的CSV表格名称
    :param sheet_index: 表格的页面索引值，第一页为0，以此类推
    :return:
    """
    # 打开Excel文档
    ex_rd = xlrd.open_workbook(filename=file_name)
    # 读取Excel的表格（sheet_index=0 读取第一张表格）
    sheet = ex_rd.sheet_by_index(sheet_index)

    result = []
    for i in range(sheet.nrows):
        # 循环读取表格每行数据
        row_data = sheet.row_values(i)
        result.append(row_data)
    return result


def parse(contents=None):
    for index, content in enumerate(contents):
        column1, column2 = content
        result = re.search(r',"(\d+)","(\d+\.?\d+)","(\d+)","(\d+)","(\d+)","(\d+)","(\d+)","(\d+)"', column1)
        if result:
            final1 = list(result.groups())
        else:
            final1 = []
        final2 = column2[:-1].split(',')

        print(index, final1, final2)
        if final1 != final2:
            print('index: {}, is fail'.format(index))


if __name__ == '__main__':
    result = excel_read(file_name=r'C:\Users\evaliu\Desktop\Xor_compare.xlsx', sheet_index=0)
    print(result)
    print(len(result))
    parse(result)
