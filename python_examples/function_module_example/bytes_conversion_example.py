import os
import chardet


def bytes_conversion(size):
    """
    字节符号转换
    :param size: 字节大小（B）
    :return:
    """
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = dict()
    for i, s in enumerate(symbols, 1):  # 获取每个符号的字节数
        prefix[s] = 1 << i*10
    for s in reversed(symbols):  # 判断文件大小所属的符号范围
        if int(size) >= prefix[s]:
            return '{:.2f} {}'.format(float(size) / prefix[s], s)
    return "{} B".format(size)


if __name__ == '__main__':
    print(bytes_conversion(size=os.path.getsize('bytes_conversion_example.py')))

    # 获取文件的编码格式
    result = chardet.detect(open('bytes_conversion_example.py', mode='rb').read())
    print(result)
