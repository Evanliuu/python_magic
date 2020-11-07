import os


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


print(bytes_conversion(size=os.path.getsize(r'C:\Users\evaliu\Desktop\GifCam.exe')))
