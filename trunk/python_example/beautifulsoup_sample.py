from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="boy" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="child" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


def parse_html():
    soup = BeautifulSoup(html_doc, 'lxml')
    # soup.prettify()  # 补全HTML代码
    # print(soup.p)   # 获取标签信息
    # print(soup.p.name)  # 获取标签名称
    # print(soup.p.string)  # 获取标签文本
    # print(soup.text)  # 获取所有文本信息
    # print(soup.p['class'])  # 获取标签内class属性值

    # 使用re.compile('Lacie')为in的匹配关系，不使用Regex则是完全匹配，如：text='Lacie'
    print(soup.find_all('a', text=re.compile('Lacie'), limit=1))  # 根据文本定位 (limit: 限制匹配个数)
    print(soup.find_all('a', id='link2'))  # 根据id定位
    print(soup.find_all('a', class_='boy'))  # 根据class定位
    print(soup.find_all(name='a'))  # 根据标签定位
    print(soup.find_all(attrs={'class': 'boy'}))  # 根据属性定位


if __name__ == '__main__':
    parse_html()
