# -*- coding: UTF-8 -*-
import re
import requests
from urllib.parse import urljoin, quote
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

GET = 'get'
POST = 'post'


class Crawler(object):

    def __init__(self, base_url=None, like_movie=None):
        self.base_url = base_url
        self.source_url = urljoin(self.base_url, '/index.php')
        self.session = requests.Session()
        self.like_movie = like_movie

    def parameter(self):
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            'Host': 'www.623zz.com'
        }
        params = {
            'm': 'vod-search-wd-{}'.format(self.like_movie)
        }
        return headers, params

    def get_web_page(self, url=None, purpose=GET, headers=None, params=None):
        url = url or self.source_url
        headers = headers or self.parameter()[0]
        params = params or self.parameter()[1]

        try:
            if purpose == GET:
                response = self.session.get(url, headers=headers, params=params, timeout=60)
            else:
                response = self.session.post(url, headers=headers, data=params, timeout=60)

            if response.status_code == 200:
                return response
            else:
                return None

        except Exception as ex:
            print('Get the url ({}) error, error msg: {}'.format(url, ex))
            return None

    @staticmethod
    def parse_url(html):
        final_ufl = []
        soup = BeautifulSoup(html, 'lxml')
        lines = soup.find_all('a', class_='module_play_img')
        for line in lines:
            url = line['href']
            final_ufl.append(url)

        if final_ufl:
            return final_ufl
        else:
            return None

    def main(self):
        html = self.get_web_page(purpose=GET)
        if html:
            total_url = self.parse_url(html.text)
            if total_url:
                like_url = total_url[0]
                print(like_url)
                download_url = urljoin(self.base_url, like_url)
                print(download_url)


if __name__ == '__main__':
    base_url = 'https://www.623zz.com/'
    like_movie = '鬼父'

    crawler = Crawler(base_url=base_url, like_movie=like_movie)
    crawler.main()
