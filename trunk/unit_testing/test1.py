# -*- coding:utf-8 -*-
import requests


def request_url(url):
    response = requests.get(url='https://www.baidu.com/s?ie=UTF-8&wd=python')  # 用GET请求访问百度首页
    print(response.text)  # 打印百度首页的HTML文本

    # 请求头参数
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36'
    }
    params = {
        'ie': 'UTF-8',
        'wd': 'python'
    }
    response = requests.get(url=url, headers=headers, params=params)  # Get请求
    print(response.text)


if __name__ == '__main__':
    request_url(url='https://www.baidu.com/')
