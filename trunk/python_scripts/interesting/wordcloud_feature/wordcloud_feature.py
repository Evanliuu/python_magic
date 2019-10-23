import wordcloud


def generate_word_cloud():
    # 生成词云对象
    w = wordcloud.WordCloud()
    # 构建词云文本
    w.generate("Python and WordCloud")
    # 输出词云图片
    w.to_file("outfile.png")


if __name__ == '__main__':
    generate_word_cloud()
