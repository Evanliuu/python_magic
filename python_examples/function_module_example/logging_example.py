"""日志一共分为5个级别，从低到高分别是: DEBUG、INFO、WARNING、ERROR、CRITICAL (所有的默认级别都是 WARNING)
1. DEBUG:           # 程序调试信息，通常只会出现在诊断问题上
2. INFO:            # 程序运行正常，增加一些提示信息
3. WARNING:         # 程序警告信息，用于一些突发事件
4. ERROR:           # 比较严重的问题，程序没能执行一些功能
5. CRITICAL:        # 十分严重的错误，程序可能会中断或者崩溃

<<日志格式说明>>
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
# -*- coding:utf-8 -*-
import logging

__author__ = 'Evan'


def simple_logger(save_log_path='', file_mode='a',
                  format_info='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                  level_info=logging.INFO):
    """
    打印日志消息到控制台，或保存日志消息到文件中
    :param save_log_path: 日志文件保存路径，默认为空，如果传入有效的文件路径，控制台则不打印日志消息，仅保存日志消息到文件中
    :param file_mode: 文档打开模式，默认为追加模式
    :param format_info: 日志格式，默认是输出日志的打印时间，模块名，输出的日志级别，以及输入的日志内容。
    :param level_info: 日志级别，默认是 INFO，只有大于等于该等级的消息才会被记录
    :return:
    """
    logging.basicConfig(filename=save_log_path, filemode=file_mode, level=level_info, format=format_info)
    # logging test
    logging.debug('This is debug message')
    logging.info('This is info message')
    logging.warning('This is warning message')
    logging.error('This is error message')
    logging.critical('This is critical message')


def full_logger(save_log_path, file_mode='a',
                format_info='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    """
    打印日志消息到控制台，并保存日志消息到文件中
    :param save_log_path: 日志文件保存路径
    :param file_mode: 文档打开模式，默认为追加模式
    :param format_info: 日志格式，默认是输出日志的打印时间，模块名，输出的日志级别，以及输入的日志内容。
    :return:
    """
    # 第一步，创建一个logger
    logger = logging.getLogger(__name__)  # __name__是以当前的模块名做为对象名，默认是RootLogger
    logger.setLevel(logging.DEBUG)  # Log等级总开关，（设置级别后，不管是输出到文件还是控制台都要大于等于该级别才会被记录）

    # 第二步，创建一个handler，用于写入日志文件
    fh = logging.FileHandler(save_log_path, mode=file_mode)
    fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
    fh.setFormatter(logging.Formatter(format_info))  # 定义handler的输出格式
    logger.addHandler(fh)  # 将logger添加到handler里面

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
    ch.setFormatter(logging.Formatter(format_info))  # 定义handler的输出格式
    logger.addHandler(ch)  # 将logger添加到handler里面

    # logger test
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
    logger.error('This is error message')
    logger.critical('This is critical message')

    # logging异常处理
    try:
        raise ValueError('Value error')
    except Exception as ex:
        logger.exception(ex)  # 异常信息会被添加到日志消息中


if __name__ == '__main__':
    # TODO 仅打印日志消息到控制台，不保存
    # logger_sample()

    # 在当前路径下创建simple_logger.txt，保存日志消息到其中，不打印消息到控制台
    simple_logger(save_log_path='./simple_logger.txt', file_mode='w')
    # 在当前路径下创建full_logger.txt，保存日志消息到其中，并打印消息到控制台
    full_logger(save_log_path='./full_logger.txt', file_mode='w')
