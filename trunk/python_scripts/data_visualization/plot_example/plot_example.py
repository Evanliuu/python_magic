# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt

__author__ = 'Evan'


def plot(title, data_list=[], x_label=(), y_label=()):
    """
    绘柱形图
    :param str title: 图片标题
    :param list data_list: 数据列表
    :param tuple x_label: （X轴标签，X轴刻度标签）
    :param tuple y_label:（Y轴标签，Y轴刻度标签）
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    item_range = range(len(data_list[0]))  # 计算所有数据的长度
    plt.title(title)  # 添加标题

    # 绘X轴刻度的第一个柱形图（宽度0.4）
    plt.bar(item_range, data_list[0], align='center',
            alpha=0.8, width=0.4)
    # 向右移动0.4 绘X轴刻度的第二个柱形图（宽度0.4）
    plt.bar([i+0.4 for i in item_range], data_list[1], align='center',
            color='y', alpha=0.8, width=0.4)

    plt.xlabel(x_label[0])  # 添加X轴标签
    plt.xticks([i+0.2 for i in item_range], x_label[1])  # 添加X轴刻度标签（向右移动0.2居中摆放）

    plt.ylabel(y_label[0])  # 添加Y轴标签
    plt.ylim(y_label[1])  # 设置Y轴的刻度范围

    # 为X轴刻度的第一个柱形图加数值标签
    for x, y in enumerate(data_list[0]):
        plt.text(x, y+10, '%s' % round(y, 1), ha='center')
    # 向右移动0.4 为X轴刻度的第二个柱形图添加数值标签
    for x, y in enumerate(data_list[1]):
        plt.text(x+0.4, y+10, '%s' % round(y, 1), ha='center')

    plt.show()  # 显示图形
    # plt.savefig('./example.jpg')  # 保存图片


if __name__ == '__main__':
    city_title = '四个直辖市GDP大比拼'
    data = [[100, 300, 500, 700], [200, 400, 600, 800]]
    x_label_tuple = ('城市分布', ['北京市', '上海市', '天津市', '重庆市'])
    y_label_tuple = ('GDP', [50, 1000])
    plot(title=city_title, data_list=data, x_label=x_label_tuple, y_label=y_label_tuple)
