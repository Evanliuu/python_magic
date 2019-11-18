# -*- coding:utf-8 -*-
import random
import requests


class Crawler(object):

    def __init__(self, url=''):
        self.source_url = url
        self.session = requests.Session()  # Session初始化

    @staticmethod
    def random_headers():
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
        # files = {'file': open('favicon.ico', 'rb')}  # 上传的文件
        data = {'wd': 'python'}  # Post请求参数
        params = {'wd': 'python'}  # Get请求参数
        headers = {"User-Agent": self.random_headers()}  # 请求头参数

        # 访问页面
        # self.session.get(self.source_url, headers=headers, params=params)  # 使用Session保持会话
        # requests.post(self.source_url, headers=headers, files=files)  # 文件上传
        # requests.post(self.source_url, headers=headers, data=data)  # Post请求
        response = requests.get(self.source_url, headers=headers, params=params)  # Get请求

        # 获取网页信息
        print(response.url)  # 获取当前URL，返回一个字符串
        print(response.status_code)  # 获取响应状态码，返回一个整形
        print(response.headers)  # 获取头部信息，返回一个字典
        print(response.history)  # 获取访问的历史记录，可以查看是否重定向，返回一个列表
        print(response.cookies)  # 获取网页Cookies，返回一个字典
        print(response.content)  # 获取二进制格式，返回一个二进制数据
        print(response.text)  # 获取网页源代码，返回一个字符串
        # print(response.json())  # 如果响应信息是JSON格式则调用此方法，返回一个字典

        # 关闭网页重定向
        requests.get(self.source_url, allow_redirects=False)
        # 超时设置
        requests.get(self.source_url, timeout=60)
        # 取消SSL证书验证
        requests.get(self.source_url, verify=False)
        # 身份认证（打开网页需要身份验证时调用此方法）
        requests.get('http://localhost:5000', auth=('username', 'password'))

        # TODO 使用代理（需要提供有效的代理IP，使用SOCKS协议需要安装 'requests[socks] 外部库'）
        # proxies = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}  # 使用普通格式
        # proxies = {"http": "http://user:password@10.10.1.10:3128"}  # 使用HTTP Basic Auth格式
        # proxies = {"http": "socks5://user:password@host:port", "https": "socks5://user:password@host:port"}  # SOCKS
        # requests.get(self.source_url, proxies=proxies)


if __name__ == '__main__':
    crawler = Crawler(url='https://www.baidu.com')
    crawler.main()
