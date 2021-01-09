# -*- coding:utf-8 -*-
"""
configparser用法：
1.读取配置文件
- read(filename) 直接读取ini文件内容
- sections() 得到所有的section，并以列表的形式返回
- options(section) 得到该section的所有option
- items(section) 得到该section的所有键值对
- get(section, option) 得到section中option的值，返回为string类型
- getint(section, option) 得到section中option的值，返回为int类型

2.写入配置文件
- add_section(section) 添加一个新的section
- set(section, option, value) 对section中的option进行设置
"""
import configparser

__author__ = 'Evan'


def read_ini_file(section, option, file='config.ini'):
    """
    读取ini文件
    :param section:
    :param option:
    :param file:
    :return:
    """
    config = configparser.ConfigParser()
    config.read(file)  # 读取ini文件

    print('*' * 80)
    print('所有section key: {}'.format(config.sections()))
    print('section [{}] 下所有option值: {}'.format(section, config.options(section)))
    print('section [{}] 下所有键值对: {}'.format(section, config.items(section)))
    print('*' * 80)

    value = config.get(section, option)  # 获取指定的value
    print(f'Read result：section={section}, option={option}, value={value}')
    return value


def update_ini_file(section, option, value, file='config.ini'):
    """
    更新ini文件，如果section or option不存在则创建一个新的
    :param section:
    :param option:
    :param value:
    :param file:
    :return:
    """
    config = configparser.ConfigParser()
    config.read(file)  # 读取ini文件
    try:
        config.set(section, option, value)  # 更新value
        config.write(open(file, 'r+'))  # 更新最新的config到文件
    except Exception as ex:
        config = configparser.ConfigParser()  # 重新实例化覆盖之前的config
        if 'No section:' in str(ex):
            config.add_section(section)  # 创建section

        config.set(section, option, value)  # 更新value
        config.write(open(file, 'a+'))  # 写入最新的config到文件


if __name__ == '__main__':
    read_ini_file(section='name', option='evan')  # 读取ini文件

    # update_ini_file(section='new', option='new', value='new')  # 创建new section
    # read_ini_file(section='new', option='new')  # 读取ini文件

    # update_ini_file(section='new', option='new', value='update')  # 更新new section里面的值
    # read_ini_file(section='new', option='new')  # 读取ini文件
