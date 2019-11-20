# -*- coding:utf-8 -*-
import random
import requests
from pymongo import MongoClient

from bs4 import BeautifulSoup


class Crawler(object):
    database = None
    collection = None

    def __init__(self, url=''):
        self.source_url = url
        self.session = requests.Session()

    @staticmethod
    def random_user_agent():
        ua_list = [
            # Chrome UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/73.0.3683.75 Safari/537.36',
            # IE UA
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            # Microsoft Edge UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
            ' Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        ]
        ua = random.choice(ua_list)
        return ua

    def login_mongodb(self, database_name, collection_name):
        """
        连接Mongodb客户端
        :param database_name: 数据库名称
        :param collection_name: 集合名称
        :return:
        """
        client = MongoClient(host='localhost', port=27017)
        self.database = client[database_name]
        self.collection = self.database[collection_name]
        print('Login mongodb successfully, database_name="{}", collection_name="{}"'.format(database_name,
                                                                                            collection_name))

    def main(self):
        resp = requests.get(self.source_url, headers={'User-Agent': self.random_user_agent()})
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            p = soup.select('p')

            self.login_mongodb(database_name='ZhiHu', collection_name='Feynman learning method')
            for i, r in enumerate(p):
                if not r.text:
                    continue
                write_info = {'{}'.format(i): r.text}
                self.collection.insert_one(write_info)
                print('Write {} ok'.format(write_info))

        else:
            print('No data found!')
            print('url: {}'.format(resp.url))
            print('history: {}'.format(resp.history))


if __name__ == '__main__':
    crawler = Crawler(url='https://zhuanlan.zhihu.com/p/88209825')
    crawler.main()
