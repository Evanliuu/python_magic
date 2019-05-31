# -*- coding: UTF-8 -*-
import requests
from urllib.parse import urljoin
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
        android_ua = 'Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
        chrome_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'

        headers = {
            "User-Agent": chrome_ua,
            'Host': 'www.623zz.com'
        }
        params = {
            'm': 'vod-search-wd-{}'.format(self.like_movie)
        }
        return headers, params

    def get_web_page(self, url=None, purpose=GET, headers=None, params=None):
        url = url or self.source_url
        headers = headers or self.parameter()[0]

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
    def search_total_movie(html):
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

    @staticmethod
    def search_download_url(html):
        soup = BeautifulSoup(html, 'lxml')
        lines = soup.find('p', class_='player_list')
        tag = lines.find('a')
        url = tag['href']
        return url

    def login_movie_page(self):
        params = self.parameter()[1]
        resp = self.get_web_page(purpose=GET, params=params)
        return resp

    def main(self):
        # 登录到电影网站
        resp = self.login_movie_page()
        if resp:
            # 获取指定电影类型的总数量
            total_url = self.search_total_movie(resp.text)
            if total_url:
                # 选择需要的电影名称
                like_url = total_url[0]
                movie_url = urljoin(self.base_url, like_url)
                resp = self.get_web_page(url=movie_url, purpose=GET)
                if resp:
                    # 获取电影的最终链接
                    download_url = self.search_download_url(resp.text)
                    if download_url:
                        download_url = urljoin(self.base_url, download_url)
                        resp = self.get_web_page(url=download_url, purpose=GET)
                        print(resp.text)


if __name__ == '__main__':
    # TODO 选择你喜欢的电影
    base_url = 'https://www.com/'
    like_movie = '忍者神龟'

    crawler = Crawler(base_url=base_url, like_movie=like_movie)
    crawler.main()
