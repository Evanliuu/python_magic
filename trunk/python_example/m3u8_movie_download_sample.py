import time
import requests
import datetime
import os
import threading
import urllib3
import random
from urllib.parse import urljoin


class Movie_download(object):

    def __init__(self, source_url=''):
        if 'm3u8' in source_url:
            base_url = source_url.split('/')
            base_url.pop()
            self.base_url = '/'.join(base_url)
        else:
            raise ValueError('url不是m3u8的格式，请检查url的正确性！')

        self.source_url = source_url
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
        headers = {'User-Agent': ua}
        return headers

    def download_movies(self, index=None, ts_url=None):
        ts_file_name = str(ts_url).split('/')[-1]
        try:
            print('{}, 正在下载第{}个TS >> {}'.format(datetime.datetime.now(), index, ts_url))
            resp = requests.get(url=ts_url, headers=self.random_headers(), stream=True, verify=False)
            # 保存TS数据流
            with open(ts_file_name, 'wb+') as file:
                file.write(resp.content)
            print('{}, 第{}个TS下载成功'.format(datetime.datetime.now(), index))
        except Exception as ex:
            self.failed_tx_url.append(ts_url)
            with open('failed_tx_url.txt', 'a+') as file:
                file.write(ts_url + '\n')
            print('{} 第{}下载失败, Error: {}'.format(datetime.datetime.now(), index, ex))

    def check_local_file(self):
        os.chdir(self.movie_local_path)
        if not os.path.isdir(urljoin(self.movie_local_path, self.movie_directory_name)):
            os.mkdir(self.movie_directory_name)
        os.chdir(urljoin(self.movie_local_path, self.movie_directory_name))

    def get_m3u8_movie(self):
        ts_list = []
        try:
            resp = requests.get(url=self.source_url, headers=self.random_headers())
            if resp.status_code == 200:
                # 从m3u8文件里面获取所有的TS文件（原视频数据分割为很多个TS流，每个TS流的地址记录在m3u8文件列表中）
                for line in resp.text.splitlines():
                    if '.ts' in line:
                        ts_list.append(urljoin(self.base_url, line))
        except Exception as ex:
            print('请求错误: {}'.format(ex))
            ts_list = None
        return ts_list

    @staticmethod
    def read_failed_txt_file():
        line = []
        with open('failed_tx_url.txt') as file:
            for each_line in file.readlines():
                line.append(each_line.strip())
        return line

    def merge_ts_file(self):
        os.chdir(urljoin(self.movie_local_path, self.movie_directory_name))
        cmd = "copy /b *.ts movie.mp4"
        os.system(cmd)
        # TODO 整合完mp4格式后后，ts文件不想留可删除
        # os.system('del /Q *.ts')

    def main(self):
        # 禁用安全请求警告(requests.get(url, verify=False))
        urllib3.disable_warnings()

        ts_list = self.get_m3u8_movie()
        if ts_list:
            # 检查保存路径
            self.check_local_file()

            # TODO 读取failed的txt文件重新下载
            # ts_list = self.read_failed_txt_file()

            print('总共获取到{}个ts文件, 等待下载...'.format(len(ts_list)))
            start_time = datetime.datetime.now()
            queue_index = 1
            while ts_list:
                queue = []
                try:
                    # 设置队列个数上限
                    queue_count = range(50)
                    for i in queue_count:
                        queue.append(ts_list.pop())
                except IndexError:
                    pass

                print('第{}个队列， 开始下载, 共计{}个'.format(queue_index, len(queue)))
                print('*' * 100)
                loops = range(len(queue))
                threads = []

                # 多线程爬取
                for index, ts_url in enumerate(queue):
                    t = threading.Thread(target=self.download_movies, args=(index + 1, ts_url))
                    threads.append(t)

                for i in loops:
                    threads[i].start()

                for i in loops:
                    threads[i].join()

                print('*' * 100)
                print('第{}个队列， 下载完成\n'.format(queue_index))
                queue_index += 1
                time.sleep(10)

            end_time = datetime.datetime.now()
            print('全部下载完毕： 累计{}分钟'.format((end_time - start_time).seconds / 60))

            if self.failed_tx_url:
                print('失败的ts文件: {}'.format(self.failed_tx_url))
                print('失败总数{}个'.format(len(self.failed_tx_url)))
            else:
                # 如果ts文件全部下载成功，则整合成一个mp4格式的电影文件（可手动下命令整合）
                self.merge_ts_file()
        else:
            print('没有发现任何ts文件, 请检查url的正确性！')


if __name__ == '__main__':
    source_url = 'https://xxx.xxx.tv/xxxxxx/index.m3u8'
    movie_download = Movie_download(source_url=source_url)
    movie_download.main()
