"""
lambda基本用法
"""

# 创建一个x，用来传参
demo = lambda x: x*2
print(demo(6))


def test(value):
    return value * 3


# 使用lambda间接调用函数，可用于GUI Button上传参
a = 6
demo = lambda: test(a)
print(demo())


# 使用lambda进行字符串长度排序
demo = ['foo', 'card', 'id', 'button', 'six']
print(sorted(demo, key=lambda x: len(x)))
