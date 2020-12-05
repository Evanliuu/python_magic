# -*- coding:utf-8 -*-
import configparser

__author__ = 'Evan'


def read_ini_file(section, option, file='config.ini'):
    """读取ini文件"""
    config = configparser.ConfigParser()
    config.read(file)  # 读取ini文件

    value = config.get(section, option)  # 获取指定的value
    print(f'Read result：section={section}, option={option}, value={value}')
    return value


def update_ini_file(section, option, value, file='config.ini'):
    """更新ini文件，如果section or option不存在则创建一个新的"""
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

    update_ini_file(section='new', option='new', value='new')  # 创建new section
    read_ini_file(section='new', option='new')  # 读取ini文件

    update_ini_file(section='new', option='new', value='update')  # 更新ini文件
    read_ini_file(section='new', option='new')  # 读取ini文件
