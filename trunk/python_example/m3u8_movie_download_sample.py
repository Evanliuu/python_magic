import requests
import datetime
import os
from urllib.parse import urljoin


class Crawler(object):

    def __init__(self, base_url=None):
        self.base_url = base_url
        self.source_url = urljoin(self.base_url, 'playlist.m3u8')
        self.ts_list = []
        self.base_path = r'C:\Users\86151\Desktop\m3u8_movies'

    def record_movies(self):
        os.chdir(self.base_path)
        if not os.path.isdir(urljoin(self.base_path, 'movie_1')):
            os.mkdir('movie_1')
        os.chdir(urljoin(self.base_path, 'movie_1'))

        for index, ts_url in enumerate(self.ts_list):
            ts_file_name = str(ts_url).split('/')[-1]
            try:
                print('{}, 正在下载第{}个TS >> {}'.format(datetime.datetime.now(), index + 1, ts_url))
                resp = requests.get(ts_url, stream=True, verify=False)
                # 保存TS数据流
                with open(ts_file_name, 'wb') as file:
                    for chunk in resp.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                print('{}, 第{}个TS下载成功'.format(datetime.datetime.now(), index + 1))
            except Exception as ex:
                print('{} 第{}下载失败, Error: {}'.format(datetime.datetime.now(), index + 1, ex))

    def get_m3u8_movie(self):
        # 获取m3u8格式的电影文件
        resp = requests.get(self.source_url)
        # 从m3u8文件里面获取所有的TS文件（原视频数据分割为很多个TS流，每个TS流的地址记录在m3u8文件列表中）
        for line in resp.text.splitlines():
            if '.ts' in line:
                self.ts_list.append(urljoin(self.base_url, line))

    def main(self):
        self.get_m3u8_movie()
        if self.ts_list:
            self.record_movies()


if __name__ == '__main__':
    base_url = 'https://156zy.suyunbo.tv/2019/05/30/M4dY96iXziI1DgqH/'
    crawler = Crawler(base_url=base_url)
    crawler.main()
