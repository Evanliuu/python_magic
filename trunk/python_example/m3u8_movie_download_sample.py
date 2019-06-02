import requests
import datetime
import os
import threading
import urllib3
import random
from urllib.parse import urljoin


class Crawler(object):

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.source_url = urljoin(self.base_url, 'playlist.m3u8')
        self.movie_local_path = r'C:\Users\86151\Desktop\m3u8_movies'
        self.movie_directory_name = 'movie_1'
        self.failed_tx_url = []

    @staticmethod
    def random_headers():
        ua_list = [
            # Chrome UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36',
            # IE UA
            'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            # Microsoft Edge UA
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763'
        ]
        ua = random.choice(ua_list)
        headers = {
            'User-Agent': ua,
        }
        return headers

    def download_movies(self, index=None, ts_url=None):
        ts_file_name = str(ts_url).split('/')[-1]
        try:
            print('{}, 正在下载第{}个TS >> {}'.format(datetime.datetime.now(), index + 1, ts_url))
            resp = requests.get(url=ts_url, headers=self.random_headers(), stream=True, verify=False)
            # 保存TS数据流
            with open(ts_file_name, 'wb+') as file:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print('{}, 第{}个TS下载成功'.format(datetime.datetime.now(), index + 1))
        except Exception as ex:
            self.failed_tx_url.append(ts_url)
            with open('failed_tx_url.txt', 'a+') as file:
                file.write(ts_url + '\n')
            print('{} 第{}下载失败, Error: {}'.format(datetime.datetime.now(), index + 1, ex))

    def check_local_file(self):
        os.chdir(self.movie_local_path)
        if not os.path.isdir(urljoin(self.movie_local_path, self.movie_directory_name)):
            os.mkdir(self.movie_directory_name)
        os.chdir(urljoin(self.movie_local_path, self.movie_directory_name))

    def get_m3u8_movie(self):
        # 获取m3u8格式的电影文件
        resp = requests.get(url=self.source_url, headers=self.random_headers())

        ts_list = []
        if resp.status_code == 200:
            # 从m3u8文件里面获取所有的TS文件（原视频数据分割为很多个TS流，每个TS流的地址记录在m3u8文件列表中）
            for line in resp.text.splitlines():
                if '.ts' in line:
                    ts_list.append(urljoin(self.base_url, line))
        return ts_list

    def main(self):
        # 禁用安全请求警告(requests.get(url, verify=False))
        urllib3.disable_warnings()

        ts_list = self.get_m3u8_movie()
        if ts_list:
            self.check_local_file()

            start_time = datetime.datetime.now()
            loops = range(len(ts_list))
            threads = []

            for index, ts_url in enumerate(ts_list):
                t = threading.Thread(target=self.download_movies, args=(index + 1, ts_url))
                threads.append(t)

            for i in loops:
                threads[i].start()

            for i in loops:
                threads[i].join()

            end_time = datetime.datetime.now()
            print('全部下载完毕： 累计{}分钟'.format((end_time - start_time).seconds / 60))
            if self.failed_tx_url:
                print('Failed TX url: {}'.format(self.failed_tx_url))
                print('Length: {}'.format(len(self.failed_tx_url)))


if __name__ == '__main__':
    base_url = 'https://156zy.suyunbo.tv/2019/05/30/M4dY96iXziI1DgqH/'
    crawler = Crawler(base_url=base_url)
    crawler.main()
