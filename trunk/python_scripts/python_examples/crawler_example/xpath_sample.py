"""<<常用表达式规则>>
表达式:          含义:
nodename        选择此节点的所有子节点
/               从当前节点选取直接子节点
//              从当前节点选取子孙节点
.               选取当前节点
..              选取当前节点的父节点
@               选取属性
*               选取所有信息

<<多属性匹配运算符介绍>>
运算符:          描述:                   示例:
and             与                      age=19 or age=20
or              或                      age>19 and age<21
mod             计算除法的余数           5 mod 7
|               计算两个节点集           //book | //cd
+               加法                    6 + 4
-               减法                    6 - 4
*               乘法                    6 * 4
div             除法                    8 div 4
=               等于                    age=19
!=              不等于                  age!=19
<               小于                    age<19
<=              小于等于                age<=19
>               大于                    age>19
>=              大于等于                age>=19
"""
# -*- coding:utf-8 -*-
from lxml import etree

html_doc = """
<html>
<head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<ul class="list" id="list-1">
<li class="element"><a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list two" id="list-2">
<li class="element"><a href="http://example.com/tillie" class="parent" id="link3">Tillie</a>evan</li>
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
    html = etree.HTML(html_doc)  # html文本初始化
    # html = etree.parse('./example.html', etree.HTMLParser())  # html文件初始化

    # 补全HTML代码
    print(etree.tostring(html).decode('utf-8'))

    # 文本获取
    print(html.xpath('//a[@class="parent"]/text()'))  # 获取所有a节点内class等于'parent'的文本，返回一个列表
    # 属性获取
    print(html.xpath('//ul/@class'))  # 获取所有ul节点内的class值，返回一个列表
    print(html.xpath('//ul/attribute::*'))  # 获取所有ul节点内的所有属性值，返回一个列表
    # 属性匹配
    print(html.xpath('//ul[@class="list"]'))  # 获取所有class等于'list'的ul节点，返回一个列表
    # 属性多值匹配
    print(html.xpath('//ul[contains(@class, "two")]'))  # 获取所有class包含'two'的ul节点，返回一个列表
    # 多属性匹配
    print(html.xpath('//ul[contains(@class, "two") and @id="list-2"]'))  # 满足上面的情况再加上id等于'list-2'，返回一个列表

    # 获取所有节点
    print(html.xpath('//*'))  # 获取所有节点，返回一个列表
    print(html.xpath('//li'))  # 获取所有的li节点，返回一个列表
    # 获取父·祖先节点
    print(html.xpath('//li/parent::*'))  # 获取所有li节点的直接父节点，返回一个列表
    print(html.xpath('//li/..'))  # 用法同上
    print(html.xpath('//li/ancestor::*'))  # 获取所有li节点的祖先节点，返回一个列表
    print(html.xpath('//li/ancestor::ul'))  # 获取所有li节点的ul祖先节点，返回一个列表
    # 获取子·子孙节点
    print(html.xpath('//ul/child::*'))  # 获取所有ul节点内的直接子节点，返回一个列表
    print(html.xpath('//ul/child::li'))  # 获取所有ul节点内的li直接子节点，返回一个列表
    print(html.xpath('//ul/li'))  # 用法同上
    print(html.xpath('//ul/descendant::*'))  # 获取所有ul节点内的子孙节点，返回一个列表
    print(html.xpath('//ul/descendant::a'))  # 获取所有ul节点内的a子孙节点，返回一个列表
    print(html.xpath('//ul//a'))  # 用法同上
    # 获取兄弟·后续节点
    print(html.xpath('//li[1]/following-sibling::*'))  # 获取所有li[1]节点之后的兄弟节点，返回一个列表
    print(html.xpath('//li[1]/following::*'))  # 获取所有li[1]节点的后续节点，返回一个列表
    print(html.xpath('//li[1]/following::*[2]'))  # 获取所有li[1]节点后的第二个节点，返回一个列表

    # 按序选择（正序位置是从1开始，last()-2 代表倒数第三个位置，因为last()是最后一个）
    print(html.xpath('//ul/li[1]'))  # 获取所有ul节点内的第一个li节点，返回一个列表
    print(html.xpath('//ul/li[last()]'))  # 获取所有ul节点内的最后一个li节点，返回一个列表
    print(html.xpath('//ul/li[last()-2]'))  # 获取所有ul节点内的倒数第三个li节点，返回一个列表
    print(html.xpath('//ul/li[position()<3]'))  # 获取所有ul节点内位置小于3的li节点，返回一个列表


if __name__ == '__main__':
    parse()
