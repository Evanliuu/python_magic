# -*- coding:utf-8 -*-
"""
Matplotlib基本用法
"""
import numpy as np
from matplotlib import pyplot as plt

__author__ = 'Evan'


def build_figure():
    """
    创建图形和子图
    :return:
    """
    # 创建一个新的空白图片
    fig = plt.figure()

    # 添加指定位置子图（使用add_subplot最多创建4个）
    ax1 = fig.add_subplot(2, 2, 1)  # 添加一个2x2的空白子图（位置为1）
    ax2 = fig.add_subplot(2, 2, 2)  # 位置为2
    ax3 = fig.add_subplot(2, 2, 3)  # 位置为3
    # 绘制子图
    ax1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)  # 在子图1上绘制直方图
    ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))  # 在子图2上绘制散点图
    ax3.bar(range(10), [np.random.randint(1, 10) for i in range(10)])  # 在子图3上绘制柱状图

    # 创建任意数量子图（返回值- fig：图片大小，axes：二维数组类型的图片对象）
    fig, axes = plt.subplots(nrows=2, ncols=3)  # 创建一个新的空白图片，添加2行3列的空白子图
    # 绘制子图
    axes[0, 0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)  # 在子图[0, 0]位置绘制直方图
    axes[1, 0].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))  # 在子图[1, 0]位置绘制散点图
    axes[1, 1].bar(range(10), [np.random.randint(1, 10) for i in range(10)])  # 在子图[1, 1]位置绘制柱状图

    # 设置当前各个子图之间的间距（wspace：图片宽度，hspace：高度百分比）
    plt.subplots_adjust(wspace=0.2, hspace=0.2)
    plt.show()  # 显示图片


def set_figure_attribute():
    """
    设置图形属性
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置全局属性，自定义组件属性（包含：figure、axes、xtick、ytick、grid、legend）
    plt.rc(group='figure', figsize=(10, 5))  # 设置所有的figure数字大小为10x10

    # 设置颜色（color）、标签（linestyle）和线类型（marker）
    plt.plot(np.random.randn(30).cumsum(), color='k', linestyle='--', marker='o')  # plot会默认在当前最后一个子图上绘制

    # 设置标题、标签和刻度
    # 第一种方式（直接用plt添加，只对当前最后一个图生效）
    plt.figure()  # 创建一个新的空白图片
    plt.plot([np.random.randint(1, 10) for i in range(10)])  # 绘制折线图
    plt.title('示例')  # 设置标题

    plt.xlabel('X轴标签')  # 添加X轴标签
    plt.xticks(ticks=range(10), labels=range(1, 11))  # 添加X轴刻度值（ticks：刻度位置或值（labels不定义则默认用此值），labels：刻度值）
    # plt.xlim([0, 10])  # 添加X轴刻度范围

    plt.ylabel('Y轴标签')  # 添加Y轴标签
    # plt.yticks([0, 5, 10])  # 添加Y轴刻度值
    plt.ylim([1, 11])  # 添加Y轴刻度范围

    # 第二种方式（使用子图的set方式添加，可以对任一子图使用）
    fig = plt.figure()  # 创建一个新的空白图片
    ax = fig.add_subplot(1, 1, 1)  # 添加一个子图
    ax.plot([np.random.randint(1, 11) for i in range(10)])  # 绘制折线图
    ax.set_title('示例')

    ax.set_xlabel('X轴标签')
    ax.set_xticks(ticks=range(10))  # 添加刻度位置或值（labels不定义则默认用此值）
    ax.set_xticklabels(labels=range(1, 11), rotation=30, fontsize='small')  # 添加labels，rotation为旋转度数
    # ax.set_xlim([0, 10])

    ax.set_ylabel('Y轴标签')
    # ax.set_yticks(ticks=range(10))  # 添加刻度位置或值（labels不定义则默认用此值）
    # ax.set_yticklabels(labels=range(1, 11), rotation=30, fontsize='small')  # 添加labels，rotation为旋转度数
    ax.set_ylim([1, 11])

    # 第三种方式（使用字典格式批量设置绘图属性）
    # props = {
    #     'title': '示例',
    #     'xlabel': 'X轴标签',
    #     'xticks': range(11),
    #     'ylabel': 'Y轴标签',
    #     'ylim': [1, 11],
    # }
    # ax.set(**props)

    plt.legend(loc='best')  # 添加图例（label）
    plt.show()  # 显示图片


def save_figure():
    """
    保存图片
    :return:
    """
    fig = plt.figure()  # 创建一个新的空白图片
    ax = fig.add_subplot(1, 1, 1)  # 添加一个子图
    ax.plot([np.random.randint(1, 11) for i in range(10)])  # 绘制折线图

    # dpi：每英寸点数的分辨率（默认为100），bbox_inches：要保存的图片范围，如果设置为"tight"将会去除掉图片周围空白的部分
    plt.savefig(fname='example.jpg', dpi=120, bbox_inches='tight')  # 保存图片


if __name__ == '__main__':
    build_figure()  # 创建图形和子图
    set_figure_attribute()  # 设置图形属性
    save_figure()  # 保存图片
