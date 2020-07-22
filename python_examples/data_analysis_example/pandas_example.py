"""
Pandas使用例子
"""
import pandas as pd


# Series => 一维的数组型对象（长度固定且有序的字典）
# 创建数组
pd.Series(dict(names='Evan', id=66))  # 使用字典生成一个Series（字典的键是行索引）
test = pd.Series(['11', '33', '55'], index=[1, 3, 5])  # 使用列表生成一个Series，并指定行索引值（默认从0开始）
test.name = 'Data'  # 指定数组名称
test.index.name = 'Info'  # 指定行索引名称
# 查看数组属性
print('返回数组名称\n{}'.format(test.name))
print('返回指定行索引内的值\n{}'.format(test[3]))
print('返回数组的所有值\n{}'.format(test.values))
print('返回数组的所有索引\n{}'.format(test.index))


# DataFrame => 二维的数组型对象（或多维）
# 创建数组
data = {
    'Name': {'Evan': 1, 'Jane': 2},
    'Id': {'Evan': 11, 'Jane': 22}
}
print('使用嵌套字典构建DataFrame\n{}'.format(pd.DataFrame(data)))  # 字典的键作为列标签，内部字典的键作为行索引
data = {
    'Name': ['Evan', 'Jane', 'Spring', 'Summer', 'Autumn', 'Winter'],
    'Id': [66, 77, 88, 99, 100, 110],
    'Stature': [177, 160, 150, 167, 180, 190],
    'Weight': [65, 45, 50, 60, 65, 70]
}
frame = pd.DataFrame(data, columns=['Id', 'Name', 'Weight', 'Stature'], index=[1, 2, 3, 4, 5, 6])
print('构建指定列标签顺序的DataFrame\n{}'.format(frame))  # 指定列标签顺序、行索引值（默认从0开始）
# 查看数组属性
print('返回数组的头5行\n{}'.format(frame.head()))
print('返回指定行索引内的指定列标签值（使用轴标签）\n{}'.format(frame.loc[2, ['Id', 'Weight']]))  # 使用行索引和列标签的值
print('返回指定行索引内的指定列标签值（使用整数标签）\n{}'.format(frame.iloc[1, [0, 2]]))  # 使用行索引和列标签的位置
print('返回指定行索引内的所有值\n{}'.format(frame.loc[2]))
print('返回指定列标签内的所有值\n{}'.format(frame['Name']))
print('返回数组所有的列标签\n{}'.format(frame.columns))
print('返回数组所有的值\n{}'.format(frame.values))


# 数组操作（Serials和DataFrame同理）
# ffill向前填充（缺失值和其前面的值相同），bfill向后填充（缺失值和其后面的值相同）
print('重新构建数组的行索引\n{}'.format(frame.reindex([1, 3, 5, 7], method='ffill')))
# fill_value赋给缺失值
print('重新构建数组的行索引\n{}'.format(frame.reindex([2, 4, 6, 8], fill_value='world')))
print('重新构建数组的列标签\n{}'.format(frame.reindex(columns=['Id', 'Weight', 'happy'], fill_value='news')))
# inplace默认False，代表是否影响原数组，为True时返回None，否则返回一个新数组
frame.drop([1, 3], inplace=True)
print('删除指定行\n{}'.format(frame))
print('删除指定列\n{}'.format(frame.drop(['Id', 'Weight'], axis='columns')))  # axis控制轴的位置
