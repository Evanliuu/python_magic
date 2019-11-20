# -*- coding:utf-8 -*-
import random
import requests

from bs4 import BeautifulSoup


class Crawler(object):

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

    def main(self):
        resp = requests.get(self.source_url, headers={'User-Agent': self.random_user_agent()})
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'lxml')
            print(soup)
        else:
            print('No data found!')
            print('url: {}'.format(resp.url))
            print('history: {}'.format(resp.history))


if __name__ == '__main__':
    crawler = Crawler(url='https://zhuanlan.zhihu.com/p/88209825')
    crawler.main()
