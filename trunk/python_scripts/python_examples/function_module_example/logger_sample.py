"""
日志一共分为5个级别，从低到高分别是：DEBUG、INFO、WARNING、ERROR、CRITICAL (所有的设定默认级别都是 WARNING)
1.DEBUG：详细的信息，通常只出现在诊断问题上；
2.INFO：确认一切按预期运行；
3.WARNING：一个迹象表明，一些意想不到的事情发生了，或表明一些问题在不久的将来会发生(例如：磁盘空间低...等等)
4.ERROR：比较严重的问题，软件或程序没能执行一些功能；
5.CRITICAL：十分严重的错误，这表明程序本身可能无法继续运行。

日志格式说明：
%(levelno)s         # 打印日志级别的数值
%(levelname)s       # 打印日志级别名称
%(pathname)s        # 打印当前执行程序的路径，其实就是 sys.argv[0]
%(filename)s        # 打印当前执行程序名
%(funcName)s        # 打印日志的当前函数
%(lineno)d          # 打印日志的当前行号
%(asctime)s         # 打印日志的时间
%(thread)d          # 打印线程ID
%(threadName)s      # 打印线程名称
%(process)d         # 打印进程ID
%(message)s         # 打印日志信息

<<常用格式>>
这个格式可以输出日志的打印时间，模块名[代码所在行数]，日志级别，以及输出的日志内容
format = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
"""


import logging


def logger_sample(format_info='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                  level_info=logging.WARNING, record_file_path='', record_file_mode=''):
    """
    打印日志消息到控制台，或保存日志消息到文件中
    :param format_info: 日志格式，默认是输出日志的打印时间，模块名，输出的日志级别，以及输入的日志内容。
    :param level_info: 日志级别，默认是 WARNING，只有大于等于该等级的消息才会被记录
    :param record_file_path: 日志文件保存的路径，默认为空，如果传合法的文件路径进来，控制台则不打印日志消息，仅保存日志消息到文件中
    :param record_file_mode: 打开文档的模式
    :return:
    """
    logging.basicConfig(level=level_info, format=format_info, filename=record_file_path, filemode=record_file_mode)
    # Use logging
    logging.debug('This is a loggging debug message')
    logging.info('This is a loggging info message')
    logging.warning('This is loggging a warning message')
    logging.error('This is an loggging error message')
    logging.critical('This is a loggging critical message')


def logger_full(record_file_path, record_file_mode,
                format_info='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    """
    打印日志消息到控制台，并保存日志消息到文件中
    :param record_file_path: 日志文件保存的路径
    :param record_file_mode: 打开文档的模式
    :param format_info: 日志格式，默认是输出日志的打印时间，模块名，输出的日志级别，以及输入的日志内容。
    :return:
    """
    # 第一步，创建一个logger
    logger = logging.getLogger(__name__)  # __name__是以当前的模块名做为对象名，默认是RootLogger
    logger.setLevel(logging.DEBUG)  # Log等级总开关，（设置级别后，不管是输出到文件还是控制台都要大于等于该级别才会被记录）

    # 第二步，创建一个handler，用于写入日志文件
    fh = logging.FileHandler(record_file_path, mode=record_file_mode)
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    fh.setFormatter(logging.Formatter(format_info))  # 定义handler的输出格式
    logger.addHandler(fh)  # 将logger添加到handler里面

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
    ch.setFormatter(logging.Formatter(format_info))  # 定义handler的输出格式
    logger.addHandler(ch)  # 将logger添加到handler里面

    # Use logging
    logger.debug('This is a logger debug message')
    logger.info('This is a logger info message')
    logger.warning('This is a logger warning message')
    logger.error('This is a logger error message')
    logger.critical('This is a logger critical message')

    # logging异常处理
    try:
        raise ValueError('Value error')
    except Exception as ex:
        logger.exception(ex)  # 异常信息会被添加到日志消息中


if __name__ == '__main__':
    # 仅打印日志消息到控制台，不保存
    # logger_sample()
    # 在当前路径下创建log_sample.txt，保存日志消息到其中，不打印消息到控制台
    # logger_sample(record_file_path='./log_sample.txt', record_file_mode='w')

    # 在当前路径下创建log_sample.txt，保存日志消息到其中，并打印消息到控制台
    logger_full(record_file_path='./log_sample.txt', record_file_mode='w')
