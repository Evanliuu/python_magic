# -*- coding:utf-8 -*-
from matplotlib import pyplot as plt

__author__ = 'Evan'


def draw_pie():
    """
    绘制饼状图
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title("饼状图")  # 添加标题
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼图才是圆的

    label_list = ["第一部分", "第二部分", "第三部分"]  # 饼图数据标签
    data = [55, 35, 10]  # 饼图各部分数据
    color = ["r", "g", "b"]  # 饼图各部分颜色
    explode = [0.05, 0, 0]  # 饼图各部分突出值（突出值代表与饼图中心点的距离，默认是0）

    """
    pie部分参数用法:
    x：写入数据（list）
    explode：设置各部分突出值
    label:：设置各部分标签
    labeldistance：设置标签文本距圆心位置，1.1表示1.1倍半径
    autopct：设置圆里面文本
    shadow：设置是否有阴影
    startangle：起始角度，默认从0开始逆时针转
    pctdistance：设置圆内文本距圆心距离
    """
    plt.pie(x=data, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=True,
            startangle=90, pctdistance=0.6)
    plt.legend()
    plt.show()  # 显示图形


if __name__ == '__main__':
    draw_pie()
