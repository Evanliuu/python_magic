import matplotlib.pyplot as plt


def plot(title, data_list=[], x_label=(), y_label=()):
    """
    绘图
    :param str title: 图片标题
    :param list data_list: 数据列表
    :param tuple x_label: （X轴标签，X轴刻度标签）
    :param tuple y_label:（Y轴标签，Y轴刻度标签）
    :return:
    """
    # 处理中文乱码
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.title(title)  # 添加标题
    plt.bar(range(len(data_list)), data_list, align='center', color='steelblue', alpha=0.8)  # 绘柱形图

    plt.xlabel(x_label[0])  # 添加X轴标签
    plt.xticks(range(len(data_list)), x_label[1])  # 添加X轴刻度标签

    plt.ylabel(y_label[0])  # 添加Y轴标签
    plt.ylim(y_label[1])  # 设置Y轴的刻度范围

    # 为每个条形图添加数值标签
    for x, y in enumerate(data_list):
        plt.text(x, y+100, '%s' % round(y, 1), ha='center')

    plt.show()  # 显示图形
    # plt.savefig('./123.jpg')  # 保存图片


if __name__ == '__main__':
    city_title = '四个直辖市GDP大比拼'
    data = [12406.8, 13908.57, 9386.87, 9143.64]
    x_label_tuple = ('城市分布', ['北京市', '上海市', '天津市', '重庆市'])
    y_label_tuple = ('GDP', [5000, 15000])
    plot(title=city_title, data_list=data, x_label=x_label_tuple, y_label=y_label_tuple)
