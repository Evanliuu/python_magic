# -*- coding:utf-8 -*-
"""
Pandas使用例子
"""
import pandas as pd


# TODO Series => 一维的数组型对象（长度固定且有序的字典）
# 创建数组
pd.Series(dict(names='Evan', id=66))  # 使用字典生成一个Series（字典的键是行索引）
test = pd.Series(['aa', 'bb', 'cc', 'aa'], index=[1, 3, 5, 7])  # 使用列表生成一个Series，并指定行索引值（默认从0开始）
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


# TODO DataFrame => 二维的数组型对象（或多维）
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
frame = pd.DataFrame(data, columns=['Id', 'Name', 'Weight', 'Stature'], index=[3, 2, 1, 6, 5, 4])  # 指定列标签顺序、行索引值
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


# TODO 数组操作（Serials和DataFrame一致）
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

# 重新构建数组
# ffill向前填充（缺失值和其前面的值相同），bfill向后填充（缺失值和其后面的值相同）
print('重新构建数组的行索引\n{}'.format(frame.reindex([1, 3, 5, 7], method='ffill')))
# fill_value赋给缺失值
print('重新构建数组的行索引\n{}'.format(frame.reindex([2, 4, 6, 8], fill_value='world')))
print('重新构建数组的列标签\n{}'.format(frame.reindex(columns=['Id', 'Weight', 'happy'], fill_value='news')))

# 删除指定的项目
print('删除指定行\n{}'.format(frame.drop([1, 3])))
print('删除指定列\n{}'.format(frame.drop(['Id', 'Weight'], axis='columns')))  # axis控制轴的位置，默认为index
