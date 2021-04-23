# encoding=utf8
import cv2
import numpy as np


def change_background_color(picture, changed_color='white', new_picture_name='new.jpg'):
    """
    改变图片的背景颜色
    :param picture:
    :param changed_color:
    :param new_picture_name:
    :return:
    """
    # BGR格式
    background_color = {
        'white': (255, 255, 255),
        'red': (0, 0, 255),
        'blue': (219, 142, 67),
    }

    img = cv2.imread(picture)

    # 转换hsv
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # rgb转hsv
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    # 去除背景，低于lower_red和高于upper_red的部分分别变成0，lower_red～upper_red之间的值变成255
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Mask', mask)

    # 遍历替换
    rows, cols, channels = img.shape
    for i in range(rows):
        for j in range(cols):
            if mask[i, j] == 255:
                img[i, j] = background_color[changed_color]  # 替换颜色

    cv2.imshow('res', img)  # 预览
    cv2.imwrite(new_picture_name, img)  # 保存新图片
    # cv2.waitKey(0)  # 阻塞
    cv2.destroyAllWindows()  # 关闭所有窗口


if __name__ == '__main__':
    change_background_color(picture='1.jpg', changed_color='red', new_picture_name='new.jpg')
