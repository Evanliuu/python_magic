from lxml import etree

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
    html = etree.HTML(html_doc)
    html.prettify()
    print(html.xpath('//a/[@class=sister]'))


if __name__ == '__main__':
    parse()
