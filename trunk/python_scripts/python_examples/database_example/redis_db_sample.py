"""
Redis数据类型:
1. <set key value>
    类型	:   String(字符串)	
    简介:   二进制安全	
    特性	:   可以包含任何数据,比如jpg图片或者序列化的对象,一个键最大能存储512M
    场景:   /

2. <hset major_key key value>
    类型	:   Hash(字典)
    简介:   键值对集合,即编程语言中的Map类型
    特性	:   适合存储对象,并且可以像数据库中update一个属性一样只修改某一项属性值(Memcached中需要取出整个字符串反序列化成对象修改完再序列化存回去)
    场景:   存储、读取、修改用户属性

3. <头部：lpush key value1 value2 ... 末尾：rpush key value1 value2 ...> 可添加一个或多个值
    类型	:   List(列表)
    简介:   链表(双向链表)
    特性	:   增删快,提供了操作某一段元素的API
    场景:   1.最新消息排行等功能(比如朋友圈的时间线) 2.消息队列

4. <sadd key member1 member2 ...> 可添加一个或多个值
    类型	:   Set(集合)
    简介:   哈希表实现,元素不重复
    特性	:   1.添加、删除,查找的复杂度都是O(1) 2.为集合提供了求交集、并集、差集等操作
    场景:   1.共同好友 2.利用唯一性,统计访问网站的所有独立ip 3,好用推荐时,根据tag求交集,大于某个阈值就可以推荐

5. <zadd key score1 member1 score2 member2 ...> 可添加一个或多个值
    类型	:   Sorted Set(有序集合)
    简介:   将Set中的元素增加一个权重参数score,元素按score有序排列
    特性	:   数据插入集合时,已经进行天然排序
    场景:   	1.排行榜 2.带权重的消息队列

键值相关命令：
1.  keys *                   查看当前所有的key
2.  exists name              查看数据库是否有name这个key
3.  del name                 删除key name
4.  expire confirm 100       设置confirm这个key100秒过期
5.  ttl confirm              获取confirm 这个key的有效时长
6.  select 0                 选择到0数据库 redis默认的数据库是0~15一共16个数据库
7.  move confirm 1           将当前数据库中的key移动到其他的数据库中，这里就是把confire这个key从当前数据库中移动到1中
8.  persist confirm          移除confirm这个key的过期时间
9.  randomkey                随机返回数据库里面的一个key
10. rename key2 key3         重命名key2 为key3
11. type key2                返回key的数据类型

服务器相关命令:
1.  ping                     PING返回响应是否连接成功
2.  echo                     在命令行打印一些内容
3.  select                   0~15 编号的数据库
4.  quit                    /exit 退出客户端
5.  dbsize                   返回当前数据库中所有key的数量
6.  info                     返回redis的相关信息
7.  config get dir/*         实时传储收到的请求
8.  flushdb                  删除当前选择数据库中的所有key
9.  flushall                 删除所有数据库中的数据库
"""

# -*- coding: utf-8 -*-
from redis import StrictRedis

# 打开cmd输入 redis-cli.exe 即可进入redis命令行


class RedisHandle(object):

    def __init__(self, host='localhost', port=6379):
        self.host = host
        self.port = port
        # 连接redis数据库
        self.client = StrictRedis(host=self.host, port=self.port, db=0, password='')
        print('连接redis数据库成功！')

    def write_data(self, key, value):
        self.client.set(key, value)

    def get_data(self, key):
        value = self.client.get(key)
        return value

    def get_all_data(self):
        all_keys = []
        if self.client.keys():
            for i in self.client.keys():
                key = i.decode('ascii')
                value = self.get_data(i).decode('ascii')
                all_keys.append({key: value})
        else:
            all_keys = None
        print('find total items:\n{}'.format(all_keys))
        return all_keys

    def delete_data(self, key):
        self.client.delete(key)
        print('delete the key: {}'.format(key))


if __name__ == '__main__':
    redisDb = RedisHandle()
    redisDb.write_data('name', 'evan')
    redisDb.get_all_data()
    redisDb.delete_data('name')
    redisDb.get_all_data()
