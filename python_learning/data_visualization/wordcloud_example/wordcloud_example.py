# -*- coding:utf-8 -*-
import numpy as np
import jieba

from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image

__author__ = 'Evan'


def generate_word_cloud(text, background_image='', save_file_name=''):
    """
    读取文本信息生成词云图
    :param text: 词云文本
    :param background_image: 词云背景图片
    :param save_file_name: 保存图片的名称
    :return:
    """
    if background_image:
        img = Image.open(background_image)  # 读取本地图片
        img_array = np.array(img)  # 将图片装换为数组
    else:
        img_array = None
    wc = WordCloud(background_color='white',
                   width=600,
                   height=800,
                   mask=img_array,  # 添加图片背景框
                   font_path=r'C:\Windows\Fonts\STFANGSO.ttf',  # 如果是中文必须要添加这个，否则会显示成框框
                   max_words=2000,  # 设置最大字数
                   random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )
    text = ' '.join(jieba.cut(text))  # 使用jieba分词，精确模式切分
    wc.generate_from_text(text)  # 生成词云
    plt.imshow(wc)  # 使用plt加载图片
    plt.axis('off')  # 不显示坐标轴
    plt.show()  # 预览图片
    if save_file_name:
        wc.to_file(save_file_name)  # 保存词云图片到本地


if __name__ == '__main__':
    with open('template.txt', 'r') as f:
        txt = f.read()
    generate_word_cloud(text=txt, background_image='background.jpg', save_file_name='result.jpg')
