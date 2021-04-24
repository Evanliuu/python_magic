# encoding=utf8
import cv2
import numpy as np


def change_background_color(picture, resize=(), changed_color='white', new_picture_name='new.jpg'):
    """
    改变图片的背景颜色
    :param picture: 原图片
    :param resize: 自定义像素比例（注意，排序是反的）
    :param changed_color: 改变后的颜色
    :param new_picture_name: 新图片名称
    :return:
    """
    # 背景颜色，BGR格式
    background_color = {
        'white': (255, 255, 255),
        'red': (0, 0, 255),
        'blue': (219, 142, 67),
    }

    img = cv2.imread(picture)  # 读取原图片

    # RGB转换HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])

    # 去除背景，低于lower_red和高于upper_red的部分变成0，lower_red～upper_red之间的值变成255
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # cv2.imshow('Mask', mask)  # 预览

    # 腐蚀膨胀
    erode = cv2.erode(mask, None, iterations=1)
    dilate = cv2.dilate(erode, None, iterations=1)

    # 遍历替换
    rows, cols, channels = img.shape
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                img[i, j] = background_color[changed_color]  # 替换颜色

    # 调整像素大小
    if resize:
        img = cv2.resize(img, resize, interpolation=cv2.INTER_CUBIC)

    # cv2.imshow('res', img)  # 预览
    cv2.imwrite(new_picture_name, img)  # 保存新图片
    # cv2.waitKey(0)  # 阻塞
    cv2.destroyAllWindows()  # 关闭所有窗口


if __name__ == '__main__':
    change_background_color(picture='1.jpg', changed_color='white', new_picture_name='new.jpg')
