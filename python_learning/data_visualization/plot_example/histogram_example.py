# -*- coding:utf-8 -*-
import numpy
from matplotlib import pyplot as plt

__author__ = 'Evan'


def draw_histogram():
    """
    绘制柱状图
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title('四个直辖市GDP大比拼')  # 添加标题

    data_list = [[100, 300, 500, 700], [200, 400, 600, 800]]  # 柱状图数据
    item_range = range(len(data_list[0]))  # 计算所有数据的长度

    x_label = ['城市分布', ['北京市', '上海市', '天津市', '重庆市']]  # X轴大标签和刻度标签
    y_label = ['GDP', [50, 1000]]  # Y轴大标签和刻度标签

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


def draw_hist():
    """
    绘制直方图
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 随机生成服从正态分布的数据
    data = numpy.random.randn(10000)

    """
    hist部分参数用法:
    data：必选参数，绘图数据
    bins：直方图的长条形数目，可选项，默认为10
    normed：是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
    facecolor：长条形的颜色
    edgecolor：长条形边框的颜色
    alpha：透明度
    """
    plt.hist(data, bins=40, density=0, facecolor="blue", edgecolor="black", alpha=0.7)
    plt.xlabel("区间")  # 显示横轴标签
    plt.ylabel("频数/频率")  # 显示纵轴标签
    plt.title("频数/频率分布直方图")  # 显示图标题
    plt.show()


if __name__ == '__main__':
    draw_histogram()  # 绘制柱形图
    draw_hist()  # 绘制直方图
