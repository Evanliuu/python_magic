# -*- coding:utf-8 -*-
import requests


# r = requests.get(url='http://httpbin.org/get')  # 使用GET请求访问
# print(r.text)  # 打印网页的HTML文本

data = {
    'name': 'Evan',
    'age': '24'
}

# 请求头参数
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/78.0.3904.108 Safari/537.36'
}

# 第一次访问，并设置cookies
r1 = requests.get(url='http://httpbin.org/cookies/set/number/123456789')
print('r1: {}'.format(r1.text))
# 第二次访问
r2 = requests.get(url='http://httpbin.org/cookies')
print('r2: {}'.format(r2.text))
