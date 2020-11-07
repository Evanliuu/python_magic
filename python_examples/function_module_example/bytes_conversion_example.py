import os


def bytes_conversion(size):
    """
    字节转换
    :param size: 字节大小（B）
    :return:
    """
    symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
    prefix = dict()
    for i, s in enumerate(symbols, 1):
        prefix[s] = 1 << i*10
    for s in reversed(symbols):
        if int(size) >= prefix[s]:
            value = float(size) / prefix[s]
            return '%.2f%s' % (value, s)
    return "%sB" % size


print(bytes_conversion(size=os.path.getsize(r'C:\Users\evaliu\Desktop\GifCam.exe')))
