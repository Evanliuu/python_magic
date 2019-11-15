import re
from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list two" id="list-2">
<li class="element">evan</li>
<li class="element">jane</li>
<li class="element">summer</li>
</ul>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="child" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="parent" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">End...</p>
</body>
</html>
"""


def parse():
    # 初始化对象
    soup = BeautifulSoup(html_doc, 'lxml')  # html文本初始化
    # soup = BeautifulSoup(open('example.html'), 'lxml')  # html文件初始化

    # 补全HTML代码
    print(soup.prettify())

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

    # 获取父·子节点
    print(soup.p.parent)  # 获取p标签的直接父节点
    print(soup.p.parents)  # 获取p标签的所有父节点，返回一个生成器
    print(soup.p.contents)  # 获取p标签内的所有直接子节点，返回一个列表
    print(soup.p.children)  # 获取p标签内的所有直接子节点，返回一个生成器
    # 获取子孙节点
    print(soup.p.descendants)  # 获取p标签内的所有子孙节点，返回一个生成器
    # 获取兄弟节点
    print(soup.a.previous_sibling)  # 获取a标签的上一个兄弟节点
    print(soup.a.previous_siblings)  # 获取a标签前面的所有兄弟节点，返回一个生成器
    print(soup.a.next_sibling)  # 获取a标签的下一个兄弟节点
    print(soup.a.next_siblings)  # 获取a标签后面的所有兄弟节点，返回一个生成器

    # TODO 方法选择器：find() 和 find_all() 使用方法完全相同，前者返回匹配到的第一个结果，后者返回一个包含所有匹配结果的列表
    print(soup.find_all(text=re.compile('Lacie'), limit=2))  # 使用正则获取文本包含'Lacie'的节点（limit: 限制匹配个数）
    print(soup.find_all('a', text='Lacie'))  # 获取a标签内文本等于'Lacie'的节点（完整匹配）
    print(soup.find_all('a', id='link2'))  # 获取a标签内id等于'link2'的节点
    print(soup.find_all('a', class_='sister'))  # 获取a标签内class等于'sister'的节点
    print(soup.find_all(name='a'))  # 获取整条a标签信息
    print(soup.find_all(attrs={'class': 'sister'}))  # 获取属性值class为'sister'的节点
    # TODO CSS选择器：#代表id .代表class
    print(soup.select('ul'))  # 获取所有ul标签，返回一个列表
    print(soup.select('ul li'))  # 获取所有ul标签内的li节点，返回一个列表
    print(soup.select('ul.list'))  # 获取ul标签内class为'list'的所有元素，返回一个列表
    print(soup.select('.list'))  # 获取class为'list'的所有元素，返回一个列表
    print(soup.select('.list.two'))  # 获取class为'list two'的所有元素，返回一个列表
    print(soup.select('#list-1 .element'))  # 获取id为'list-1'内class为'element'的所有元素，返回一个列表


if __name__ == '__main__':
    parse()
