from redis import StrictRedis


# 打开cmd输入 redis-cli.exe 即可进入redis命令行

class Redis_DB(object):

    def __init__(self, host='localhost', port=6666):
        self.host = host
        self.port = port
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
