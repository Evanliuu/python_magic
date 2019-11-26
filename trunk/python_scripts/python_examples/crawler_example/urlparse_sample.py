# -*- coding:utf-8 -*-
from urllib.parse import urlparse
from urllib.parse import urljoin
from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote


# urlparse --> 返回一个ParseResult类型的对象，包含六个部分（scheme netloc path params query fragment）
print(urlparse('http://www.baidu.com/index.html;user?id=5#comment'))


# urljoin -- > 合并两个字符串组合成一个完整的URL
print(urljoin('http://www.baidu.com', 'index.html'))


params = {
    'name': 'Evan',
    'age': '20'
}
print('http://www.baidu.com?' + urlencode(params))  # urlencode --> 将字典序列化为Get请求参数
print(parse_qs('http://www.baidu.com?name=Evan&age=20'))  # parse_qs --> 将Get请求参数反序列化为字典
print(parse_qsl('http://www.baidu.com?name=Evan&age=20'))  # parse_qsl --> 将Get请求参数反序列化为列表


print('http://www.baidu.com?' + quote('年龄'))  # quote --> 将中文转化为URL编码
print(unquote('http://www.baidu.com?%E5%B9%B4%E9%BE%84'))  # unquote --> 将URL编码转化为中文
