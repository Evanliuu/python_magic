# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
from numpy import *


x = linspace(-4, 4)  # 设置自变量的取值范围为[-4,4]，
y1 = math.e ** x  # 原函数
y2 = x**0  # 0阶
y3 = 1 + x  # 1阶
y4 = 1 + x + x**2/2  # 2阶
y5 = 1 + x + x**2/2 + x**3/6  # 3阶
plt.figure()
plt.xlim(-4, 4)
plt.ylim(-8, 12)
y_major_locator = MultipleLocator(2)
ax = plt.gca()
ax.yaxis.set_major_locator(y_major_locator)
l1, = plt.plot(x, y1, label='$\mathregular{\mathit{y}}$ = exp($\mathregular{\mathit{x}}$)')
l2, = plt.plot(x, y2, color='orange', linestyle=':', label='0th order')  # 设置函数线的颜色和线的样式
l3, = plt.plot(x, y3, color='green', linestyle=':', label='1st order')  # 设置函数线的颜色和线的样式
l4, = plt.plot(x, y4, color='red', linestyle=':', label='2nd order')  # 设置函数线的颜色和线的样式
l5, = plt.plot(x, y5, color='purple', linestyle=':', label='3rd order')  # 设置函数线的颜色和线的样式
plt.grid()  # 生成网格
plt.title('Approximating Exponential Function by Taylor Series at Origin', fontdict={'size': 11})
plt.xlabel('x', fontdict={'style': 'italic'})
plt.ylabel('y', fontdict={'style': 'italic'})
ax.legend(loc='lower right')
plt.show()  # 显示上面所绘制的所有图片
