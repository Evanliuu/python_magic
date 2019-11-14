import re
from bs4 import BeautifulSoup

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


def parse():
    # 初始化对象
    soup = BeautifulSoup(html_doc, 'lxml')
    # soup = BeautifulSoup(open('example.html'), 'lxml')

    # 补全HTML代码
    soup.prettify()
    # 获取标签名称
    print(soup.p)  # 获取整条p标签
    print(soup.p.name)  # 获取p标签名称
    # 获取标签属性
    print(soup.p.attrs)  # 获取p标签内的所有属性
    print(soup.p['class'])  # 获取p标签内的class属性值
    # 获取标签文本
    print(soup.p.string)  # 获取p标签的文本信息，如果p标签内包含了多个子节点并有多个文本时返回None
    print(soup.p.strings)  # 获取p标签内的所有文本信息，返回一个生成器
    print(soup.p.text)  # 获取p标签内的所有文本信息，返回一个列表
    print(soup.stripped_strings)  # 去掉空白，保留所有的文本，返回一个生成器

    # 获取父子节点
    print(soup.p.parent)  # 获取p标签的父节点
    print(soup.p.parents)  # 获取p标签的所有父节点，返回一个生成器
    print(soup.p.contents)  # 获取p标签内的所有子节点，返回一个列表
    print(soup.p.children)  # 获取p标签内的所有子节点，返回一个生成器
    # 获取子孙节点
    print(soup.p.descendants)  # 获取p标签内的所有子孙节点，返回一个生成器
    # 获取兄弟节点
    print(soup.a.previous_sibling)  # 获取a标签的上一个兄弟节点
    print(soup.a.previous_siblings)  # 获取a标签的上一个兄弟节点，返回一个生成器
    print(soup.a.next_sibling)  # 获取a标签的下一个兄弟节点
    print(soup.a.next_siblings)  # 获取a标签的下一个兄弟节点，返回一个生成器

    # 使用re.compile('Lacie')为in的匹配关系，不使用Regex则是完全匹配，如：text='Lacie'
    print(soup.find_all('a', text=re.compile('Lacie'), limit=1))  # 根据文本定位 (limit: 限制匹配个数)
    print(soup.find_all('a', id='link2'))  # 根据id定位
    print(soup.find_all('a', class_='boy'))  # 根据class定位
    print(soup.find_all(name='a'))  # 根据标签定位
    print(soup.find_all(attrs={'class': 'boy'}))  # 根据属性定位


if __name__ == '__main__':
    parse()
