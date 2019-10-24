from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import jieba


def generate_word_cloud(text='Python is a great programming language', image_name='sample.png'):
    """
    读取文本信息生成词云图
    :param text: 词云文本
    :param image_name: 生成图片的名称
    :return:
    """
    img = Image.open(r'picture.jpg')  # 打开本地图片
    img_array = np.array(img)  # 将图片装换为数组
    font = r'C:\Windows\Fonts\FZSTK.TTF'
    wc = WordCloud(background_color='white',
                   width=1000,
                   height=800,
                   mask=img_array,  # 根据图片背景框来填充词云
                   font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
                   )
    # TODO 普通构建词云文本
    # wc.generate(text)

    # 使用分词构建词云文本
    cut = jieba.cut(text)
    string = ' '.join(cut)
    wc.generate_from_text(string)
    # 运行结束后预览图片
    plt.imshow(wc)  # 用plt显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.figure()
    plt.show()  # 显示图片
    wc.to_file(image_name)  # 保存词云图片到本地


if __name__ == '__main__':
    generate_word_cloud(text='Importance of relative word frequencies for font-size. With relative_scaling=0,'
                             ' only word-ranks are considered. With relative_scaling=1,'
                             ' a word that is twice as frequent will have twice the size.'
                             ' If you want to consider the word frequencies and not only their rank,'
                             ' relative_scaling around .5 often looks good.')
