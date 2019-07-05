from pymongo import MongoClient


"""Mongodb条件查询:
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
"""


class Mongo_db(object):

    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        # 连接mongodb数据库
        self.client = MongoClient(host=self.host, port=self.port)
        print('连接mongodb数据库成功！')

    @staticmethod
    def write_data(collection, expect_dict={}):
        """
        在指定的集合内写入指定的数据
        :param collection: 传入需要添加数据的集合名称
        :param expect_dict: 传入需要添加的字典
        :return:
        """
        print('在{}中添加{}'.format(collection, expect_dict))
        # collection.insert_many([expect_dict1, expect_dict2])  # 插入多行数据
        collection.insert_one(expect_dict)  # 插入一行数据
        print('添加数据结果：{}\n'.format(expect_dict))

    @staticmethod
    def get_data(collection, expect_dict={}):
        """
        获取集合内指定的数据
        :param collection: 传入需要查找的集合名称
        :param expect_dict: 传入需要查询的字典
        :return:
        """
        print('在{}中查询{}'.format(collection, expect_dict))
        # result = collection.find_one({'age': {'$lt': 20}})  # 返回结果小于20的数据
        # result = collection.find_one({'age': {'$regex': '2\d'}})  # 返回结果等于20~29的整形
        result = collection.find_one(expect_dict)  # 返回第一个匹配结果
        print('查询结果：{}\n'.format(result))

    @staticmethod
    def get_all_data(collection, expect_dict={}):
        """
        获取所有指定集合内的数据
        :param collection: 传入需要查找的集合名称
        :return:
        """
        print('开始查询{}所有数据:'.format(collection))
        if expect_dict:
            result = collection.find(expect_dict)  # 返回一个生成器（集合内所有的数据）
        else:
            result = collection.find()  # 返回一个生成器（集合内所有的数据）
        result_total = [i for i in result]
        print('查询结果：{}\n共查询到{}个数据\n'.format(result_total, len(result_total)))

    @staticmethod
    def update_data(collection, before_dict={}, after_dict={}):
        """
        更新指定的数据
        :param collection: 传入需要更新的集合名称
        :param before_dict: 传入更新前的字典
        :param after_dict: 传入更新后的字典格式
        :return:
        """
        print('在{}中把{}更新为{}'.format(collection, before_dict, after_dict))
        # result = collection.update_many(before_dict, after_dict)  # 更新所有匹配的数据
        result = collection.update_one(before_dict, after_dict)  # 更新一个数据
        print('共更新{}个数据\n'.format(result.matched_count))

    @staticmethod
    def delete_data(collection, expect_dict={}):
        """
        删除指定的数据
        :param collection: 传入需要删除值字典的集合名称
        :param expect_dict: 传入需要删除的字典
        :return:
        """
        print('在{}中删除{}:'.format(collection, expect_dict))
        # collection.remove(expect_dict)  # 删除一个数据（删除后的数据无法恢复）
        # collection.delete_many(expect_dict)  # 删除所有匹配的数据
        result = collection.delete_one(expect_dict)  # 删除一个数据
        print('共删除{}个数据\n'.format(result.deleted_count))

    @staticmethod
    def data_count(collection, expect_dict={}):
        """
        查询数据个数
        :param collection: 传入需要查询的集合名称
        :param expect_dict: 传入需要查询的字典
        :return:
        """
        print('在{}中查询{}个数：'.format(collection, expect_dict))
        result = collection.count_documents(expect_dict)
        print('共查询到{}个数据\n'.format(result))


if __name__ == '__main__':
    mongodb = Mongo_db()
    # 指定数据库
    db = mongodb.client.test
    # 指定集合
    collection = db.students
    # 写入数据
    test_data = {'age': 20}
    mongodb.write_data(collection, test_data)
    mongodb.get_data(collection, test_data)
    # 更新数据
    test_data = {'age': 20}
    update_data = {'age': 23}
    update_data_format = {"$inc": {'age': 3}}
    mongodb.update_data(collection, test_data, update_data_format)
    mongodb.get_data(collection, update_data)
    # 查询数据
    mongodb.data_count(collection, test_data)
    mongodb.data_count(collection, update_data)
    # 删除数据
    mongodb.get_all_data(collection, update_data)
    mongodb.delete_data(collection, update_data)
    mongodb.get_all_data(collection)
