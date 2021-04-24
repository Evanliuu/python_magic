# -*- coding:utf-8 -*-
import html
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote

__author__ = 'Evan'


print('返回一个ParseResult类型的对象: ', urlparse('http://www.baidu.com/index.html;user?id=5#comment'))
print('合并两个字符串组合成一个完整的URL: ', urljoin('http://www.baidu.com', 'index.html'))

params = {
    'name': 'Evan',
    'id': '77'
}
print('将字典序列化为Get请求参数: ', 'http://www.baidu.com?' + urlencode(params))

print('将Get请求参数反序列化为字典: ', parse_qs('http://www.baidu.com?name=Evan&id=77'))
print('将Get请求参数反序列化为列表: ', parse_qsl('http://www.baidu.com?name=Evan&id=77'))

print('将中文转化为URL编码: ', 'http://www.baidu.com?' + quote('年龄'))
print('将URL编码转化为中文: ', unquote('http://www.baidu.com?%E5%B9%B4%E9%BE%84'))

print('字符转义成HTML格式: ', html.escape('https://127.0.0.1/report'))
print('HTML格式反转义成字符: ', html.unescape('https&#x3a;&#x2f;&#x2f;127.0.0.1&#x2f;report'))
