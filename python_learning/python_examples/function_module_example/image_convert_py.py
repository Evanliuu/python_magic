# -*- coding:utf-8 -*-
import base64
import importlib

__author__ = 'Evan'


def image_covert_to_py(image_list=[], py_name=''):
    """
    将图像文件转换为.py文件
    :param list image_list: 每个图像文件的路径
    :param str py_name: 转换后的python文件名
    :return:
    """
    write_data = []
    for each_image in image_list:
        with open(each_image, 'rb') as rf:
            b64str = base64.b64encode(rf.read())  # 将图像二进制数据转换为base64编码
        image_variable = each_image.replace('.', '_')  # 创建python变量名保存base64数据
        write_data.append('%s = "%s"\n' % (image_variable, b64str.decode()))

    with open('{}.py'.format(py_name), 'w') as wf:
        for data in write_data:
            wf.write(data)  # 将base64写入到python文件，保存到字符串中，下次使用时直接调用python变量获取


def get_py_image(image_list=[], py_name=''):
    """
    取出python文件里的image字符串并写入到图像文件
    :param image_list: 每个图像文件名
    :param py_name: 要读取的python文件名
    :return:
    """
    # 动态import python文件
    py_object = importlib.import_module('{}'.format(py_name))  # 此对象用于给eval()使用
    for each_image in image_list:
        image_name = 'new_{}'.format(each_image)
        with open(image_name, 'wb') as wf:
            image_variable = each_image.replace('.', '_')
            base64_data = base64.b64decode(eval('py_object.{}'.format(image_variable)))  # 动态取出对应的image变量
            wf.write(base64_data)
            print('成功写入 << {} >> 图像'.format(image_name))


if __name__ == '__main__':
    image_covert_to_py(image_list=['Rudder.ico', 'Star.PNG'], py_name='image_storage')
    get_py_image(image_list=['Rudder.ico', 'Star.PNG'], py_name='image_storage')
