from redis import StrictRedis

# 打开cmd输入 redis-cli.exe 即可进入redis命令行

"""键值相关命令：
1. keys *                   取出当前所有的key
2. exists name              查看数据库是否有name这个key
3. del name                 删除key name
4. expire confirm 100       设置confirm这个key100秒过期
5. ttl confirm              获取confirm 这个key的有效时长
6. select 0                 选择到0数据库 redis默认的数据库是0~15一共16个数据库
7. move confirm 1           将当前数据库中的key移动到其他的数据库中，这里就是把confire这个key从当前数据库中移动到1中
8. persist confirm          移除confirm这个key的过期时间
9. randomkey                随机返回数据库里面的一个key
10. rename key2 key3        重命名key2 为key3
11. type key2               返回key的数据类型
"""

"""服务器相关命令:
1. ping                     PING返回响应是否连接成功
2. echo                     在命令行打印一些内容
3. select                   0~15 编号的数据库
4. quit                    /exit 退出客户端
5. dbsize                   返回当前数据库中所有key的数量
6. info                     返回redis的相关信息
7. config get dir/*         实时传储收到的请求
8. flushdb                  删除当前选择数据库中的所有key
9. flushall                 删除所有数据库中的数据库
"""


class Redis_DB(object):

    def __init__(self, host='localhost', port=6379):
        self.host = host
        self.port = port
        # 连接本地redis数据库
        self.redis = StrictRedis(host=self.host, port=self.port, db=0, password='')

    def write_data(self, key, value):
        self.redis.set(key, value)

    def get_data(self, key):
        value = self.redis.get(key)
        return value

    def get_all_data(self):
        all_keys = []
        if self.redis.keys():
            for i in self.redis.keys():
                key = i.decode('ascii')
                value = self.get_data(i).decode('ascii')
                all_keys.append({key: value})
        else:
            all_keys = None
        print('find total items:\n{}'.format(all_keys))
        return all_keys

    def delete_data(self, key):
        self.redis.delete(key)
        print('delete the key: {}'.format(key))


if __name__ == '__main__':
    redis_db = Redis_DB()
    redis_db.write_data('name', 'evan')
    print('*' * 50)
    redis_db.get_all_data()
    print('*' * 50)
    redis_db.delete_data('name')
    print('*' * 50)
    redis_db.get_all_data()
    print('*' * 50)
