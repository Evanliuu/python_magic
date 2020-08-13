# -*- coding:utf-8 -*-
"""
Pandas基本用法
"""
import os
import sys
import pandas as pd
import numpy as np

__author__ = 'Evan'


def build_series():
    """
    使用pandas创建Series对象（一维的数组型对象）
    :return:
    """
    # 创建数组
    pd.Series(dict(names='Evan', id=66))  # 使用字典生成一个Series（字典的键是行索引）
    test = pd.Series(['12k', '15k16k', '18k1', 'k20'], index=[1, 3, 5, 7])  # 使用列表生成一个Series，并指定行索引值（默认从0开始）
    test.name = 'Data'  # 指定数组名称
    test.index.name = 'Info'  # 指定行索引名称

    # 查看数组属性
    print('返回数组名称\n{}'.format(test.name))
    print('返回指定行索引内的值\n{}'.format(test[3]))
    print('返回数组的所有值\n{}'.format(test.values))
    print('返回数组的所有索引\n{}'.format(test.index))
    print('返回数组所有的唯一值（去重）\n{}'.format(test.unique()))
    print('返回数组所有值的出现次数（默认降序）\n{}'.format(test.value_counts()))
    print('计算数组中每个值是否包含于传入序列的值，返回一个布尔值\n{}'.format(test.isin(['aa', 'cc'])))

    # 强制转换为字符串类型
    test.astype(str)

    # 数组字符串操作常用方法（使用str属性：自动开启正则表达式模式）
    # cat：和指定字符进行拼接
    print('字符拼接（不指定参数）\n{}'.format(test.str.cat()))  # 返回一个字符串
    print('和指定字符进行拼接（指定“-”）\n{}'.format(test.str.cat(sep='-')))  # 返回一个字符串
    print('字符组合（每个字符末尾加xx）\n{}'.format(test.str.cat(others=['xx'] * len(test), sep='=')))  # 返回一个Series

    # extract：提取指定字符（如有多个符合规则，则会放入不同的列）
    print('提取所有的数字（extract）\n{}'.format(test.str.extract(r'(\d+)')))
    # extractall：基本与 extract 一样，但是能把多个匹配放入同一列(按 index 分组)
    print('提取所有的数字（extractall）\n{}'.format(test.str.extractall(r'(\d+)')))

    # split：和python内置方法一样
    # rsplit：和split用法一致，只不过默认是从右往左分隔
    # get：获取指定位置的字符，每项只能获取1个
    # contains：判断字符串是否含有指定子串，返回的是bool类型
    # match：和python正则中的match一样，是从头开始匹配的。返回布尔型，表示是否匹配给定的模式
    # replace：和python内置方法一样，替换指定字符串


def build_data_frame():
    """
    使用pandas创建DataFrame对象（二维的数组型对象）
    :return:
    """
    # 创建数组
    # 1. 使用嵌套字典格式创建DataFrame（字典的键作为列标签，内部字典的键作为行索引）
    data = {
        'Name': {'Evan': 1, 'Jane': 2},
        'Id': {'Evan': 11, 'Jane': 22}
    }
    print('使用嵌套字典构建DataFrame\n{}'.format(pd.DataFrame(data)))
    # 2. 使用字典列表格式创建DataFrame（字典的键为列标签，行索引默认从0开始，列表内的所有值是每一列的值）
    data = {
        'Name': ['Evan', 'Jane', 'Spring', 'Summer', 'Autumn', 'Winter'],
        'Id': [66, 77, 88, 99, 100, 110],
        'Stature': [177, 160, 150, 167, 180, 190],
        'Weight': [65, 45, 50, 60, 65, 70]
    }
    # 指定行索引值、列标签顺序（使用columns参数时，只会读取该列表内的列索引数据）
    frame = pd.DataFrame(data, columns=['Id', 'Name', 'Weight', 'Stature'], index=[3, 2, 1, 6, 5, 4])
    print('构建指定列标签顺序和行索引的DataFrame\n{}'.format(frame))

    # 查看数组属性
    print('返回数组的行索引是否唯一\n{}'.format(frame.index.is_unique))
    print('返回数组的头5行\n{}'.format(frame.head()))
    print('返回指定行索引内的指定列标签值（使用轴标签）\n{}'.format(frame.loc[2, ['Id', 'Weight']]))  # 使用行索引和列标签的值
    print('返回指定行索引内的指定列标签值（使用整数标签）\n{}'.format(frame.iloc[1, [0, 2]]))  # 使用行索引和列标签的位置
    print('返回指定行索引内的所有值\n{}'.format(frame.loc[2]))
    print('返回指定列标签内的所有值\n{}'.format(frame['Name']))
    print('返回数组所有的列标签\n{}'.format(frame.columns))
    print('返回数组所有的值\n{}'.format(frame.values))
    print('返回数组中所有值在每一列的出现次数（没有的默认为0）\n{}'.format(frame.apply(pd.value_counts).fillna(0)))
    print('返回数组中指定列标签内所有值的出现次数\n{}'.format(pd.value_counts(frame['Weight'])))
    print('返回数组中指定列标签内所有的唯一值（去重）\n{}'.format(pd.unique(frame['Weight'])))


def array_operations():
    """
    数组操作
    :return:
    """
    data = {
        'Name': ['Evan', 'Jane', 'Spring', 'Summer', 'Autumn', 'Winter'],
        'Id': [66, 77, 88, 99, 100, 110],
        'Stature': [177, 160, 150, 167, 180, 190],
        'Weight': [65, 45, 50, 60, 65, 70]
    }
    frame = pd.DataFrame(data, columns=['Id', 'Name', 'Weight', 'Stature'], index=[3, 2, 1, 6, 5, 4])
    # 对数组排序
    # inplace默认False，代表是否改变原数组，为True时返回None，False返回一个新数组
    print('根据行索引排序（默认升序）\n{}'.format(frame.sort_index(inplace=True)))
    print('根据行索引排序（降序）\n{}'.format(frame.sort_index(ascending=False)))  # 指定降序
    print('根据列标签排序\n{}'.format(frame.sort_index(axis='columns')))
    data = pd.Series([3, 6, -5, 8, 3])
    print('根据数组值排序\n{}'.format(data.sort_values()))
    print('根据指定列标签排序\n{}'.format(frame.sort_values(by=['Weight', 'Stature'])))

    # 对数组排名
    print('对所有值进行排名（默认升序）\n{}'.format(data.rank()))  # 默认升序排名，平级全部取平均值
    print('对所有值进行排名（降序）\n{}'.format(data.rank(ascending=False)))  # 降序排名，平级全部取平均值
    print('平级关系取最小值，占用坑位\n{}'.format(data.rank(method='min')))  # 平级关系全部取最小值，每个平级关系占用一个坑位
    print('平级关系取最小值，不占用坑位\n{}'.format(data.rank(method='dense')))  # 平级关系全部取最小值，平级关系不占用坑位
    print('平级关系取最大值，占用坑位\n{}'.format(data.rank(method='max')))  # 平级关系全部取最大值，每个平级关系占用一个坑位
    print('按观察顺序排名\n{}'.format(data.rank(method='first')))  # 按照值在数据中出现的次序分配排名

    # 重构数组
    # ffill向前填充（缺失值和其前面的值相同），bfill向后填充（缺失值和其后面的值相同）
    print('重新构建数组的行索引\n{}'.format(frame.reindex([1, 3, 5, 7], method='ffill')))
    # fill_value赋给缺失值
    print('重新构建数组的行索引\n{}'.format(frame.reindex([2, 4, 6, 8], fill_value='world')))
    print('重新构建数组的列标签\n{}'.format(frame.reindex(columns=['Id', 'Weight', 'happy'], fill_value='news')))

    # 删除指定的项目
    print('删除指定行\n{}'.format(frame.drop([1, 3])))
    print('删除指定列\n{}'.format(frame.drop(['Id', 'Weight'], axis='columns')))  # axis控制轴的位置，默认为index


def file_operations():
    """
    使用pandas载入存储文件
    :return:
    """
    data = pd.DataFrame([[1, 2, 3, '11'], [4, 5, 6, '22'], [7, 8, 9, None]], columns=['a', 'b', 'c', 'd'])
    # 写入读取CSV文件
    file_name = 'example.csv'
    # index：是否写入行索引，header：是否写入列标签
    # columns：可指定写入对应的列标签数据并且有顺序，na_rep会赋值给缺失值（默认为空）
    data.to_csv(file_name, index=False, header=False, columns=['b', 'd', 'a'], na_rep='NULL')  # 写入CSV文件
    data.to_csv(sys.stdout, sep='|')  # 输出到屏幕，sep为分隔符（可用于临时查看写入的数据）
    print('读取CSV文件')
    print('自动分配默认列标签（从0开始）\n{}'.format(pd.read_csv(file_name, header=None)))
    print('指定列标签顺序\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'])))
    print('指定"a"列的值为行索引\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'], index_col='a')))
    print('指定"a"列和"b"列的值为行索引（分层索引）\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'], index_col=['a', 'b'])))
    print('使用缺失值替换文件内的指定值\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'], na_values={'b': [5, 8]})))
    # pd.options.display.max_rows = 5  # 设置文件读取显示的行数，多出的行数变为省略号显示
    print('跳过指定的行读取\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'], skiprows=[0, 2])))  # 跳过第0行和第2行
    print('读取指定的行范围\n{}'.format(pd.read_csv(file_name, names=['a', 'b', 'c'], nrows=2)))  # 只读取前2行
    os.remove(file_name)

    # 写入读取Excel文件
    file_name = 'example.xls'
    data.to_excel(file_name, index=True, header=True, sheet_name='sheet1', na_rep='NULL')
    print('读取Excel文件')
    print(pd.read_excel(file_name, sheet_name='sheet1'))
    os.remove(file_name)

    # 写入读取JSON文件
    file_name = 'example.json'
    data.to_json(file_name)
    print('读取JSON文件')
    print(pd.read_json(file_name))
    os.remove(file_name)

    # 读取TXT文件
    print('读取TXT文件')
    file_name = 'example.txt'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(['A,B,C\n', '1,2,3\n', '4,5,6\n', '4,5,6\n'])
    print(pd.read_csv(file_name, sep=','))  # 使用sep根据逗号切分每个数据
    os.remove(file_name)


def data_cleansing():
    """
    数据清洗
    :return:
    """
    nan = np.NAN
    # 过滤缺失值
    data = pd.DataFrame([[1, 2, 3], [4, 5, nan], [None, nan, nan], [1, 2, 3]], columns=['a', 'b', 'c'])
    print('过滤所有包含缺失值的行\n{}'.format(data.dropna()))  # 默认删除包含缺失值的行
    print('过滤所有包含缺失值的列\n{}'.format(data.dropna(axis='columns')))
    print('过滤所有值均为NA的行\n{}'.format(data.dropna(how='all')))  # 只删除所有值均为NA的行
    print('过滤并保留包含一定数量NA的行\n{}'.format(data.dropna(thresh=1)))  # 保留一行NA值

    # 补全缺失值
    print('补全所有缺失值\n{}'.format(data.fillna(0)))  # 全部的缺失值变为0
    print('只补全指定列标签内的缺失值\n{}'.format(data.fillna({'a': 0, 'b': 1})))  # 只补全"a"列和"b"列的缺失值
    print('补全所有缺失值（向前填充）\n{}'.format(data.fillna(method='ffill', limit=1)))  # 向前填充（缺失值和其前面的值相同），limit为最大填充范围
    print('补全所有缺失值（向后填充）\n{}'.format(data.fillna(method='bfill')))  # 向后填充（缺失值和其后面的值相同）

    # 删除重复值
    print('删除所有重复的行（默认保留第一个观测到的行）\n{}'.format(data.drop_duplicates()))
    print('删除所有重复的行（保留最后一个观测到的行）\n{}'.format(data.drop_duplicates(keep='last')))
    print('删除指定列标签下重复的行\n{}'.format(data.drop_duplicates(['b'])))

    # 替代值
    print('替换所有的NA为0\n{}'.format(data.replace(nan, 0)))
    print('替换指定数量的值\n{}'.format(data.replace({1: 10, 2: 20})))  # 1替换为10，2替换为20

    # 重命名轴索引
    print('重命名行索引\n{}'.format(data.rename(index={1: 10})))
    print('重命名列标签\n{}'.format(data.rename(columns={'c': 'cc'})))


def data_structured():
    """
    数据规整
    :return:
    """
    # Series分层索引
    data = pd.Series(np.random.randn(6), index=[['a', 'a', 'b', 'b', 'c', 'c'], [1, 2, 3, 1, 2, 3]])
    print('创建Series分层索引\n{}'.format(data))
    print('分层索引重新排列\n{}'.format(data.unstack()))  # 第二索引变为列标签（Series对象转化为DataFrame对象）
    print('分层索引复原\n{}'.format(data.unstack().stack()))

    # DataFrame分层索引
    data = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                        columns=[['one', 'one', 'two'], ['three', 'four', 'five']])
    # 定义层级行名称和列名称
    data.index.names = ['key1', 'key2']
    data.columns.names = ['number1', 'number2']
    print('创建DataFrame分层索引\n{}'.format(data))

    # 层级交换（数据不会跟着变）
    print('行层级名称交换（使用名称）\n{}'.format(data.swaplevel('key1', 'key2')))
    print('列层级名称交换（使用序号）\n{}'.format(data.swaplevel(0, 1, axis='columns')))

    # 层级排序（数据会跟着变）
    print('行层级名称排序\n{}'.format(data.sort_index(level=1)))
    print('列层级名称排序\n{}'.format(data.sort_index(level=1, axis='columns')))

    # 按层级进行汇总统计
    print('按行层级求和\n{}'.format(data.sum(level='key1')))
    print('按列层级求和\n{}'.format(data.sum(level='number2', axis='columns')))

    # 将DataFrame的列变为行索引
    data = pd.DataFrame(np.arange(12).reshape((4, 3)), columns=['a', 'b', 'c'])
    print('将DataFrame的列变为行索引（移除该列）\n{}'.format(data.set_index(['c'])))  # "c"会从数组中移除变为行索引
    print('将DataFrame的列变为行索引（保留该列）\n{}'.format(data.set_index(['c'], drop=False)))  # "c"会保留在数组中


if __name__ == '__main__':
    build_series()  # 构建Series对象
    # build_data_frame()  # 构建DataFrame对象
    # array_operations()  # 数组操作
    # file_operations()  # 文件操作
    # data_cleansing()  # 数据清洗
    # data_structured()  # 数据规整
