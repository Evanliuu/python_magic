"""
Pandas使用例子
"""
import pandas as pd

# Series => 一维的数组型对象（长度固定且有序的字典）
pd.Series([1, 2, 3], index=['a', 'b', 'c'])  # 使用列表生成一个Series，并指定行标签值（默认从0开始）
test = pd.Series(dict(names='Evan', id=66))  # 使用字典生成一个Series（字典的键是行标签）
test.name = 'Data'  # 指定数组名称
test.index.name = 'Info'  # 指定行标签名称
print('返回数组名称\n{}'.format(test.name))
print('返回指定行标签内的值\n{}'.format(test.names))
print('返回数组的所有值\n{}'.format(test.values))
print('返回数组的所有索引\n{}'.format(test.index))

# DataFrame => 矩阵数组型对象（二维或以上）
data = {
    'Name': ['Evan', 'Jane', 'Spring', 'Summer', 'Autumn', 'Winter'],
    'Id': [66, 77, 88, 99, 100, 110],
    'Stature': [177, 160, 150, 167, 180, 190],
    'Weight': [65, 45, 50, 60, 65, 70]
}
# 指定列标签顺序、行标签值（默认从0开始）
frame = pd.DataFrame(data, columns=['Id', 'Name', 'Weight', 'Stature'], index=['1', '2', '3', '4', '5', '6'])
print('返回数组的头5行\n{}'.format(frame.head()))
print('返回指定行标签内的所有值\n{}'.format(frame.loc['2']))
print('返回指定列标签内的所有值\n{}'.format(frame['Name']))
print('返回所有的列标签\n{}'.format(frame.columns))
