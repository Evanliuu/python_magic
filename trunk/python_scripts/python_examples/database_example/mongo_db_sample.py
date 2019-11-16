"""
Mongodb条件查询:
1.   $gt:                      大于
2.   $lt:                      小于
3.   $gte:                     大于等于
4.   $lte:                     小于等于
5.   $ne:                      不等于   
6.   $in:                      在范围内
7.   $nin:                     不在在范围内
8.   $regex:                   使用正则表达式匹配
9.   $all:                     查找数据库中某一条数据是否全部包含all中的数据, 如果'全部'包含则返回该条数据,否则不返回
10.  $push:                    向已有数据源中按照字段进行数据的添加.基于'列表'
11.  $pop:                     将数据库中对应数据的某一个字段数据按照指定方式进行删除. 其中 -1:从列表的起始位置开始删除; 1: 从列表的最后位置开始删除
12.  $pull:                    将对应数据中指定的数据分布进行删除(按值删除)
13.  $or:                      或者指令, 该指令通常作为字典的键, 其对应的值是一个'列表'结构,列表中每一个元素之间是'并列'的关系.
14.  $and:                     在字典中所有的键值对之间代表的是一种'并且'的关系
15.  result.sort('age', 1):    将查找之后的结果按照指定的字段进行排序, 1为升序, -1为降序
16.  result.skip(m).limit(n):  将查找结果的取值显示为,跳过m条数据,显示n条数据, 即只显示m+1~m+1+n的数据

Mongodb数据更新指令：(指令必须使用双引号)
1: $inc增加值
    db.test.update({'id':2},{"$inc":{'id':2}})
    db.test.update({'id':6},{$inc:{id:2}})  # 在mongodb交互环境中的写法

2: $set设置字段值
    db.test.update({'id':6},{"$set":{'id':2}})
    db.test.update({'id':6},{$set:{id:2}})  # 在mongodb交互环境中的写法

3: $unset删除字段
    db.test.update({'id':6},{"$unset":{'id':6}})
    db.test.update({'id':6},{$unset:{id:6}})  # 在mongodb交互环境中的写法

4: $rename重命名字段
    db.test.update({'id':1},{"$rename":{'id':'userid'}})
    db.test.update({id:10},{$rename:{id:'userid'}})  # 在mongodb交互环境中的写法
"""
# -*- coding:utf-8 -*-
from pymongo import MongoClient


def mongodb_handle(host='localhost', port=27017):
    # 连接mongodb客户端
    client = MongoClient(host=host, port=port)

    # 创建数据库example
    database = client.example
    db_name = eval(str(database).split()[-1][:-1])
    print('创建数据库：{}'.format(db_name))
    # 创建集合sample
    collection = database.sample
    table_name = eval(str(collection).split()[-1][:-1])
    print('创建集合：{}'.format(table_name))

    name = dict(name='Evan')
    age = dict(stature=20)
    stature = dict(stature=177)

    # 插入数据到sample集合
    collection.insert_one(name)  # 插入单行数据
    collection.insert_many([age, stature])  # 插入多行数据
    # 更新sample集合中数据
    update_format = {"$inc": {'age': 6}}  # age + 6，更新age值为26
    collection.update_many(age, update_format)  # 更新多行数据
    result = collection.update_one(age, update_format)  # 更新单行数据
    print(result.matched_count)  # 查看更新个数
    # 查询sample集合中数据
    print(collection.find_one(age))  # 返回匹配到的第一个结果
    print(collection.find_one({'age': {'$lt': 25}}))  # 使用条件查询，返回结果小于25的数据
    print(collection.find_one({'stature': {'$regex': r'1\d\d'}}))  # 使用正则查询，返回结果等于100~199的整形
    print([i for i in collection.find(name)])  # 返回所有匹配结果
    print([i for i in collection.find()])  # 返回集合中所有数据
    # 查询数据个数
    collection.count_documents(name)
    # 删除sample集合中数据
    collection.delete_many(stature)  # 删除多行数据
    result = collection.delete_one(stature)  # 删除单行数据
    print(result.deleted_count)  # 查看删除个数
    # 关闭客户端连接
    client.close()


if __name__ == '__main__':
    mongodb_handle(host='localhost')
