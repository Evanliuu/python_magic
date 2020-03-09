"""常用的匹配规则:
模式:              描述:
\w                匹配字母，数字及下划线
\W                匹配不是字母，数字及下划线的字符
\s                匹配任意空白字符
\S                匹配任意非空字符
\d                匹配任意数字
\D                匹配任意非数字的字符
\z                匹配字符串结尾，如果存在换行，同时还会匹配到换行符
\Z                匹配字符串结尾，如果存在换行，只匹配到换行前的结束字符串
\G                匹配最后完成匹配的位置
\n                匹配一个换行符
\t                匹配一个制表符
^                 匹配一行字符串的开头
$                 匹配一行字符串的结尾
.                 匹配任意字符，除了换行符
[...]             用来表示一组字符，单独列出，比如[abc]: 匹配 A、b或c 的字符
[^...]            匹配不在[]中的字符，比如[abc]: 匹配除了 A、b或c 之外的字符
*                 匹配0个或多个前面的表达式
+                 匹配1个或多个前面的表达式
？                匹配0个或1个前面的表达式，非贪婪方式
{n}               精确匹配n个前面的表达式
{n, m}            匹配n到m次前面的表达式，贪婪方式
a|b               匹配a或b
()                匹配括号内的表达式，也表示一个组

<<修饰符>>
模式:              描述:
re.S              使.匹配包括换行在内的所有字符
re.I              使匹配对大小写不敏感
re.M              多行匹配，影响^和$
re.L              做本地化识别（locale-aware）匹配
re.U              根据Unicode字符集解析字符，则个标志影响\w，\W，\b，\B
re.X              该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
"""
# -*- coding:utf-8 -*-
import re

__author__ = 'Evan'
example = """Just as you need air to breathe,
you need opportunity to succeed. It takes more than just breathing in the fresh air of opportunity,
however. You must make use of that opportunity. That's not up to the opportunity. That's up to you.
It doesn't matter what "floor" the opportunity is on. What matters is what you do with it.
"""


def parse():
    # 匹配方式
    print(re.match('Just as you need air to breathe', example).group())  # 起始位置匹配
    print(re.search("That's up to you", example).group())  # 任意位置匹配
    print(re.findall("is", example))  # 匹配所有指定内容，返回一个列表

    # 分组匹配
    result = re.search(r'You (.+?)\..+?What (.+?)\.', example, re.S)
    if result:
        print(result.group())  # 返回所有的匹配结果
        print(result.group(1))  # 返回第一个圆括号的匹配结果
        print(result.group(2))  # 返回第二个圆括号的匹配结果
        print(result.groups())  # 返回一个列表，包含所有圆括号的结果

    # 输出匹配的范围
    print(re.match('Just as you need air to breathe', example).span())  # 返回一个元组

    # 替换字符串
    print(re.sub('what', 'happy', example))  # 把所有的'what'替换成'happy'

    # 编译正则表达式，可重复使用
    pattern = re.compile('succeed')
    print(re.findall(pattern, example))

    # 匹配中文
    text = 'abc我爱你def中国'
    pattern = '[\u4E00-\u9FA5]+'  # 匹配所有的中文
    print(re.findall(pattern, text))

    # 只匹配字符串中的中文，字母，数字
    print(re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', text))


if __name__ == '__main__':
    parse()
