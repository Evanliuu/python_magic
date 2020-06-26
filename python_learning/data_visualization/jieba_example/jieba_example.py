# -*- coding:utf-8 -*-
"""jieba库支持三种分词模式：精确模式、全模式和搜索引擎模式
下面是三种模式的特点：
精确模式：试图将语句最精确的切分，不存在冗余数据，适合做文本分析
全模式：将语句中所有可能是词的词语都切分出来，速度很快，但是存在冗余数据
搜索引擎模式：在精确模式的基础上，对长词再次进行切分
"""
import jieba

__author__ = 'Evan'


def jieba_example():
    # 三种模式
    seg_str = "好好学习，天天向上。"
    print('精确模式：{}'.format(jieba.lcut(seg_str)))  # 精确模式，返回一个列表类型的结果
    print('全模式：{}'.format(jieba.lcut(seg_str, cut_all=True)))  # 全模式，使用 'cut_all=True' 指定
    print('搜索引擎模式：{}'.format(jieba.lcut_for_search(seg_str)))  # 搜索引擎模式

    # 统计中文词频
    txt = """七禽孟获三国中期，蜀国占据西蜀一带，这时南方孟获作乱。诸葛亮出征南蛮孟获，为了收买人心，七次俘获孟获而又其次将其释放。第七次释放孟获的时候，孟获终于归顺蜀国，诸葛亮平定了南方。
空城计三国中后期，诸葛亮出兵讨伐魏国，由于要地街亭失守，导致满盘皆输。诸葛亮被迫撤兵，司马懿大军追至，这时孔明手下的将领士兵基本都分配军务调完了，只剩二千五百军在城中。于是他命令偃旗息鼓，大开城门，独自在城楼上弹琴。司马懿疑心有伏兵。调头就撤兵。诸葛亮躲过一劫！
失街亭就是在空城计之前了，马谡自告奋勇去守街亭，结果犯了低级错误。被司马懿打败。蜀军被断了咽喉之路。被迫撤兵。
斩马谡马谡失了街亭。诸葛亮非常生气。想起了刘备临死前嘱咐他的话“吾观马谡，言过其实也”。后悔不已。悲痛了斩了立了军令状的马谡。
    """
    words = jieba.lcut(txt)  # 使用精确模式对文本进行分词
    counts = {}  # 通过键值对的形式存储词语及其出现的次数
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    print('统计中文词频：{}'.format(items))

    # 统计英文单词词频
    def get_text():
        article = """Nothing succeeds like confidence.When you are truly confident,it radiates from you like sunlight,
        and attracts success to you like a magnet.
        """
        article = article.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
            article = article.replace(ch, " ")  # 将文本中特殊字符替换为空格
        return article
    file_txt = get_text()
    words = file_txt.split()  # 对字符串进行分割，获得单词列表
    counts = {}
    for word in words:
        if len(word) == 1:  # 单个词语不计算在内
            continue
        else:
            counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序
    print('统计英文单词词频：{}'.format(items))


if __name__ == '__main__':
    jieba_example()
