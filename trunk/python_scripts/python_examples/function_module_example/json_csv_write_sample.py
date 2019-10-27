import json
import csv
import pandas


def read_write_json_data(msg, file_name='json_file', do_read=False):
    """
    读取或写入JSON对象
    :param msg: 要转换为JSON对象的字符串
    :param file_name: 文件名称
    :param do_read: 默认为False，如果设置为True则是读取JSON对象并返回文本字符串
    :return:
    """
    if do_read:
        with open('{}.json'.format(file_name), 'r', encoding='utf-8') as rf:
            read_file = rf.read()
            # 把JSON对象转换为文本字符串
            str_text = json.loads(read_file)
            return str_text
    else:
        with open('{}.json'.format(file_name), 'w', encoding='utf-8') as wf:
            # 把文本字符串转换为JSON对象，如果有中文ensure_ascii要设置为False，indent代表缩进字符个数
            wf.write(json.dumps(msg, ensure_ascii=False, indent=2) + '\n')


def write_csv_data(msg, file_name='csv_file', headers=None, do_read=False):
    """

    :param msg: 要写入CSV表格的数据
    :param file_name: 文件名称
    :param headers: CSV表格的第一行表头
    :param do_read: 默认为False，如果设置为True则是读取CSV表格并返回所有行的数据
    :return:
    """
    if do_read:
        # 用CSV读取
        with open('{}.csv'.format(file_name), 'r', encoding='utf-8') as rf:
            # 读取CSV表格并返回所有行数据
            reader = csv.reader(rf)
            result = []
            for i in reader:
                result.append(i)
            return result

        # 用pandas读取，返回一个CSV表格，并且有行数显示
        # result = pandas.read_csv('{}.csv'.format(file_name))
    else:
        # 取消多余的空白行： Python3.7是newline=''，Python2.7是用'wb'写入
        with open('{}.csv'.format(file_name), 'w', encoding='utf-8', newline='') as wf:
            # TODO 这个是普通格式的写入
            """
            write = csv.writer(wf)
            msg = [['name', 'evan'], ['id', '66']]
            for i in msg:
                # 循环写入每行数据
                write.writerow(i)
            # 同时写入多行数据
            write.writerows(msg)
            """
            # TODO 这个是字典格式的写入
            dict_write = csv.DictWriter(wf, fieldnames=headers)
            dict_write.writeheader()  # 写入第一行的表头数据
            for i in msg:
                # 循环写入每行数据
                dict_write.writerow(i)
            # 同时写入多行数据
            dict_write.writerows(msg)


if __name__ == '__main__':
    # write json file
    read_write_json_data(msg={'name': 'evan'})
    # write csv file
    write_csv_data(msg=[{'name': 'evan', 'id': '66'}, {'name': 'jane', 'id': '99'}], headers=['name', 'id'])
